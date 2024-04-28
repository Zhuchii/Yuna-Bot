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
                embed = discord.Embed(title ='Commads', description= 'A list of all the commands', color= discord.Color.blue())
                embed.add_field(name='', value='-------------------------\n', inline=False)
                embed.add_field(name='set_leavech', value='Set the leave channel\n', inline=False)
                embed.add_field(name='set_joinch', value='Set the welcome channel\n', inline=False)
                embed.add_field(name='music', value='Show all the music commands')
                embed.add_field(name='enviar', value='Send any message u want to any channel on the server (only available with Slash commands)\n', inline=False)
                embed.set_thumbnail(url='https://i.pinimg.com/originals/2a/0a/2a/2a0a2a1021e29f96173e35bc17f5b326.gif')
                embed.set_image(url='https://qph.cf2.quoracdn.net/main-qimg-1a5fff09f7f19543037efe0cf1dbf4b3')
                embed.timestamp = datetime.datetime.now()
                await ctx.send(content=None, embed=embed)
            elif arg1=='add_admin':
                embed = discord.Embed(title ='>add_admin', description= f'Used to add a user as admin\n\nUsage:\n\n  >add_admin <@{autor}>', color= discord.Color.blue())
                await ctx.send(content=None, embed=embed)
            elif arg1=='set_leavech':
                embed = discord.Embed(title ='-set_leavech', description= f'It is used to set the channel through which the bot will send goodbye messages every time a user leaves the server.\n\nEjemplo de uso:\n\n  -set_leavech <#{canal}>', color= discord.Color.blue())
                await ctx.send(content=None, embed=embed)
            elif arg1=='set_joinch':
                embed = discord.Embed(title ='-set_joinch', description= f'It is used to set the channel through which the bot will send welcome messages every time a user joins the server.\n\nEjemplo de uso:\n\n  -set_joinch <#{canal}>', color= discord.Color.blue())
                await ctx.send(content=None, embed=embed)
            elif arg1=='play':
                embed = discord.Embed(title ='-play', description= f'Use it to play music on the voice channel (Only works with youtube links)\n\nUsage:\n\n  -play https://www.youtube.com/watch?v=dQw4w9WgXcQ', color= discord.Color.blue())
                await ctx.response.send_message(content=None, embed=embed)
            elif arg1=='music':
                embed = discord.Embed(title ='Commads', description= 'A list of all the commands', color= discord.Color.blue())
                embed.add_field(name='play', value='Plays music (Using youtube links)\n', inline=False)
                embed.add_field(name='stop', value='Stop playing songs\n', inline=False)
                embed.add_field(name='skip', value='Skip the current song and play the next song in the playlist\n', inline=False)
                embed.add_field(name='queue', value='Add a song to the playlist', inline=False)
                embed.add_field(name='pause', value='Pause the  current song', inline=False)
                embed.add_field(name='resume', value='Resume the current paused song',inline=False)
                embed.add_field(name='clear_queue', value='Clear the playlist')
                embed.add_field(name='pause', value='Pause the  current song', inline=False)
                embed.add_field(name='resume', value='Resume the current paused song',inline=False)
                embed.set_thumbnail(url='https://i.imgur.com/UzaXeJV.png')
                embed.set_image(url='https://i.imgur.com/WaAFj1k.jpeg')
                await ctx.send(content=None, embed=embed)
            elif arg1=='enviar':
                embed = discord.Embed(title ='/enviar', description= f'Se usa para enviar un mensaje a otro canal mediante el bot, bueno para hacer anuncion :D\n\nEjemplo de uso:\n\nSolo disponible con Slash /enviar (Es mas intuitivo!)', color= discord.Color.blue())
                await ctx.response.send_message(content=None, embed=embed)
            elif arg1 == 'roleplay':
                embed = discord.Embed(
                    title='Acciones de Roleplay',
                    description='Aquí están las acciones que puedes hacer.',
                    color=discord.Color.blue()
                )

                # Dividimos las acciones en tres listas para las columnas
                acciones_columna1 = ["abrazo", "beso", "golpe", "caricia", "aplauso"]
                acciones_columna2 = ["saludo", "despedida", "broma", "canto", "baile"]
                acciones_columna3 = ["chiste", "comida", "bebe", "duerme", "susurro"]

                # Agregar campos para cada columna
                embed.add_field(name='Acciones 1', value="\n".join(acciones_columna1), inline=True)
                embed.add_field(name='Acciones 2', value="\n".join(acciones_columna2), inline=True)
                embed.add_field(name='Acciones 3', value="\n".join(acciones_columna3), inline=True)

                await ctx.send(embed=embed)
            else:
                await ctx.reply(f'Comando {arg1} no reconocido, usa -ayuda para ver una guia de todos los comandos')

        @bot.tree.command(
        name='ayuda',
        description='Muestra una guia de uso de comandos'
        )
        async def ayuda(ctx: discord.Interaction, comando: str=None):
            autor=ctx.user.id
            canal=ctx.channel.id
            if comando is None:
                embed = discord.Embed(title ='Comandos', description= 'Guia de todos los comandos del bot', color= discord.Color.blue())
                embed.add_field(name='', value='-------------------------\n', inline=False)
                embed.add_field(name='set_leavech', value='Establece el canal de despedidas\n', inline=False)
                embed.add_field(name='set_joinch', value='Establece el canal de bienvenidas\n', inline=False)
                embed.add_field(name='music', value='Show all the music commands')
                embed.add_field(name='enviar', value='Send any message u want to any channel on the server (only available with Slash commands)\n', inline=False)
                embed.set_thumbnail(url='https://i.pinimg.com/originals/2a/0a/2a/2a0a2a1021e29f96173e35bc17f5b326.gif')
                embed.set_image(url='https://qph.cf2.quoracdn.net/main-qimg-1a5fff09f7f19543037efe0cf1dbf4b3')
                embed.timestamp = datetime.datetime.now()
                await ctx.response.send_message(content=None, embed=embed)
            elif comando=='add_admin':
                embed = discord.Embed(title ='>add_admin', description= f'Se usa para añadir un usuario como admin\n\nEjemplo de uso:\n\n  >add_admin <@{autor}>', color= discord.Color.blue())
                await ctx.response.send_message(content=None, embed=embed)
            elif comando=='set_leavech':
                embed = discord.Embed(title ='-set_leavech', description= f'Se usa para establecer el canal por donde el bot enviara mensajes de despedida cada vez que un usuario salga del servidor\n\nEjemplo de uso:\n\n  -set_leavech <#{canal}>', color= discord.Color.blue())
                await ctx.response.send_message(content=None, embed=embed)
            elif comando=='set_joinch':
                embed = discord.Embed(title ='-set_joinch', description= f'Se usa para establecer el canal por donde el bot enviara mensajes de bienvenida cada vez que un usuario se una al servidor\n\nEjemplo de uso:\n\n  -set_joinch <#{canal}>', color= discord.Color.blue())
                await ctx.response.send_message(content=None, embed=embed)
            elif comando=='play':
                embed = discord.Embed(title ='-play', description= f'Se usa para reproducir música en el canal en el canal de voz\n\nEjemplo de uso:\n\n  -play https://www.youtube.com/watch?v=dQw4w9WgXcQ', color= discord.Color.blue())
                await ctx.response.send_message(content=None, embed=embed)
            elif comando=='music':
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
            elif comando=='enviar':
                embed = discord.Embed(title ='/enviar', description= f'Se usa para enviar un mensaje a otro canal mediante el bot, bueno para hacer anuncion :D\n\nEjemplo de uso:\n\nSolo disponible con Slash /enviar (Es mas intuitivo!)', color= discord.Color.blue())
                await ctx.response.send_message(content=None, embed=embed)
            else:
                await ctx.response.send_message(f'Comando {comando} no reconocido, usa -ayuda para ver una guia de todos los comandos')