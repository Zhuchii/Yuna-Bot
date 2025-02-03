import json
from discord.utils import MISSING
import requests
import random
import discord
import asyncio
import datetime
from discord import app_commands, ui
import time
from discord.ext import commands
import sqlite3
import os

def conection(guild):
    return sqlite3.connect(f'database/{guild}.db')

class setwmodal(discord.ui.Modal, title="Customize the welcome message"):
    def __init__(self, guild):
        self.guild = guild
        super().__init__(title="Customize the welcome message")
        self.titlesd = discord.ui.TextInput(label='Title', placeholder='Title of the message here', style=discord.TextStyle.short, required=False)
        self.content = discord.ui.TextInput(label='Content', placeholder='Content of the message here', style=discord.TextStyle.long, required=False)
        self.image = discord.ui.TextInput(label='Image', placeholder='URL to the image here', style=discord.TextStyle.short, required=False)
        self.channel = discord.ui.TextInput(label='Channel ID or URL', placeholder='Use command "help setup" for more information', style=discord.TextStyle.short, required=False)
        self.add_item(self.titlesd)
        self.add_item(self.content)
        self.add_item(self.image)
        self.add_item(self.channel)

    async def on_submit(self, interaction: discord.Interaction):
        conect = conection(self.guild)
        cursor = conect.cursor()
        cursor.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='welcome_msg' ''')
        if cursor.fetchone()[0] == 0:
            cursor.execute('''
                CREATE TABLE welcome_msg (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    content TEXT,
                    image TEXT,
                    channel TEXT
                )
            ''')
            print('Se ha creado la tabla welcome_msg.')

        cursor.execute('SELECT COUNT(*) FROM welcome_msg')
        if cursor.fetchone()[0] == 0:
            cursor.execute('INSERT INTO welcome_msg (title, content, image, channel) VALUES (?, ?, ?, ?)', ("", "", "", ""))

        title_value = self.titlesd.value or ""
        content_value = self.content.value or ""
        image_value = self.image.value or ""
        channel_value=self.channel.value or ""
        if title_value!='':
            print('pepe')
            conect.commit()
            cursor.execute("UPDATE welcome_msg SET title = ? WHERE id = 1", (title_value,))
        if content_value!='':
            print('pepe')
            conect.commit()
            cursor.execute("UPDATE welcome_msg SET content = ? WHERE id = 1", (content_value,))
        if image_value!='':
            print('pepe')
            conect.commit()
            cursor.execute("UPDATE welcome_msg SET image = ? WHERE id = 1", (image_value,))
        if channel_value!='':
            print('pepe')
            conect.commit()
            cursor.execute("UPDATE welcome_msg SET channel = ? WHERE id = 1", (channel_value,))
        conect.commit()
        conect.close()
        await interaction.response.send_message("Welcome message updated!", ephemeral=True)


class confif(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        class SelectView(discord.ui.View):
            def __init__(self, guild, message):
                super().__init__(timeout=None)
                self.guild = guild
                select = discord.ui.Select(
                    placeholder="Choose a command...",
                    options=[
                        discord.SelectOption(label="Welcome message", description="", value="welcome_msg"),
                    ]
                )
                select.callback = self.select_option_callback
                self.add_item(select)
            
            async def select_option_callback(self, interaction: discord.Interaction):
                selected_value = interaction.data['values'][0]
                print(selected_value)
                if selected_value=='welcome_msg':
                    await interaction.response.send_modal(setwmodal(self.guild))

        @bot.command(name='set', description='Set a configuration for some commands')
        async def set_command(ctx):
            guild = ctx.guild.id
            message = await ctx.send("What configuration you want to set?:")
            view = SelectView(guild, message)
            await message.edit(view=view)
        
        
