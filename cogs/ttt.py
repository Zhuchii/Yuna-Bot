import discord
import discord.context_managers
from discord.ext import commands
from discord.utils import get
import asyncio
import psycopg2
from colorama import init, Fore, Back, Style
import random
from collections import deque
from pytube import *
import yt_dlp
import re


        


class ttt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        class Buttons(discord.ui.View):
            def __init__(self, ctx, player1, message, player2 , bot, user_list, comienza) -> None:
                super().__init__(timeout=None)
                self.message = message
                self.ctx = ctx
                self.bot = bot
                self.player1=player1
                self.player2=int(player2)
                self.teclasx=[]
                self.teclaso=[]
                self.combinaciones = [
                    {'p1', 'p2', 'p3'},
                    {'p4', 'p5', 'p6'},
                    {'p7', 'p8', 'p9'},
                    {'p1', 'p4', 'p7'},
                    {'p2', 'p5', 'p8'},
                    {'p3', 'p6', 'p9'},
                    {'p1', 'p5', 'p9'},
                    {'p3', 'p5', 'p7'}
                ]
                self.user_list = user_list
                self.teclas=[]
                self.juga=True
                self.actual = self.user_list[comienza]
                self.done = False

            @discord.ui.button(label='‎', custom_id='1', row=0)
            async def p1(self, interacion: discord.Interaction, Button: discord.ui.Button):
                
                if interacion.user.id == self.actual: 
                    
                    if self.actual == self.user_list[0]:
                        self.actual = self.user_list[1]
                    elif self.actual == self.user_list[1]:
                        self.actual = self.user_list[0]
                        
                    if 'p1' not in self.teclaso and 'p1' not in self.teclasx:
                        if self.juga==True:
                            Button.label= 'X'
                            Button.style = discord.ButtonStyle.red
                            await interacion.response.edit_message(view=self)
                            self.teclasx.append('p1')
                            self.juga=False
                        else:
                            Button.label= 'O'
                            Button.style = discord.ButtonStyle.blurple
                            await interacion.response.edit_message(view=self)
                            self.teclaso.append('p1')
                            self.juga=True
                        self.teclas.append('p1')
                        
                    for combinacion in self.combinaciones:
                        if combinacion.issubset(self.teclasx):
                            user = bot.get_user(self.player1)
                            user2 = bot.get_user(self.player2)
                            embed = discord.Embed(title=f'**{user.global_name} WON!**', description=f'Opponent: **{user2.global_name}**')
                            embed.set_thumbnail(url=(user.avatar.url))
                            await self.ctx.send(embed=embed)
                            self.done = True
                            await self.message.delete()
                    for combinacion in self.combinaciones:
                        if combinacion.issubset(self.teclaso):
                            user = bot.get_user(self.player1)
                            user2 = bot.get_user(self.player2)
                            embed = discord.Embed(title=f'**{user2.global_name} WON!**',description=f'Opponent: **{user.global_name}**')
                            embed.set_thumbnail(url=(user2.avatar.url))
                            await self.ctx.send(embed=embed)
                            self.done = True
                            await self.message.delete()
                    if self.done==False and {'p1', 'p2', 'p3','p4','p5','p6','p7','p8','p9'}.issubset(self.teclas):
                        view = self.PlayAgainView(self.ctx,self.player1, self.message, self.player2, self.bot, self.user_list)
                        embed = discord.Embed(title=f'**DRAW**',description=f'Want to play again?')
                        await self.ctx.send(embed=embed, view=view)
                        await self.message.delete()
                    
                    
            @discord.ui.button(label='‎', custom_id='2', row=0)
            async def p2(self, interacion: discord.Interaction, Button: discord.ui.Button):

                if interacion.user.id == self.actual: 
                    
                    if self.actual == self.user_list[0]:
                        self.actual = self.user_list[1]
                    elif self.actual == self.user_list[1]:
                        self.actual = self.user_list[0]
                        
                    if 'p2' not in self.teclaso and 'p2' not in self.teclasx:
                        if self.juga==True:
                            Button.label= 'X'
                            Button.style = discord.ButtonStyle.red
                            await interacion.response.edit_message(view=self)
                            self.teclasx.append('p2')
                            self.juga=False
                        else:
                            Button.label= 'O'
                            Button.style = discord.ButtonStyle.blurple
                            await interacion.response.edit_message(view=self)
                            self.teclaso.append('p2')
                            self.juga=True
                        self.teclas.append('p2')
                    for combinacion in self.combinaciones:
                        if combinacion.issubset(self.teclasx):
                            user = bot.get_user(self.player1)
                            user2 = bot.get_user(self.player2)
                            embed = discord.Embed(title=f'**{user.global_name} WON!**', description=f'Opponent: **{user2.global_name}**')
                            embed.set_thumbnail(url=(user.avatar.url))
                            await self.ctx.send(embed=embed)
                            self.done = True
                            await self.message.delete()
                    for combinacion in self.combinaciones:
                        if combinacion.issubset(self.teclaso):
                            user = bot.get_user(self.player1)
                            user2 = bot.get_user(self.player2)
                            embed = discord.Embed(title=f'**{user2.global_name} WON!**',description=f'Opponent: **{user.global_name}**')
                            embed.set_thumbnail(url=(user2.avatar.url))
                            await self.ctx.send(embed=embed)
                            self.done = True
                            await self.message.delete()
                    if self.done==False and {'p1', 'p2', 'p3','p4','p5','p6','p7','p8','p9'}.issubset(self.teclas):
                        view = self.PlayAgainView(self.ctx,self.player1, self.message, self.player2, self.bot, self.user_list)
                        embed = discord.Embed(title=f'**DRAW**',description=f'Want to play again?')
                        await self.ctx.send(embed=embed, view=view)
                        await self.message.delete()
                    

                
            @discord.ui.button(label='‎', custom_id='3', row=0)
            async def p3(self, interacion: discord.Interaction, Button: discord.ui.Button):

                if interacion.user.id == self.actual: 
                    if self.actual == self.user_list[0]:
                        self.actual = self.user_list[1]
                    elif self.actual == self.user_list[1]:
                        self.actual = self.user_list[0]
                        
                    if 'p3' not in self.teclaso and 'p3' not in self.teclasx:
                        if self.juga==True:
                            Button.label= 'X'
                            Button.style = discord.ButtonStyle.red
                            await interacion.response.edit_message(view=self)
                            self.teclasx.append('p3')
                            self.juga=False
                        else:
                            Button.label= 'O'
                            Button.style = discord.ButtonStyle.blurple
                            await interacion.response.edit_message(view=self)
                            self.teclaso.append('p3')
                            self.juga=True
                        self.teclas.append('p3')
                    for combinacion in self.combinaciones:
                        if combinacion.issubset(self.teclasx):
                            user = bot.get_user(self.player1)
                            user2 = bot.get_user(self.player2)
                            embed = discord.Embed(title=f'**{user.global_name} WON!**', description=f'Opponent: **{user2.global_name}**')
                            embed.set_thumbnail(url=(user.avatar.url))
                            await self.ctx.send(embed=embed)
                            self.done = True
                            await self.message.delete()
                    for combinacion in self.combinaciones:
                        if combinacion.issubset(self.teclaso):
                            user = bot.get_user(self.player1)
                            user2 = bot.get_user(self.player2)
                            embed = discord.Embed(title=f'**{user2.global_name} WON!**',description=f'Opponent: **{user.global_name}**')
                            embed.set_thumbnail(url=(user2.avatar.url))
                            await self.ctx.send(embed=embed)
                            self.done = True
                            await self.message.delete()
                    if self.done==False and {'p1', 'p2', 'p3','p4','p5','p6','p7','p8','p9'}.issubset(self.teclas):
                        view = self.PlayAgainView(self.ctx,self.player1, self.message, self.player2, self.bot, self.user_list)
                        embed = discord.Embed(title=f'**DRAW**',description=f'Want to play again?')
                        await self.ctx.send(embed=embed, view=view)
                        await self.message.delete()
                        
                

            
            @discord.ui.button(label='‎', custom_id='4', row=1)
            async def p4(self, interacion: discord.Interaction, Button: discord.ui.Button):
                if interacion.user.id == self.actual: 
                    if self.actual == self.user_list[0]:
                        self.actual = self.user_list[1]
                    elif self.actual == self.user_list[1]:
                        self.actual = self.user_list[0]
                    if 'p4' not in self.teclaso and 'p4' not in self.teclasx:
                        if self.juga==True:
                            Button.label= 'X'
                            Button.style = discord.ButtonStyle.red
                            await interacion.response.edit_message(view=self)
                            self.teclasx.append('p4')
                            self.juga=False
                        else:
                            Button.label= 'O'
                            Button.style = discord.ButtonStyle.blurple
                            await interacion.response.edit_message(view=self)
                            self.teclaso.append('p4')
                            self.juga=True
                        self.teclas.append('p4')
                    for combinacion in self.combinaciones:
                        if combinacion.issubset(self.teclasx):
                            user = bot.get_user(self.player1)
                            user2 = bot.get_user(self.player2)
                            embed = discord.Embed(title=f'**{user.global_name} WON!**', description=f'Opponent: **{user2.global_name}**')
                            embed.set_thumbnail(url=(user.avatar.url))
                            await self.ctx.send(embed=embed)
                            self.done = True
                            await self.message.delete()
                    for combinacion in self.combinaciones:
                        if combinacion.issubset(self.teclaso):
                            user = bot.get_user(self.player1)
                            user2 = bot.get_user(self.player2)
                            embed = discord.Embed(title=f'**{user2.global_name} WON!**',description=f'Opponent: **{user.global_name}**')
                            embed.set_thumbnail(url=(user2.avatar.url))
                            await self.ctx.send(embed=embed)
                            self.done = True
                            await self.message.delete()
                    if self.done==False and {'p1', 'p2', 'p3','p4','p5','p6','p7','p8','p9'}.issubset(self.teclas):
                        view = self.PlayAgainView(self.ctx,self.player1, self.message, self.player2, self.bot, self.user_list)
                        embed = discord.Embed(title=f'**DRAW**',description=f'Want to play again?')
                        await self.ctx.send(embed=embed, view=view)
                        await self.message.delete()
                        
                

            
            @discord.ui.button(label='‎', custom_id='5', row=1)
            async def p5(self, interacion: discord.Interaction, Button: discord.ui.Button):
                if interacion.user.id == self.actual: 
                    if self.actual == self.user_list[0]:
                        self.actual = self.user_list[1]
                    elif self.actual == self.user_list[1]:
                        self.actual = self.user_list[0]
                    if 'p5' not in self.teclaso and 'p5' not in self.teclasx:
                        if self.juga==True:
                            Button.label= 'X'
                            Button.style = discord.ButtonStyle.red
                            await interacion.response.edit_message(view=self)
                            self.teclasx.append('p5')
                            self.juga=False
                        else:
                            Button.label= 'O'
                            Button.style = discord.ButtonStyle.blurple
                            await interacion.response.edit_message(view=self)
                            self.teclaso.append('p5')
                            self.juga=True
                        self.teclas.append('p5')
                    for combinacion in self.combinaciones:
                        if combinacion.issubset(self.teclasx):
                            user = bot.get_user(self.player1)
                            user2 = bot.get_user(self.player2)
                            embed = discord.Embed(title=f'**{user.global_name} WON!**', description=f'Opponent: **{user2.global_name}**')
                            embed.set_thumbnail(url=(user.avatar.url))
                            await self.ctx.send(embed=embed)
                            self.done = True
                            await self.message.delete()
                    for combinacion in self.combinaciones:
                        if combinacion.issubset(self.teclaso):
                            user = bot.get_user(self.player1)
                            user2 = bot.get_user(self.player2)
                            embed = discord.Embed(title=f'**{user2.global_name} WON!**',description=f'Opponent: **{user.global_name}**')
                            embed.set_thumbnail(url=(user2.avatar.url))
                            await self.ctx.send(embed=embed)
                            self.done = True
                            await self.message.delete()
                    if self.done==False and {'p1', 'p2', 'p3','p4','p5','p6','p7','p8','p9'}.issubset(self.teclas):
                        view = self.PlayAgainView(self.ctx,self.player1, self.message, self.player2, self.bot, self.user_list)
                        embed = discord.Embed(title=f'**DRAW**',description=f'Want to play again?')
                        await self.ctx.send(embed=embed, view=view)
                        await self.message.delete()
                        

            
            @discord.ui.button(label='‎', custom_id='6', row=1)
            async def p6(self, interacion: discord.Interaction, Button: discord.ui.Button):
                if interacion.user.id == self.actual: 
                    if self.actual == self.user_list[0]:
                        self.actual = self.user_list[1]
                    elif self.actual == self.user_list[1]:
                        self.actual = self.user_list[0]
                    if 'p6' not in self.teclaso and 'p6' not in self.teclasx:
                        if self.juga==True:
                            Button.label= 'X'
                            Button.style = discord.ButtonStyle.red
                            await interacion.response.edit_message(view=self)
                            self.teclasx.append('p6')
                            self.juga=False
                        else:
                            Button.label= 'O'
                            Button.style = discord.ButtonStyle.blurple
                            await interacion.response.edit_message(view=self)
                            self.teclaso.append('p6')
                            self.juga=True
                        self.teclas.append('p6')
                    for combinacion in self.combinaciones:
                        if combinacion.issubset(self.teclasx):
                            user = bot.get_user(self.player1)
                            user2 = bot.get_user(self.player2)
                            embed = discord.Embed(title=f'**{user.global_name} WON!**', description=f'Opponent: **{user2.global_name}**')
                            embed.set_thumbnail(url=(user.avatar.url))
                            await self.ctx.send(embed=embed)
                            self.done = True
                            await self.message.delete()
                    for combinacion in self.combinaciones:
                        if combinacion.issubset(self.teclaso):
                            user = bot.get_user(self.player1)
                            user2 = bot.get_user(self.player2)
                            embed = discord.Embed(title=f'**{user2.global_name} WON!**',description=f'Opponent: **{user.global_name}**')
                            embed.set_thumbnail(url=(user2.avatar.url))
                            await self.ctx.send(embed=embed)
                            self.done = True
                            await self.message.delete()
                    if self.done==False and {'p1', 'p2', 'p3','p4','p5','p6','p7','p8','p9'}.issubset(self.teclas):
                        view = self.PlayAgainView(self.ctx,self.player1, self.message, self.player2, self.bot, self.user_list)
                        embed = discord.Embed(title=f'**DRAW**',description=f'Want to play again?')
                        await self.ctx.send(embed=embed, view=view)
                        await self.message.delete()
                        

            
            @discord.ui.button(label='‎', custom_id='7', row=2)
            async def p7(self, interacion: discord.Interaction, Button: discord.ui.Button):
                if interacion.user.id == self.actual: 
                    if self.actual == self.user_list[0]:
                        self.actual = self.user_list[1]
                    elif self.actual == self.user_list[1]:
                        self.actual = self.user_list[0]
                    if 'p7' not in self.teclaso and 'p7' not in self.teclasx:
                        if self.juga==True:
                            Button.label= 'X'
                            Button.style = discord.ButtonStyle.red
                            await interacion.response.edit_message(view=self)
                            self.teclasx.append('p7')
                            self.juga=False
                        else:
                            Button.label= 'O'
                            Button.style = discord.ButtonStyle.blurple
                            await interacion.response.edit_message(view=self)
                            self.teclaso.append('p7')
                            self.juga=True
                        self.teclas.append('p7')
                    for combinacion in self.combinaciones:
                        if combinacion.issubset(self.teclasx):
                            user = bot.get_user(self.player1)
                            user2 = bot.get_user(self.player2)
                            embed = discord.Embed(title=f'**{user.global_name} WON!**', description=f'Opponent: **{user2.global_name}**')
                            embed.set_thumbnail(url=(user.avatar.url))
                            await self.ctx.send(embed=embed)
                            self.done = True
                            await self.message.delete()
                    for combinacion in self.combinaciones:
                        if combinacion.issubset(self.teclaso):
                            user = bot.get_user(self.player1)
                            user2 = bot.get_user(self.player2)
                            embed = discord.Embed(title=f'**{user2.global_name} WON!**',description=f'Opponent: **{user.global_name}**')
                            embed.set_thumbnail(url=(user2.avatar.url))
                            await self.ctx.send(embed=embed)
                            self.done = True
                            await self.message.delete()
                    if self.done==False and {'p1', 'p2', 'p3','p4','p5','p6','p7','p8','p9'}.issubset(self.teclas):
                        view = self.PlayAgainView(self.ctx,self.player1, self.message, self.player2, self.bot, self.user_list)
                        embed = discord.Embed(title=f'**DRAW**',description=f'Want to play again?')
                        await self.ctx.send(embed=embed, view=view)
                        await self.message.delete()
                        

            
            @discord.ui.button(label='‎', custom_id='8', row=2)
            async def p8(self, interacion: discord.Interaction, Button: discord.ui.Button):
                if interacion.user.id == self.actual: 
                    if self.actual == self.user_list[0]:
                        self.actual = self.user_list[1]
                    elif self.actual == self.user_list[1]:
                        self.actual = self.user_list[0]
                    if 'p8' not in self.teclaso and 'p8' not in self.teclasx:
                        if self.juga==True:
                            Button.label= 'X'
                            Button.style = discord.ButtonStyle.red
                            await interacion.response.edit_message(view=self)
                            self.teclasx.append('p8')
                            self.juga=False
                        else:
                            Button.label= 'O'
                            Button.style = discord.ButtonStyle.blurple
                            await interacion.response.edit_message(view=self)
                            self.teclaso.append('p8')
                            self.juga=True
                        self.teclas.append('p8')
                    for combinacion in self.combinaciones:
                        if combinacion.issubset(self.teclasx):
                            user = bot.get_user(self.player1)
                            user2 = bot.get_user(self.player2)
                            embed = discord.Embed(title=f'**{user.global_name} WON!**', description=f'Opponent: **{user2.global_name}**')
                            embed.set_thumbnail(url=(user.avatar.url))
                            await self.ctx.send(embed=embed)
                            self.done = True
                            await self.message.delete()
                    for combinacion in self.combinaciones:
                        if combinacion.issubset(self.teclaso):
                            user = bot.get_user(self.player1)
                            user2 = bot.get_user(self.player2)
                            embed = discord.Embed(title=f'**{user2.global_name} WON!**',description=f'Opponent: **{user.global_name}**')
                            embed.set_thumbnail(url=(user2.avatar.url))
                            await self.ctx.send(embed=embed)
                            self.done = True
                            await self.message.delete()
                    if self.done==False and {'p1', 'p2', 'p3','p4','p5','p6','p7','p8','p9'}.issubset(self.teclas):
                        view = self.PlayAgainView(self.ctx,self.player1, self.message, self.player2, self.bot, self.user_list)
                        embed = discord.Embed(title=f'**DRAW**',description=f'Want to play again?')
                        await self.ctx.send(embed=embed, view=view)
                        await self.message.delete()
                        
                        
            
            @discord.ui.button(label='‎', custom_id='9', row=2)
            async def p9(self, interacion: discord.Interaction, Button: discord.ui.Button):
                if interacion.user.id == self.actual:
                    if self.actual == self.user_list[0]:
                        self.actual = self.user_list[1]
                    elif self.actual == self.user_list[1]:
                        self.actual = self.user_list[0]
                    if 'p9' not in self.teclaso and 'p9' not in self.teclasx:
                        if self.juga==True:
                            Button.label= 'X'
                            Button.style = discord.ButtonStyle.red
                            await interacion.response.edit_message(view=self)
                            self.teclasx.append('p9')
                            self.juga=False
                        else:
                            Button.label= 'O'
                            Button.style = discord.ButtonStyle.blurple
                            await interacion.response.edit_message(view=self)
                            self.teclaso.append('p9')
                            self.juga=True
                        self.teclas.append('p9')
                    for combinacion in self.combinaciones:
                        if combinacion.issubset(self.teclasx):
                            user = bot.get_user(self.player1)
                            user2 = bot.get_user(self.player2)
                            embed = discord.Embed(title=f'**{user.global_name} WON!**', description=f'Opponent: **{user2.global_name}**')
                            embed.set_thumbnail(url=(user.avatar.url))
                            await self.ctx.send(embed=embed)
                            self.done = True
                            await self.message.delete()
                    for combinacion in self.combinaciones:
                        if combinacion.issubset(self.teclaso):
                            user = bot.get_user(self.player1)
                            user2 = bot.get_user(self.player2)
                            embed = discord.Embed(title=f'**{user2.global_name} WON!**',description=f'Opponent: **{user.global_name}**')
                            embed.set_thumbnail(url=(user2.avatar.url))
                            await self.ctx.send(embed=embed)
                            self.done = True
                            await self.message.delete()
                    if self.done==False and {'p1', 'p2', 'p3','p4','p5','p6','p7','p8','p9'}.issubset(self.teclas):
                        view = self.PlayAgainView(self.ctx,self.player1, self.message, self.player2, self.bot, self.user_list)
                        embed = discord.Embed(title=f'**DRAW**',description=f'Want to play again?')
                        await self.ctx.send(embed=embed, view=view)
                        await self.message.delete()
                        
                        
            class PlayAgainView(discord.ui.View):
                def __init__(self, ctx, player1, message, player2, bot, user_list):
                    super().__init__()
                    self.ctx = ctx
                    self.player1 = player1
                    self.player2 = int(player2)
                    self.message = message
                    self.bot = bot
                    self.user_list = user_list
                    self.press=False

                @discord.ui.button(label="Play Again", style=discord.ButtonStyle.green)
                async def play_again(self, interaction: discord.Interaction, button: discord.ui.Button):
                    if self.press==False:
                        self.press=True
                        try:
                            await self.message.delete()
                        except discord.errors.NotFound:
                            pass
                        comienza = random.randint(0,1)
                        message = await self.ctx.send(f"**TIC TAC TOE**\nStarts: <@{self.user_list[comienza]}>")
                        view = Buttons(self.ctx, self.player1, message, self.player2, self.bot, self.user_list, comienza)
                        await message.edit(view=view)
                        await interaction.message.delete()


        @bot.command()
        async def ttt(ctx, arg1=None):
            if arg1==None:
                await ctx.reply('You must to tag someone to do that')
            else:
                player2= (int((arg1)[:-1][2:]))
                player1 = ctx.author.id
                user_list = [player1, player2]
                comienza= random.randint(0,1)
                message = await ctx.send(f'**TIC TAC TOE**\nStarts: <@{user_list[comienza]}>')
                view = Buttons(ctx, player1, message, player2, bot, user_list, comienza)
                await message.edit(view=view)