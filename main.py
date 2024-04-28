import discord
import discord.context_managers
from discord.ext import commands
from discord.utils import get
import asyncio
import psycopg2
from colorama import init, Fore, Back, Style
from collections import deque
from pytube import *
import yt_dlp
import re
from cogs.music import music
from cogs.help import help
from cogs.fun import fun
#Loop bot

#AIzaSyAKW1k0uuI26qFAJhM2Kj5oTQVVu27K7kc
voice_clients = {}
queues = {}
yt_dl_options = {"format": "bestaudio/best"}
ytdl = yt_dlp.YoutubeDL(yt_dl_options)
ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn -filter:a "volume=1"'}

def clean_filename(title):
    # Eliminar caracteres no válidos para nombres de archivo
    cleaned_title = re.sub(r'[\\/*?:"<>|]', '_', title)
    return cleaned_title

global_queue = deque()

def conectar():
    return psycopg2.connect(
        host='bocyvag1izqpqkhqbct4-postgresql.services.clever-cloud.com' ,
        user='ubgd5rionxagg2o3r25h',
        password='JNisggrGpkXGvr1yoVPnC3cOLOs8cf',
        port='50013',
        database='bocyvag1izqpqkhqbct4'
) 


def admin(x):
  conexion=conectar()
  cursor=conexion.cursor()
  valor=f'<@{x}>'
  sql="SELECT user FROM admins"
  cursor.execute(sql)
  usuarios = cursor.fetchall()
  s=False
  for usuario in usuarios:
    if usuario[0]==valor:
      s=True
  if s:
    conexion.close()
    cursor.close()
    return True
  else:
    cursor.close()
    conexion.close()
    return False



TOKEN='MTIyNTk2MzI5MDM1ODcxNDQ4Mg.GWqS6u.1o7tzl3li1nasji5HvkvW3zRMrVD_C8epWMiKA'
bot = commands.Bot(command_prefix="-", intents=discord.Intents.all(), help_command=None)


@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name='-help | /help'))
  print(Fore.GREEN,'''
    ______  _____  _____      _____  _   _  _      _____  _   _  _____ 
    | ___ \|  _  ||_   _|    |  _  || \ | || |    |_   _|| \ | ||  ___|
    | |_/ /| | | |  | |      | | | ||  \| || |      | |  |  \| || |__  
    | ___ \| | | |  | |      | | | || . ` || |      | |  | . ` ||  __| 
    | |_/ /\ \_/ /  | |      \ \_/ /| |\  || |____ _| |_ | |\  || |___ 
    \____/  \___/   \_/       \___/ \_| \_/\_____/ \___/ \_| \_/\____/       
        ''',Fore.WHITE)
  sinc =  await bot.tree.sync()
  #print('Slash commands sincronizados: ' + str(len(sinc)))
  print("\033[1;33m"+'Slash commands sincronizados: ' + str(len(sinc)) + '\033[0;m')
  

@bot.event
async def on_guild_join(guild):
  conection=conectar()
  cursor=conection.cursor()
  server=guild.id
  try:
    sql = f"CREATE SCHEMA s_{server}"
    cursor.execute(sql)
    conection.commit()
    sql=f'CREATE TABLE s_{server}.channels (channel VARCHAR(255), channel_id VARCHAR(255))'
    cursor.execute(sql)
    conection.commit()
    print('Se ah añadido un nuevo server a la base de datos')
  except:
    print('No se ah podido añadir el servidor')
  cursor.close()
  conection.close()
    
