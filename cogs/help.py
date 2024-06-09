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
            if arg1 is None:
                embed = discord.Embed(title ='Commands', description= 'A list of all the commands', color= discord.Color.blue())
                embed.add_field(name='', value='-------------------------\n', inline=False)
                embed.add_field(name='music', value='Show all the music commands', inline=False)
                embed.add_field(name='roleplay', value='some actions that you can send to do some roleplay with your friends (if you have any)', inline=False)
                embed.add_field(name='fun', value='Show all the fun and minigames commands', inline=False)
                embed.set_thumbnail(url='https://i.pinimg.com/originals/2a/0a/2a/2a0a2a1021e29f96173e35bc17f5b326.gif')
                embed.set_image(url='https://qph.cf2.quoracdn.net/main-qimg-1a5fff09f7f19543037efe0cf1dbf4b3')
                embed.timestamp = datetime.datetime.now()
                await ctx.send(content=None, embed=embed)
            elif arg1=='music':
                embed = discord.Embed(title ='Commads', description= 'A list of all the commands', color= discord.Color.blue())
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
                await ctx.send(content=None, embed=embed)
            elif arg1 == 'roleplay':
                embed = discord.Embed(
                    title='All the roleplay actions',
                    description='Here are all the roleplay actions that you can do. (if u dont have friends to kiss u can also tag me >.<)',
                    color=discord.Color.blue()
                )
                
                acciones_columna1 = [" **hug**", " **kiss**", " **poke**", " **bye**", " **blush**"]
                acciones_columna2 = ["**confused**", "**happy**", "**hi**", "**angry**", ""]
                embed.add_field(name='', value="\n\n".join(acciones_columna1), inline=True)
                embed.add_field(name='', value="\n\n".join(acciones_columna2), inline=True)
                await ctx.send(embed=embed)
            else:
                await ctx.reply(f'Command {arg1} not recognized, use -help for a guide to all commands')

        @bot.tree.command(
        name='help',
        description='Show the help command'
        )
        async def help(ctx: discord.Interaction, command: str=None):
            autor=ctx.user.id
            canal=ctx.channel.id
            if command is None:
                embed = discord.Embed(title ='Commands', description= 'A list of all the commands', color= discord.Color.blue())
                embed.add_field(name='', value='-------------------------\n', inline=False)
                embed.add_field(name='music', value='Show all the music commands', inline=False)
                embed.add_field(name='roleplay', value='some actions that you can send to do some roleplay with your friends (if you have any)', inline=False)
                embed.add_field(name='fun', value='Show all the fun and minigames commands', inline=False)
                embed.set_thumbnail(url='https://i.pinimg.com/originals/2a/0a/2a/2a0a2a1021e29f96173e35bc17f5b326.gif')
                embed.set_image(url='https://qph.cf2.quoracdn.net/main-qimg-1a5fff09f7f19543037efe0cf1dbf4b3')
                embed.timestamp = datetime.datetime.now()
                await ctx.response.send_message(content=None, embed=embed)
            elif command=='music':
                embed = discord.Embed(title ='Music commads', description= 'A list of all the music commads', color= discord.Color.blue())
                embed.add_field(name='play', value='Plays music (Using youtube links)\n', inline=False)
                embed.add_field(name='stop', value='Stop playing songs\n', inline=False)
                embed.add_field(name='skip', value='Skip the current song and play the next song in the playlist\n', inline=False)
                embed.add_field(name='queue', value='Add a song to the playlist', inline=False)
                embed.add_field(name='pause', value='Pause the  current song', inline=False)
                embed.add_field(name='resume', value='Resume the current paused song',inline=False)
                embed.add_field(name='clear_queue', value='Clear the playlist')
                embed.set_thumbnail(url='https://i.imgur.com/UzaXeJV.png')
                embed.set_image(url='https://i.imgur.com/WaAFj1k.jpeg')
                await ctx.response.send_message(content=None, embed=embed)
            elif command=='fun':
                embed = discord.Embed(title ='Fun', description= 'A list of all the Fun commands', color= discord.Color.blue())
                embed.add_field(name='wordle', value='Play the classic wordle game\n', inline=False)
                embed.add_field(name='ttt', value='TIC TAC TOE minigame\n', inline=False)
                await ctx.send(content=None, embed=embed)
            elif command == 'roleplay':
                embed = discord.Embed(
                    title='All the roleplay actions',
                    description='Here are all the roleplay actions that you can do. (if u dont have friends to kiss u can also tag me >.<)',
                    color=discord.Color.blue()
                )
                
                acciones_columna1 = [" **hug**", " **kiss**", " **poke**", " **bye**", " **blush**"]
                acciones_columna2 = ["**confused**", "**happy**", "**hi**", "**angry**", ""]
                embed.add_field(name='', value="\n\n".join(acciones_columna1), inline=True)
                embed.add_field(name='', value="\n\n".join(acciones_columna2), inline=True)
                await ctx.send(embed=embed)
            else:
                await ctx.reply(f'Command {command} not recognized, use -help for a guide to all commands')