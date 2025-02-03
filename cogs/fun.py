import discord
import discord.context_managers
from discord.ext import commands
from discord.utils import get
import random
import time
from colorama import init, Fore, Back, Style
from pytube import *
import datetime
import wordle
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

words_es=wordle.es
words_en=wordle.en

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.gif_cache = {}
    
    
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

        @bot.command(
            name="8ball",
            description='Get a random response about your question',
            alias=['8ball']
            )
        async def _8ball(ctx, *args):
            link = " ".join(args).lstrip()
            random.shuffle(ball_responses)

            embed = discord.Embed(title = link, description = ball_responses[0], color= discord.Color.blue())
            embed.add_field(name='', value='                          ')
            await ctx.send(embed=embed)
        
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
                if arg1=='<@1225963290358714482>':
                    message= 'w~wh~why did y-you k-ki-kissed me suddenly (//▽//)'
                else:
                    message=f'<@{author}> is kissing {arg1} (づ ￣ ³￣)づ♡'
                
                with open('fun/gif/kiss.txt', 'r') as f:
                    enlaces = [linea.strip() for linea in f]
                    enlace_aleatorio = random.choice(enlaces)
                embed = discord.Embed(title="",description=message, color=discord.Color.blue())
                embed.set_image(url=enlace_aleatorio)
                embed.timestamp = datetime.datetime.now()
                await ctx.send(embed=embed)
            else:
                emoji_id = 1231279253581205554
                emoji = bot.get_emoji(emoji_id)
                if emoji is not None:
                    await ctx.reply(f'You have to tag someone to do that {emoji}')
                else:
                    await ctx.reply('You have to tag someone to do that')
        
        @bot.command()
        async def poke(ctx, arg1=None):
            if arg1!=None:
                author = ctx.author.id
                with open('fun/gif/poke.txt', 'r') as f:
                    enlaces = [linea.strip() for linea in f]
                
                if enlaces:
                    enlace_aleatorio = random.choice(enlaces)
                
                embed = discord.Embed(title ='', description= f'<@{author}> is annoying {arg1} ( ๑‾̀◡‾́)σ»', color=discord.Color.blue())
                embed.set_image(url=enlace_aleatorio)
                embed.timestamp = datetime.datetime.now()
                await ctx.send(embed=embed)
            else:
                emoji_id = 1231279253581205554 
                emoji = bot.get_emoji(emoji_id)
                if emoji is not None:
                    await ctx.reply(f'You have to tag someone to do that {emoji}')
                else:
                    await ctx.reply('You have to tag someone to do that')

        @bot.command()
        async def confused(ctx):
            author = ctx.author.id
            message = f'<@{author}> is confused  ୧( ˵ ° ~ ° ˵ )୨'
                
            with open('fun/gif/confused.txt', 'r') as f:
                enlaces = [linea.strip() for linea in f]
                enlace_aleatorio = random.choice(enlaces)
            
            embed = discord.Embed(title="",description=message, color=discord.Color.blue())
            embed.set_image(url=enlace_aleatorio)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)

        @bot.command()
        async def happy(ctx):
            author = ctx.author.id
            message = f'<@{author}> is happy ٩(^ᗜ^ )و ´-'
                
            with open('fun/gif/happy.txt', 'r') as f:
                enlaces = [linea.strip() for linea in f]
                enlace_aleatorio = random.choice(enlaces)
            embed = discord.Embed(title="",description=message, color=discord.Color.blue())
            embed.set_image(url=enlace_aleatorio)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)

        @bot.command()
        async def hi(ctx, arg1=None):
            author = ctx.author.id
            if arg1==None:
                message=f'<@{author}> says hi!  ＼(＾▽＾)' 
            elif arg1=='<@1225963290358714482>':
                message= f'Hii! <@{author}>  o(≧∇≦o)'
            else:
                message=f'<@{author}> says hi to {arg1}! ٩(^ᴗ^)۶'
            
            with open('fun/gif/hi.txt', 'r') as f:
                enlaces = [linea.strip() for linea in f]
                enlace_aleatorio = random.choice(enlaces)
            embed = discord.Embed(title="",description=message, color=discord.Color.blue())
            embed.set_image(url=enlace_aleatorio)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)

        @bot.command()
        async def wordle(ctx, arg1=None):
            if str(arg1).lower()=='es':
                autor= ctx.author.id
                user= bot.get_user(autor)
                palabra=random.choice(words_es).lower()
                embed=discord.Embed(title='**WORDLE**', description='Adivina la palabra oculta en 5 intentos', color=discord.Color.blue())
                embed.set_thumbnail(url=(user.avatar.url))
                embed.add_field(name=':black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square:', value='')
                message = await ctx.send(embed=embed)
                def check(m):
                    return m.author == ctx.message.author and m.channel == ctx.message.channel
                gana=False
                intento=0
            
                for i in range(5):
                    try:
                        intento+=1
                        word = await bot.wait_for('message', check=check, timeout=999)
                        word1= str(word.content).lower()
                        if len(word1)>5:
                            x=1+'pepe'
                        liste=[]
                        pos=0
                        goodpos=[]
                        mehpos=[]
                        for i in word1:
                            if i==palabra[pos]:
                                goodpos.append(pos)
                            elif i in palabra:
                                mehpos.append(pos)
                            pos+=1
                        
                        for i in range (5):
                            if i in goodpos:
                                liste.append(':green_square:')
                            elif i in mehpos:
                                liste.append(':yellow_square:')
                            else:
                                liste.append(':black_large_square:')
                        messag=''
                        for i in liste:
                            messag+=f'{i} '
                        messag=messag[:-1]
                        valu=''
                        numeros='abcdefghijklmnopqrstuvwxyz'
                        for i in word1:
                            if i in numeros:
                                valu+=f':regional_indicator_{i}: '
                            else:
                                valu+=':x: '
                        valu=valu[:-1]
                            
                        embed.add_field(name=f'Intento {intento}', value='', inline=False)
                        embed.add_field(name=messag, value=valu, inline=False)
                        await message.edit(embed=embed)
                    except:
                        embed.add_field(name=f'Intento {intento}', value='', inline=False)
                        embed.add_field(name=':black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square:', value=':x: :x: :x: :x: :x:', inline=False)
                        await message.edit(embed=embed)
                        await ctx.send('La palabra solo puede tener 5 caracteres')
                    if str(word1).lower()==palabra:
                        time.sleep(2)
                        gana=True
                        break
                        
                if gana==True:
                    embed=discord.Embed(title='**WORDLE**', description='', color=discord.Color.blue())
                    embed.add_field(name=f'**HAZ GANADO!!**', value=f'La palabra era **{palabra.upper()}**', inline=False)
                    embed.set_thumbnail(url=(user.avatar.url))
                    await message.edit(embed=embed)
                else:
                    embed=discord.Embed(title='**WORDLE**', description='', color=discord.Color.blue())
                    embed.add_field(name=f'**HAZ PERDIDO**', value=f'La palabra era **{palabra.upper()}**', inline=False)
                    embed.set_thumbnail(url=(user.avatar.url))
                    await message.edit(embed=embed)
            elif str(arg1)=='en':
                autor= ctx.author.id
                user= bot.get_user(autor)
                palabra=random.choice(words_en).lower()
                embed=discord.Embed(title='**WORDLE**', description='Guess the hidden word in 5 tries', color=discord.Color.blue())
                embed.set_thumbnail(url=(user.avatar.url))
                embed.add_field(name=':black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square:', value='')
                message = await ctx.send(embed=embed)
                def check(m):
                    return m.author == ctx.message.author and m.channel == ctx.message.channel
                gana=False
                intento=0
                

                for i in range(5):
                    try:
                        intento+=1
                        word = await bot.wait_for('message', check=check, timeout=999)
                        word1= str(word.content).lower()
                        if len(word1)>5:
                            x=1+'pepe'
                        liste=[]
                        pos=0
                        goodpos=[]
                        mehpos=[]
                        for i in word1:
                            if i==palabra[pos]:
                                goodpos.append(pos)
                            elif i in palabra:
                                mehpos.append(pos)
                            pos+=1
                        
                        for i in range (5):
                            if i in goodpos:
                                liste.append(':green_square:')
                            elif i in mehpos:
                                liste.append(':yellow_square:')
                            else:
                                liste.append(':black_large_square:')
                        messag=''
                        for i in liste:
                            messag+=f'{i} '
                        messag=messag[:-1]
                        valu=''
                        numeros='abcdefghijklmnopqrstuvwxyz'
                        for i in word1:
                            if i in numeros:
                                valu+=f':regional_indicator_{i}: '
                            else:
                                valu+=':x: '
                        valu=valu[:-1]
                            
                        embed.add_field(name=f'Attempt {intento}', value='', inline=False)
                        embed.add_field(name=messag, value=valu, inline=False)
                        await message.edit(embed=embed)
                    except:
                        embed.add_field(name=f'Attempt {intento}', value='', inline=False)
                        embed.add_field(name=':black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square:', value=':x: :x: :x: :x: :x:', inline=False)
                        await message.edit(embed=embed)
                        await ctx.send('The word must be 5 characters long')
                    if str(word1).lower()==palabra:
                        time.sleep(2)
                        gana=True
                        break
                        
                if gana==True:
                    embed=discord.Embed(title='**WORDLE**', description='', color=discord.Color.blue())
                    embed.add_field(name=f'**YOU WON!!**', value=f'The word was: **{palabra.upper()}**', inline=False)
                    embed.set_thumbnail(url=(user.avatar.url))
                    await message.edit(embed=embed)
                else:
                    embed=discord.Embed(title='**WORDLE**', description='', color=discord.Color.blue())
                    embed.add_field(name=f'**YOU LOST**', value=f'The word was: **{palabra.upper()}**', inline=False)
                    embed.set_thumbnail(url=(user.avatar.url))
                    await message.edit(embed=embed)
            else:
                embed=discord.Embed(title='Wanna play wordle?', description='Try this:',color=discord.Color.blue() )
                embed.add_field(name='wordle es', value='Juega wordle con palabras en español', inline=False)
                embed.add_field(name='wordle en',value='Play wordle with english words')
                await ctx.send(embed=embed)