@bot.event
async def on_member_remove(member):
    conection=conectar()
    cursor=conection.cursor()
    serverid=member.guild.id
    sql = f"SELECT channel, channel_id FROM s_{serverid}.channels WHERE channel = 'leave'"
    cursor.execute(sql)
    servers=cursor.fetchall()    
    for i,n in servers:
        canal = int(n)
    canal_despedida = bot.get_channel(canal)
    mensaje = f'Gracias por salir {member.mention} y ojalá no vuelvas!'
    avatar_url = member.avatar.url
    embed = discord.Embed(title='Y no vuelvas', description=mensaje, color=808080)
    embed.set_thumbnail(url=avatar_url)
    embed.set_image(url='https://media.tenor.com/xTmaFemZXCgAAAAC/no-vuelvas-mas-el-incre%C3%ADble-mundo-de-gumball.gif')
    await canal_despedida.send(embed=embed)
    cursor.close()
    conection.close()

@bot.command()
async def add(ctx):
    conection=conectar()
    cursor=conection.cursor()
    server=ctx.guild.id
    try:
        sql = f"CREATE SCHEMA s_{server}"
        cursor.execute(sql)
        conection.commit()
        sql=f'CREATE TABLE s_{server}.channels (channel VARCHAR(255), channel_id VARCHAR(255))'
        cursor.execute(sql)
        conection.commit()
        print('Se ah añadido un nuevo server a la base de datos')
        await ctx.reply('Added')
    except:
        print('No se ah podido añadir el servidor')
    cursor.close()
    conection.close()





@bot.command()
async def add_admin(ctx, arg1):
  conection=conectar()
  cursor=conection.cursor()
  id=ctx.author.id
  si=admin(id)
  if si==True or id==791382250959798272:
    try:
      sql='''CREATE TABLE admins (user VARCHAR(255))'''
      cursor.execute(sql)
      sql= '''INSERT INTO admins (user) VALUES(%s)'''
      valor=(arg1,)
      cursor.execute(sql,valor)
      await ctx.reply('Usuario añadido como admin')
      conection.commit()
    except:
      try:
        sql= '''INSERT INTO admins (user) VALUES(%s)'''
        valor=(arg1,)
        cursor.execute('SELECT user FROM admins')
        users = cursor.fetchall()
        esta=False
        for i in users:
          if i==valor:
            esta=True
            await ctx.reply('El usuario ya  se encuentra como admin')
        if not esta:
          cursor.execute(sql,valor)
          await ctx.reply('Usuario añadido como admin')
        conection.commit()
      except:
        await ctx.reply('Ah ocurrido un error')
  else:
    await ctx.reply('Acceso dengado')
  cursor.close()
  conection.close()

@bot.tree.command(
  name='add_admin',
  description='Añade a un usuario como administrador'
)
async def add_admin(ctx: discord.Interaction, user: discord.User):
  conection=conectar()
  cursor=conection.cursor()
  id=ctx.author.id
  si=admin(id)
  if si==True:
    try:
      sql='''CREATE TABLE admins (user VARCHAR(255))'''
      cursor.execute(sql)
      sql= '''INSERT INTO admins (user) VALUES(%s)'''
      valor=(user,)
      cursor.execute(sql,valor)
      await ctx.reply('Usuario añadido como admin')
      conection.commit()
    except:
      try:
        sql= '''INSERT INTO admins (user) VALUES(%s)'''
        valor=(user,)
        cursor.execute('SELECT userid FROM admins')
        users = cursor.fetchall()
        esta=False
        for i in users:
          if i==valor:
            esta=True
            await ctx.reply('El usuario ya  se encuentra como admin')
        if not esta:
          cursor.execute(sql,valor)
          await ctx.reply('Usuario añadido como admin')
        conection.commit()
      except:
        await ctx.reply('Ah ocurrido un error')
  else:
    await ctx.reply('Acceso dengado')
  cursor.close()
  conection.close()

