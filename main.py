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
from cogs.ttt import ttt
from cogs.guess import guess
from cogs.moderation import moderation
from cogs.misc import misc
from discord import app_commands
from cogs.ai import ai
from cogs.config import confif
import sqlite3
import datetime

import json

with open('config.json') as config_file:
    config = json.load(config_file)

def conection(guild):
    return sqlite3.connect(f'database/{guild}.db')

def clean_filename(title):
    cleaned_title = re.sub(r'[\\/*?:"<>|]', '_', title) 
    return cleaned_title

def conectar():
    host = config['host']
    user = config['user']
    password = config['password']
    port = config['port']
    database = config['database']

    return psycopg2.connect(
        host=host,
        user=user,
        password=password,
        port=port,
        database=database
    )


TOKEN=config['token']
bot = commands.Bot(command_prefix=config['prefix'], intents=discord.Intents.all(), help_command=None)


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
  
  print("\033[1;33m"+'Slash commands sincronizados: ' + str(len(sinc)) + '\033[0;m')
  
@bot.event
async def on_member_join(member):
  guild = member.guild.id
  guilded = await bot.fetch_guild(guild)
  conect = conection(guild)
  cursor = conect.cursor()
  memberid = member.id
  user = await bot.fetch_user(int(memberid))
  try:
    cursor.execute('SELECT * FROM welcome_msg WHERE id == 1')
    row = cursor.fetchone()
    print(row)
    if row:
        title=(row[1])
        content=(row[2])
        image=(row[3])
        channel=(row[4])
    try:
      if channel:
        print(channel)
        channel_parts = str(channel).split('/')
        if channel_parts:
          channel_id = channel_parts[-1]
          channel = int(channel_id)
      else:
        print("Channel URL is empty or not set")
    except ValueError as e:
      print(f"Error converting channel to int: {e}")
    except Exception as e:
      print(f"Unexpected error: {e}")
    contente = f'{user.mention} just joined!'
    channel = bot.get_channel(int(channel))
    embed = discord.Embed(title =str(title).replace('{user}', f'{user}').replace('{server}', f'{guilded}'), description=(f'{content}').replace('{user}', f'{user}').replace('{server}', f'{guilded}'), color= discord.Color.blue())
    embed.set_thumbnail(url=str(user.avatar.url))
    embed.timestamp = datetime.datetime.now()
    try:
      embed.set_image(url=image)
      await channel.send(content=contente, embed=embed)
    except:
      embed = discord.Embed(title = title, description=f'{content}', color= discord.Color.blue())
      await channel.send(content=content, embed=embed)
  except Exception as e:
    print(e)
async def startcog():
  await bot.add_cog(music(bot))
  await bot.add_cog(help(bot))
  await bot.add_cog(fun(bot))
  await bot.add_cog(ttt(bot))
  await bot.add_cog(guess(bot))
  await bot.add_cog(moderation(bot))
  await bot.add_cog(misc(bot))
  await bot.add_cog(ai(bot))
  await bot.add_cog(confif(bot))

asyncio.run(startcog())


bot.run(TOKEN)
