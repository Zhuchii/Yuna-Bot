import discord
import discord.context_managers
from discord.ext import commands, tasks 
from discord.utils import get
import asyncio
from colorama import init, Fore, Back, Style
from collections import deque
from youtube_search import YoutubeSearch
import yt_dlp




yt_dl_options = {
    "format": "bestaudio/best",
}
ffmpeg_options = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn -filter:a "volume=1"',
}

voice_clients = {}
queues = {}
queues_name = {}



class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @bot.command()
        async def play(ctx, *, link):
            if not link:
                return await ctx.send("Please provide a valid URL or search term.")

            if link.startswith("https://"):
                await play_url(ctx, link)
            else:
                await search_and_play(ctx, link)

        async def play_url(ctx, link):
            if ctx.author.voice is None:
                return await ctx.send("You must be in a voice channel first.")

            voice_client = voice_clients.get(ctx.guild.id)

            if not voice_client or not voice_client.is_connected():
                voice_client = await ctx.author.voice.channel.connect()
                voice_clients[ctx.guild.id] = voice_client

            ytdl = yt_dlp.YoutubeDL(yt_dl_options)
            data = await asyncio.to_thread(ytdl.extract_info, link, download=False)
            song = data["url"]
            song_name = data["title"]
            if ctx.guild.id not in queues_name:
                queues_name[ctx.guild.id] = []
            if ctx.guild.id not in queues:
                queues[ctx.guild.id] = []

            if voice_client.is_playing():
                queues[ctx.guild.id].append(link)
                queues_name[ctx.guild.id].append(song_name)
                return await ctx.send("Song added to queue!")
            else:
                player = discord.FFmpegOpusAudio(song, **ffmpeg_options)
                await ctx.send(f"🎵 Now playing: **{song_name}** 🎵")

                def after_playing(error):
                    coro = play_next(ctx)
                    fut = asyncio.run_coroutine_threadsafe(coro, bot.loop)
                    try:
                        fut.result()
                    except Exception as e:
                        print(f"Error in after_playing: {e}")

                voice_client.play(player, after=after_playing)

        async def search_and_play(ctx, query):
            results = YoutubeSearch(query, max_results=10).to_dict()

            if not results:
                return await ctx.send("No results were found")
            
            result_text = "\n".join([
                f"{idx + 1}. **{video['title']}** - {video['channel']} "
                for idx, video in enumerate(results)
            ])

            embed = discord.Embed(title='Please select one of the following results:', description=result_text, color=discord.Color.blue())
            await ctx.send(embed=embed)

            def check(m):
                return m.author == ctx.author and m.content.isdigit() and 1 <= int(m.content) <= 10

            response = await bot.wait_for("message", check=check, timeout=30)

            selected_index = int(response.content) - 1
            selected_video = results[selected_index]

            selected_video_url = f"https://www.youtube.com/watch?v={selected_video['id']}"

            await play_url(ctx, selected_video_url)

        async def play_next(ctx):
            if ctx.guild.id in queues and queues[ctx.guild.id]:
                next_song = queues[ctx.guild.id].pop(0)
                next_name = queues_name[ctx.guild.id].pop(0)
                await play_url(ctx, next_song)
            else:
                voice_client = voice_clients.get(ctx.guild.id)
                if voice_client and voice_client.is_connected():
                    await voice_client.disconnect()
                    del voice_clients[ctx.guild.id]

        @bot.command(name="pause")
        async def pause(ctx):
            voice_client = voice_clients.get(ctx.guild.id)
            if voice_client and voice_client.is_playing():
                voice_client.pause()
                await ctx.send("Paused the music.")

        @bot.command(name="resume")
        async def resume(ctx):
            voice_client = voice_clients.get(ctx.guild.id)
            if voice_client and voice_client.is_paused():
                voice_client.resume()
                await ctx.send("Resumed the music.")

        @bot.command(name="stop")
        async def stop(ctx):
            voice_client = voice_clients.get(ctx.guild.id)
            if voice_client:
                voice_client.stop()
                await voice_client.disconnect()
                del voice_clients[ctx.guild.id]
                await ctx.send("Music stopped.")

        @bot.command(name="skip")
        async def skip(ctx):
            voice_client = voice_clients.get(ctx.guild.id)
            if voice_client:
                voice_client.stop()
                await ctx.send("Skipped to the next song.")

        @bot.command(name="clear_queue")
        async def clear_queue(ctx):
            if ctx.guild.id in queues:
                queues[ctx.guild.id].clear()
                queues_name[ctx.guild.id].clear()
                await ctx.send("Queue cleared :3")
            else:
                await ctx.send("The queue is already empty!")

        @bot.command()
        async def queue(ctx):  
            if ctx.guild.id not in queues_name or not queues_name[ctx.guild.id]:
                return await ctx.send('The queue is empty!')
            
            results = ''
            for idx, name in enumerate(queues_name[ctx.guild.id], start=1):
                results += f'{idx}. {name}\n'

            embed = discord.Embed(title='**QUEUE**', description=results, color=discord.Color.blue())
            await ctx.send(embed=embed)