import discord
import discord.context_managers
from discord.ext import commands
from discord.utils import get
import random
from colorama import init, Fore, Back, Style
from pytube import *
import datetime
import os

ball_responses = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes, definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
]


tenor_api_key = 'AIzaSyAKW1k0uuI26qFAJhM2Kj5oTQVVu27K7kc'

class fun(commands.Cog):
  
  
    def __init__(self, bot):
        self.bot = bot
        self.gif_cache = {}
        
        # Precachear los GIFs por carpeta
        base_gif_folder = 'fun/gif'
        subfolders = os.listdir(base_gif_folder)  # Lista de carpetas dentro de 'fun/gif'

        # Cachea todos los GIFs en cada subcarpeta
        for subfolder in subfolders:
            folder_path = os.path.join(base_gif_folder, subfolder)
            if os.path.isdir(folder_path):
                # Carga todos los GIFs de esta carpeta en la caché
                self.gif_cache[subfolder] = [
                    os.path.join(folder_path, gif) for gif in os.listdir(folder_path) if gif.endswith(".gif")
                ]
    
    
        @bot.tree.command(
        name='roll',
        description='Roll a random number',
        )
        async def roll(ctx: discord.Interaction, min_num: int, max_num: int):
            try:
                if min_num<max_num:
                    await ctx.response.send_message(random.randint(min_num, max_num))
                else:
                    await ctx.response.send_message('El numero minimo debe ser mayor que el maximo')
            except Exception as e:
                pass

        @bot.tree.command(
            name="8ball",
            description='Get a random response about your question'
            )
        async def _8ball(ctx, question: str):
            random.shuffle(ball_responses)
            
            
            embed = discord.Embed(title = question, description = ball_responses[0], color= discord.Color.blue())
            embed.add_field(name='', value='                          ')
            await ctx.response.send_message(embed=embed)

        @bot.command()
        async def hug(ctx, arg1=None):
            if arg1!=None:
                author = ctx.author.id
                with open('fun/gif/hug.txt', 'r') as f:
                    enlaces = [linea.strip() for linea in f]
                
                if enlaces:
                    enlace_aleatorio = random.choice(enlaces)
                
                embed = discord.Embed(title ='', description= f'<@{author}> is hugging {arg1} (づ ˆᴗˆ)づ♡', color=discord.Color.blue())
                embed.set_image(url=enlace_aleatorio)
                embed.timestamp = datetime.datetime.now()
                await ctx.send(embed=embed)
            else:
                emoji_id = 1231279253581205554  # ID del emoji
                emoji = bot.get_emoji(emoji_id)
                if emoji is not None:
                    await ctx.reply(f'You have to tag someone to do that {emoji}')
                else:
                    await ctx.reply('You have to tag someone to do that')
        
        @bot.command()
        async def angry(ctx):
            author = ctx.author.id
                
            with open('fun/gif/angry.txt', 'r') as f:
                enlaces = [linea.strip() for linea in f]
                enlace_aleatorio = random.choice(enlaces)
            
            embed = discord.Embed(title ='', description= f'<@{author}> is angry ๑(•̀⌓•́ )ﾉ', color=discord.Color.blue())
            embed.set_image(url=enlace_aleatorio)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)

        @bot.command()
        async def bye(ctx, arg1=None):
            author = ctx.author.id
            if arg1 == None:
                message = f'<@{author}> says goodbyeヾ(￣▽￣)~'
            else:
                message = message = f'<@{author}> says goodbye to {arg1}ヾ(˵•̀ ᴗ -˵) ✧'
                
            with open('fun/gif/bye.txt', 'r') as f:
                enlaces = [linea.strip() for linea in f]
                enlace_aleatorio = random.choice(enlaces)
            
            embed = discord.Embed(title="",description=message, color=discord.Color.blue())
            embed.set_image(url=enlace_aleatorio)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
            
        @bot.command()
        async def kiss(ctx, arg1=None):  
            if arg1!=None:
                author = ctx.author.id
                with open('fun/gif/kiss.txt', 'r') as f:
                    enlaces = [linea.strip() for linea in f]
                    enlace_aleatorio = random.choice(enlaces)
                embed = discord.Embed(title="",description=f'<@{author}> is kissing {arg1} (づ ￣ ³￣)づ♡( ๑‾̀◡‾́)σ»', color=discord.Color.blue())
                embed.set_image(url=enlace_aleatorio)
                embed.timestamp = datetime.datetime.now()
                await ctx.send(embed=embed)
            else:
                emoji_id = 1231279253581205554  # ID del emoji
                emoji = bot.get_emoji(emoji_id)
                if emoji is not None:
                    await ctx.reply(f'You have to tag someone to do that {emoji}')
                else:
                    await ctx.reply('You have to tag someone to do that')
        
        @bot.command()
        async def poke(ctx, arg1=None):
            if arg1!=None:
                author = ctx.author.id
                hug_gifs = self.gif_cache.get("poke", [])
                
                if hug_gifs:
                    # Elige un GIF al azar de la caché
                    gif_path = random.choice(hug_gifs)
                
                # Crea un embed
                embed = discord.Embed(title="",description=f'<@{author}> is trying to poke {arg1} ( ๑‾̀◡‾́)σ» so annoying!', color=discord.Color.blue())
                embed.set_image(url=f"attachment://{os.path.basename(gif_path)}")
                embed.timestamp = datetime.datetime.now()
            # Envía el embed con el GIF adjunto
                with open(gif_path, "rb") as file:
                    await ctx.send(embed=embed, file=discord.File(file, filename=os.path.basename(gif_path)))
            else:
                emoji_id = 1231279253581205554  # ID del emoji
                emoji = bot.get_emoji(emoji_id)
                if emoji is not None:
                    await ctx.reply(f'You have to tag someone to do that {emoji}')
                else:
                    await ctx.reply('You have to tag someone to do that')

