import discord
import discord.context_managers
from discord.ext import commands
from gradio_client import Client
import discord.gateway
from discord.utils import get
import datetime
from pytube import *
from discord import app_commands
import os
import random
import time
from PIL import Image, ImageDraw
import requests
from io import BytesIO
import asyncio
import json

estim = random.randint(30, 50)


def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)


def save_config(config):
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)


def create_banner_image(user, banner_size=(680, 240)):
    avatar_url = user.avatar.url
    response = requests.get(avatar_url)
    avatar_image = Image.open(BytesIO(response.content))

    width_percent = (banner_size[0] / float(avatar_image.size[0]))
    height_size = int((float(avatar_image.size[1]) * float(width_percent)))
    resized_avatar = avatar_image.resize((banner_size[0], height_size), Image.LANCZOS)

    if resized_avatar.size[1] > banner_size[1]:
        top_cut = (resized_avatar.size[1] - banner_size[1]) // 2
        resized_avatar = resized_avatar.crop((0, top_cut, banner_size[0], top_cut + banner_size[1]))

    banner_image = Image.new('RGB', banner_size, (255, 255, 255))
    position = ((banner_size[0] - resized_avatar.width) // 2, (banner_size[1] - resized_avatar.height) // 2)
    banner_image.paste(resized_avatar, position)
    byte_arr = BytesIO()
    banner_image.save(byte_arr, format='PNG')
    byte_arr.seek(0)

    return byte_arr


class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
        @bot.event
        async def on_command_error(ctx, error):
            if isinstance(error, commands.CommandOnCooldown):
                msg= '**Still on cooldown** >.<, please try again in {:.2f}s'. format(error.retry_after)
                await ctx.reply(msg)
        
        
        @bot.command()
        async def server_info(ctx):
            Tchannels = ctx.guild.text_channels
            Vchannels = ctx.guild.voice_channels
            users = 0
            bots = 0
            created_at = ctx.guild.created_at
            formatted_created_at = created_at.strftime("%Y-%m-%d %H:%M:%S")
            emojis=0
            roles=0
            try:
                for i in ctx.guild.roles:
                    roles+=1
            except:
                roles=0

            try:
                for i in ctx.guild.emojis:
                    emojis+=1
            except:
                emojis=0
                
            for i in ctx.guild.members:
                if i.bot == False:
                    users+=1
                elif i.bot == True:
                    bots+=1
            try:
                banner = ctx.guild.banner.url
            except:
                banner = ''
            try:
                icon = ctx.guild.icon.url
            except:
                icon = ''
            embed = discord.Embed(title=f'Server Info', description=f'', color=discord.Color.blue())
            embed.add_field(name='\nSome information about the server', value='\n', inline=False)
            embed.add_field(name='ID', value=ctx.guild.id,inline=False)
            embed.add_field(name='Owner', value=ctx.guild.owner, inline=False)
            embed.add_field(name=f'Members', value=f'`Users: {users}| Bots: {bots}`')
            embed.add_field(name=f'Channels', value=f'`Text: {len(Tchannels)} | Voice: {len(Vchannels)}`')
            embed.add_field(name=f'Boosted', value=f'`{ctx.guild.premium_subscription_count} times`')
            embed.add_field(name=f'', value=f'', inline=False)
            embed.add_field(name=f'Emojis ', value=f'`{emojis} ')
            embed.add_field(name=f'Roles ', value=f'`{roles} `')
            embed.add_field(name=f'Verification ', value=f'`{ctx.guild.verification_level} `')
            embed.add_field(name='Server Created On', value=f'`{formatted_created_at}`', inline=False)
            embed.set_image(url=f'{banner}')
            embed.set_thumbnail(url=f'{icon}')
            await ctx.send(embed=embed)
            
        @bot.command()
        async def user_info(ctx, arg1):
            user = arg1[2:][:-1]
            user = await bot.fetch_user(user)
            try:
                banner = user.banner.url
            except:
                banner = ''
                
            member = await ctx.guild.fetch_member(arg1[2:][:-1])
            account_created_at = member.created_at.strftime("%Y-%m-%d %H:%M:%S")
            account_created_since = discord.utils.format_dt(user.created_at, style='R')
            if member.joined_at:
                joined_at = member.joined_at.strftime("%Y-%m-%d %H:%M:%S")
                joined_since = discord.utils.format_dt(member.joined_at, style='R')
            else:
                joined_at = "N/A"
                joined_since = "N/A"

            embed = discord.Embed(title=f'User Info', description=f'', color=discord.Color.blue())
            embed.add_field(name='', value=f'**ID**: {user.id}', inline=False)
            embed.add_field(name='', value=f'**Username**: {user}', inline=False)
            embed.add_field(name='', value=f'**Color**: {user.accent_color}', inline=False)
            embed.add_field(name='Discord Membership', value=f'{account_created_at} [ {account_created_since} ]', inline=False)
            embed.add_field(name=f'{ctx.guild.name} server Membership', value=f'{joined_at} [ {joined_since} ]', inline=False)
            embed.set_thumbnail(url=f'{user.avatar.url}')
            if user.banner:
                embed.set_image(url=user.banner.url)
                await ctx.send(embed=embed)
            else:
                image = create_banner_image(user)
                file = discord.File(fp=image, filename='banner.png')
                embed.set_image(url='attachment://banner.png')
                await ctx.send(file=file, embed=embed)
                
        def upscale_image(image_bytes):
            image = Image.open(BytesIO(image_bytes))

            original_width, original_height = image.size

            new_size = (original_width * 2, original_height * 2)
            resized_image = image.resize(new_size, resample=Image.LANCZOS)
            byte_arr = BytesIO()
            resized_image.save(byte_arr, format='PNG')
            byte_arr.seek(0)

            return byte_arr

        @bot.command()
        @commands.cooldown(1,110, commands.BucketType.user)
        async def imagine(ctx, *args):
                return await ctx.reply ('Temporarily disabled. Will be fixed soon')
                id = ctx.author.id
                user = await bot.fetch_user(id)
                global estim
                prompt = " ".join(args).lstrip()
                seed = random.randint(1, 10000000000)
                start = time.time()
                men = await ctx.send(f'Generating... ETA: {round(estim, 1)} seconds\nSteps: 1/2')
                
                def get_image_url(prompt):
                    with open('config.json') as config_file:
                        config = json.load(config_file)

                    client = Client(config['hf_url'])
                    result = client.predict(
                    prompt=prompt,
                    negative_prompt="(deformed, distorted, disfigured:1.3), poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, (mutated hands and fingers:1.4), disconnected limbs, mutation, mutated, ugly, disgusting, blurry, amputation",
                    use_negative_prompt=True,
                    style="2560 x 1440",
                    collage_style="No Style",
                    filter_name="Zero filter",
                    grid_size="1x1",
                    seed=seed,
                    width=1024,
                    height=1024,
                    guidance_scale=6,
                    randomize_seed=True,
                    api_name="/run"
                    )
                    return result[0][0]['image']

                image_url = await asyncio.to_thread(get_image_url, prompt)
                
                await men.edit(content=f'Generating... ETA: {round(estim, 1)} seconds\nSteps: 2/2')


                filename = f'{random.randint(10000000,999999999)}.png'
                resultado = 'sssss'
                end = time.time()
                estim= end - start
                await men.edit(content=f'Generating... ETA: {round(estim, 1)} seconds\nSteps: done!')
                if resultado=='sexy' or resultado=='porn' or resultado=='hentai':
                    if ctx.channel.nsfw:
                        embed = discord.Embed(title='Image generated', description='', color=discord.Color.blue())
                        embed.add_field(name=f'Created by {user}:', value=prompt)
                        embed.add_field(name=f'Time taked to generate: {round(estim, 1)} seconds', value='', inline=False)
                        file = discord.File(image_url, filename=filename)
                        embed.set_image(url=f'attachment://{filename}')
                        embed.set_footer(text='Generated by Yuna AI')
                        await ctx.send(embed=embed, file=file)
                    else:
                        await ctx.reply(content='To generate **NSFW** images you must be on an nsfw channel first -_-')
                else:
                    embed = discord.Embed(title='Image generated', description='', color=discord.Color.blue())
                    embed.add_field(name=f'Created by {user}:', value=prompt)
                    embed.add_field(name=f'Time taked to generate: {round(estim, 1)} seconds', value='', inline=False)
                    file = discord.File(image_url, filename=filename)
                    embed.set_image(url=f'attachment://{filename}')
                    embed.set_footer(text='Generated by Yuna AI')
                    await ctx.send(embed=embed, file=file)
                await men.delete()
                os.remove(image_url)


        @bot.command()
        async def reload(ctx, new_url):
            config = load_config()
            config['hf_url'] = new_url
            save_config(config)
            await ctx.send(f"Se ha actualizado hf_url a: {new_url}")
                    