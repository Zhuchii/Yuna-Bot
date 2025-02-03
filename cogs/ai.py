import json
import discord
from discord.ext import commands
from groq import Groq
import asyncio
import random
import requests
import os
import google.generativeai as genai

with open('config.json') as config_file:
    config = json.load(config_file)

genai.configure(api_key=config['gemini-ai-api'])


def load_sessions():
    try:
        with open('sessions.json', 'r') as file:
            data = file.read()
            if not data.strip():
                return {}  

            return json.loads(data)
    except (FileNotFoundError, json.JSONDecodeError):
        return {} 

def save_sessions(sessions):
    with open('sessions.json', 'w') as file:
        json.dump(sessions, file, indent=4)

user_sessions = load_sessions()

async def periodic_save(interval=300):
    while True:
        save_sessions(user_sessions)
        await asyncio.sleep(interval)

class ai(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @bot.event
        async def on_ready():
            self.bot.loop.create_task(periodic_save())

        @bot.event
        async def on_message(message):
            if message.author.bot:
                return
            if message.content[0]!='-':
                if self.bot.user in message.mentions or (message.reference and message.reference.resolved.author == self.bot.user):
                    user_id = int(message.author.id)
                    
                    
                    user_session = user_sessions['messages']
                    user = await bot.fetch_user(user_id)
                    user_input = message.content.replace(f'<@{self.bot.user.id}>', '').strip()

                    if not user_input:
                        return

                    
                    try:
                        async with message.channel.typing():
                            generation_config = {
                            "temperature": 1,
                            "top_p": 0.95,
                            "top_k": 64,
                            "max_output_tokens": 8192,
                            "response_mime_type": "text/plain",
                            }

                            model = genai.GenerativeModel(
                            model_name="gemini-1.5-pro",
                            generation_config=generation_config,
                            safety_settings = 'BLOCK_NONE',
                            
                            system_instruction=config['ai-prompt'])

                            chat_session = model.start_chat(
                            history=user_session
                            )

                            response = chat_session.send_message(f'{user}: {user_input}')

                            new_assist ={
                                "role": "model",
                                "parts": [
                                    response.text,
                                ],
                                }

                            new_message = {
                                "role": "user",
                                "parts": [
                                    f'{user}: {user_input}',
                                ],
                                }
                            
                            user_session.append(new_message)
                            user_session.append(new_assist)

                            await message.reply(response.text)
                            save_sessions(user_sessions)
                    except Exception as e:
                        print(f"An error occurred: {e}")
                        del user_session[1:15]


            await bot.process_commands(message)