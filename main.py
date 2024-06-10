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
import json

with open('config.json') as config_file:
    config = json.load(config_file)


voice_clients = {}
queues = {}
yt_dl_options = {"format": "bestaudio/best"}
ytdl = yt_dlp.YoutubeDL(yt_dl_options)
ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn -filter:a "volume=1"'}

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
  

async def startcog():
  await bot.add_cog(music(bot))
  await bot.add_cog(help(bot))
  await bot.add_cog(fun(bot))
  await bot.add_cog(ttt(bot))
  await bot.add_cog(guess(bot))
  
asyncio.run(startcog())

bot.run(TOKEN)