@bot.command()
async def enviar(ctx):
  conection=conectar()
  cursor=conection.cursor()
  usuario_id = ctx.author.id
  if usuario_id==791382250959798272:
    await ctx.send("Por favor, ingresa la ID del canal al que quieres enviar el mensaje:")
    def check(m):
        return m.author == ctx.message.author and m.channel == ctx.message.channel

    try:
        canalid = await bot.wait_for('message', check=check, timeout=30)
        canalid = int(canalid.content) 
    except TimeoutError:
        await ctx.send("Tiempo agotado. Comando cancelado.")
        return
    canal = bot.get_channel(canalid)

    if canal:
        await ctx.send("Por favor, ingresa el mensaje que quieres enviar:")

        try:
            mensaje = await bot.wait_for('message', check=check, timeout=30)
        except TimeoutError:
            await ctx.send("Tiempo agotado. Comando cancelado.")
            return
        await canal.send(mensaje.content)
        await ctx.send(f"Mensaje enviado correctamente al canal con ID {canalid}.")
    else:
        await ctx.send(f"No se pudo encontrar el canal con ID {canalid}.")
  else:
    await ctx.reply('Acceso denegado')
  cursor.close()
  conection.close()

@bot.tree.command(
  name='enviar',
  description='Haz que el bot envie el mensaje que quieras al canal que quieras'
)
async def enviar(ctx, canal: discord.TextChannel, mensaje: str):
  conection=conectar()
  cursor=conection.cursor()
  usuario_id = ctx.user.id
  e=admin(usuario_id)
  if e:
    await canal.send(mensaje)
    await ctx.response.send_message(f"Mensaje enviado correctamente al canal {canal}.")
  else:
    await ctx.response.send_message('Acceso denegado')
  cursor.close()
  conection.close()

@bot.command()
async def s(ctx):
  conection=conectar()
  cursor=conection.cursor()
  id=ctx.author.id
  print(ctx.guild.id)
  si=admin(id)
  if si:
    await ctx.reply('si')
  else:
    await ctx.reply('no')
  cursor.close()
  conection.close()
  
@bot.tree.command(
  name='set_leave_title',
  description='Set a title to the Embed that the bot will send when a user leave the server'
)
async def set_leave_title(ctx, url: str):
  conection=conectar()
  cursor=conection.cursor()
  serverid = ctx.guild.id
  sql = f"INSERT INTO s_{serverid}.channels (title) VALUES({url})"
  
    
@bot.command()
async def set_leavech(ctx, arg1):
  conection=conectar()
  cursor=conection.cursor()
  x=arg1
  x=x.replace('<#','').replace('>','')
  serverid=ctx.guild.id
  cursor.execute(f'SELECT channel,channel_id FROM s_{serverid}.channels')
  ids = cursor.fetchall()
  encontrado= False
  for i in ids:
    if serverid==int(i):
      cursor.execute(f"UPDATE s_{serverid}.channels SET channel_id = '{x}' WHERE channel = 'leave'")
      encontrado=True

  sql = f"INSERT INTO s_{serverid}.channels (channel, channel_id) VALUES('leave', {x})"
  cursor.execute(sql)
  try:
    sql= f'CREATE TABLE s_{serverid}.leavemsg (title VARCHAR(255), text VARCHAR(255), icon VARCHAR(255), image VARCHAR(255))'
    cursor.execute(sql)
  except:
    print(f'Ya existe s_{serverid}.leavemsg')
  sql = f"INSERT INTO s_{serverid}.leavemsg (title, text, icon, image) VALUES('','','','')"
  cursor.execute(sql)
  conection.commit()
  await ctx.reply('Leave channel has been added. Use -help leaveChannel to customize the leave message')
  cursor.close()
  conection.close()
  
@bot.command()
async def set_joinch(ctx, arg1):
  conection=conectar()
  cursor=conection.cursor()
  x=arg1
  x=x.replace('<#','').replace('>','')
  serverid=ctx.guild.id
  sql = f"INSERT INTO s_{serverid}.channels (channel, channel_id) VALUES('join', {x})"
  cursor.execute(sql)
  conection.commit()
  await ctx.reply('Welcome channel has been added')
  cursor.close()
  conection.close()
  

async def startcog():
  bot.add_cog(music(bot))
  bot.add_cog(help(bot))
  bot.add_cog(fun(bot))
  
asyncio.run(startcog())

bot.run(TOKEN)