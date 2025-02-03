import discord
import discord.context_managers
from discord.ext import commands
from discord.utils import get
import datetime
from pytube import *





class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


        @bot.command()
        async def help(ctx, arg1=None):
            autor=ctx.author.id
            canal=ctx.channel.id
            arg1 = str(arg1).lower()
            if arg1=='music':
                embed = discord.Embed(title ='Music', description= 'A list of all the music commands', color= discord.Color.blue())
                embed.add_field(name='play', value='Plays music (Using youtube links)\n', inline=False)
                embed.add_field(name='stop', value='Stop playing songs\n', inline=False)
                embed.add_field(name='skip', value='Skip the current song and play the next song in the playlist\n', inline=False)
                embed.add_field(name='pause', value='Pause the  current song', inline=False)
                embed.add_field(name='resume', value='Resume the current paused song',inline=False)
                embed.add_field(name='clear_queue', value='Clear the playlist',inline=False)
                embed.set_thumbnail(url='https://i.imgur.com/UzaXeJV.png')
                embed.set_image(url='https://i.imgur.com/WaAFj1k.jpeg')
                await ctx.send(content=None, embed=embed)
            elif arg1=='fun':
                embed = discord.Embed(title ='Fun', description= 'A list of all the Fun commands', color= discord.Color.blue())
                embed.add_field(name='wordle', value='Play the classic wordle game\n', inline=False)
                embed.add_field(name='ttt', value='TIC TAC TOE minigame\n', inline=False)
                embed.add_field(name='guess', value='Try to guess the anime character by an image\n', inline=False)
                await ctx.send(content=None, embed=embed)
            elif arg1 == 'roleplay':
                embed = discord.Embed(
                    title='All the roleplay actions',
                    description='Some actions that you can send to do some roleplay with your friends (if you have any)',
                    color=discord.Color.blue()
                )
                
                acciones_columna1 = [" **hug**", " **kiss**", " **poke**", " **bye**", " **blush**"]
                acciones_columna2 = ["**confused**", "**happy**", "**hi**", "**angry**", ""]
                embed.add_field(name='', value="\n\n".join(acciones_columna1), inline=True)
                embed.add_field(name='', value="\n\n".join(acciones_columna2), inline=True)
                await ctx.send(embed=embed)
            elif arg1=='moderation':
                embed = discord.Embed(title ='moderation', description= 'A list of all the moderation commands', color= discord.Color.blue())
                embed.add_field(name='kick', value='Kick an user from your server')
                embed.add_field(name='ban', value='ban an user from your server')
                embed.add_field(name='timeout', value='Timeout a member for a specified time')
                await ctx.send(embed=embed)
            elif arg1=='misc':
                embed = discord.Embed(title ='Misc', description= 'A list of all the misc commands', color= discord.Color.blue())
                embed.add_field(name='server_info', value='Show all the information about the server')
                embed.add_field(name='user_info', value='Show information about an user')
                embed.add_field(name='imagine', value='Generate images using AI\n', inline=False)
                await ctx.send(embed=embed)
            elif arg1=='setup':
                embed = discord.Embed(title ='Setup', description= 'A list of all the setup commands and usefull information to use it in a better way', color= discord.Color.blue())
                embed.add_field(name='set', value='show a list to access and customize some commands in a more fastest way\n')
                embed.add_field(name=' ', value=' ',inline=False)
                embed.add_field(name=' ', value=' ',inline=False)
                embed.add_field(name=' ', value=' ',inline=False)
                embed.add_field(name='Usefull information', value='When customizing a command or a custom embed use the following expresions:\n\n **{user}**: Use in welcome or leave message to mention the user that joined or leave the server\n **{server}**: Use in welcome or leave message to name the server on the embeds\n\n\n\n', inline=False)
                embed.add_field(name=' ', value=' ',inline=False)
                embed.add_field(name=' ', value=' ',inline=False)
                embed.add_field(name=' ', value=' ',inline=False)
                embed.add_field(name='How to get channel ID?', value='When mentioning a channel in the chat **instead of sending #example_channel** send **\\#example_channel** it will send something like this <#920746581432413856340> that **numbers bettween the <>** are the **ID** of the channel.', inline=False)
                embed.add_field(name='A more easy way to mention a channel?', value='In the welcome message or any other message u can also just paste the link to the channel in the channel box or just to mention in the message and this will also work', inline=False)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title ='Commands', description= 'A list of all the commands', color= discord.Color.blue())
                embed.add_field(name='Choose a category\n', value='', inline=False)
                embed.add_field(name='music', value='', inline=False)
                embed.add_field(name='roleplay', value='', inline=False)
                embed.add_field(name='fun', value='', inline=False)
                embed.add_field(name='moderation', value='', inline=False)
                embed.add_field(name='misc', value='', inline=False)
                embed.add_field(name='setup', value='', inline=False)
                embed.set_thumbnail(url='https://i.imgur.com/2AZlLPI.png')
                embed.set_image(url='https://i.imgur.com/bpZmtcTl.png')
                embed.add_field(name='', value='\n\n\nNote: If your found any bug pls send me a DM to zhuchii and ill fix it.')
                embed.timestamp = datetime.datetime.now()
                await ctx.send(content=None, embed=embed)

        @bot.tree.command(
        name='help',
        description='Show the help command'
        )
        async def help(ctx: discord.Interaction, command: str=None):
            autor=ctx.user.id
            canal=ctx.channel.id
            if command=='music':
                embed = discord.Embed(title ='Music commads', description= 'A list of all the music commads', color= discord.Color.blue())
                embed.add_field(name='play', value='Plays music (Using youtube links)\n', inline=False)
                embed.add_field(name='stop', value='Stop playing songs\n', inline=False)
                embed.add_field(name='skip', value='Skip the current song and play the next song in the playlist\n', inline=False)
                embed.add_field(name='queue', value='Add a song to the playlist', inline=False)
                embed.add_field(name='pause', value='Pause the  current song', inline=False)
                embed.add_field(name='resume', value='Resume the current paused song',inline=False)
                embed.add_field(name='clear_queue', value='Clear the playlist')
                embed.set_thumbnail(url='https://i.imgur.com/2AZlLPI.png')
                embed.set_image(url='https://i.imgur.com/WaAFj1k.jpeg')
                await ctx.response.send_message(content=None, embed=embed)
            elif command == 'roleplay':
                embed = discord.Embed(
                    title='Roleplay',
                    description='Some actions that you can send to do some roleplay with your friends (if you have any)',
                    color=discord.Color.blue()
                )
                
                acciones_columna1 = [" **hug**", " **kiss**", " **poke**", " **bye**", " **blush**"]
                acciones_columna2 = ["**confused**", "**happy**", "**hi**", "**angry**", ""]
                embed.add_field(name='', value="\n\n".join(acciones_columna1), inline=True)
                embed.add_field(name='', value="\n\n".join(acciones_columna2), inline=True)
                await ctx.response.send_message(content=None, embed=embed)
            elif command=='fun':
                embed = discord.Embed(title ='Fun', description= 'A list of all the Fun commands', color= discord.Color.blue())
                embed.add_field(name='wordle', value='Play the classic wordle game\n', inline=False)
                embed.add_field(name='ttt', value='TIC TAC TOE minigame\n', inline=False)
                embed.add_field(name='guess', value='Try to guess the anime character by an image\n', inline=False)
                await ctx.response.send_message(content=None, embed=embed)
            elif command=='moderation':
                embed = discord.Embed(title ='Moderation', description= 'A list of all the moderation commands', color= discord.Color.blue())
                embed.add_field(name='kick', value='Kick an user from your server')
                embed.add_field(name='ban', value='ban an user from your server')
                embed.add_field(name='timeout', value='Timeout a member for a specified time')
                await ctx.response.send_message(content=None, embed=embed)
            elif command=='misc':
                embed = discord.Embed(title ='Misc', description= 'A list of all the misc commands', color= discord.Color.blue())
                embed.add_field(name='server_info', value='Show all the information about the server')
                embed.add_field(name='user_info', value='Show information about an user')
                embed.add_field(name='imagine', value='Generate images using AI\n', inline=False)
                await ctx.response.send_message(content=None, embed=embed)
            elif command=='setup':
                embed = discord.Embed(title ='Setup', description= 'A list of all the setup commands and usefull information to use it in a better way', color= discord.Color.blue())
                embed.add_field(name='set', value='show a list to access and customize some commands in a more fastest way\n')
                embed.add_field(name=' ', value=' ',inline=False)
                embed.add_field(name=' ', value=' ',inline=False)
                embed.add_field(name=' ', value=' ',inline=False)
                embed.add_field(name='Usefull information', value='When customizing a command or a custom embed use the following expresions:\n\n **{user}**: Use in welcome or leave message to mention the user that joined or leave the server\n **{server}**: Use in welcome or leave message to name the server on the embeds\n\n\n\n', inline=False)
                embed.add_field(name=' ', value=' ',inline=False)
                embed.add_field(name=' ', value=' ',inline=False)
                embed.add_field(name=' ', value=' ',inline=False)
                embed.add_field(name='How to get channel ID?', value='When mentioning a channel in the chat **instead of sending #example_channel** send **\\#example_channel** it will send something like this <#920746581432413856340> that **numbers bettween the <>** are the **ID** of the channel.', inline=False)
                embed.add_field(name='A more easy way to mention a channel?', value='In the welcome message or any other message u can also just paste the link to the channel in the channel box or just to mention in the message and this will also work', inline=False)
                await ctx.response.send_message(content=None, embed=embed)
            else:
                embed = discord.Embed(title ='Commands', description= 'A list of all the commands', color= discord.Color.blue())
                embed.add_field(name='Choose a category\n', value='', inline=False)
                embed.add_field(name='music', value='', inline=False)
                embed.add_field(name='roleplay', value='', inline=False)
                embed.add_field(name='fun', value='', inline=False)
                embed.add_field(name='moderation', value='', inline=False)
                embed.add_field(name='misc', value='', inline=False)
                embed.add_field(name='setup', value='', inline=False)
                embed.set_thumbnail(url='https://i.imgur.com/2AZlLPI.png')
                embed.set_image(url='https://i.imgur.com/bpZmtcTl.png')
                embed.add_field(name='', value='\n\n\nNote: If your found any bug pls send me a DM to zhuchii and ill fix it.')
                embed.timestamp = datetime.datetime.now()
                await ctx.send(content=None, embed=embed)