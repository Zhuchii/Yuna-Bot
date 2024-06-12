import discord
import discord.context_managers
from discord.ext import commands
from discord.utils import get
import datetime
from pytube import *
from discord import app_commands



class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        @bot.command()
        async def ban(ctx, user: discord.Member, *args):
            reason = " ".join(args).lstrip()
            if isinstance(ctx.author, discord.Member) and ctx.author.guild_permissions.ban_members:
                try:
                    await user.ban(reason=reason)
                    embed = discord.Embed(title=f'{user.display_name} has been banned by {ctx.author.display_name}', description=f'**Reason:** {reason}', color=discord.Color.blue())
                    await ctx.send(embed=embed)
                except discord.Forbidden:
                    await ctx.send('I do not have sufficient permissions to ban this user.')
                except discord.HTTPException:
                    await ctx.send('An error occurred when trying to ban this user.')
            else:
                await ctx.send('You dont have permissions to ban this user')
                
        @bot.tree.command(
            name='ban',
            description='Ban a member from ur server'
        )
        async def bann(ctx: discord.Interaction, user: discord.Member, reason: str):
            if isinstance(ctx.user, discord.Member) and ctx.user.guild_permissions.ban_members:
                try:
                    await user.ban(reason=reason)
                    embed = discord.Embed(title =f'{user.display_name} has been banned by {ctx.user.display_name}', description= f'**Reason:** {reason}', color= discord.Color.blue())
                    await ctx.response.send_message(embed=embed)
                except discord.Forbidden:
                    await ctx.response.send_message('I do not have sufficient permissions to ban this user')
                except:
                    await ctx.response.send_message('An error occurred when trying to ban this user')
            else:
                await ctx.response.send_message('You dont have permissions to ban this user')

        @bot.command()
        async def kick(ctx, user: discord.Member, *args):
            reason = " ".join(args).lstrip()
            if isinstance(ctx.author, discord.Member) and ctx.author.guild_permissions.ban_members:
                try:
                    await user.kick(reason=reason)
                    embed = discord.Embed(title=f'{user.display_name} has been kicked by {ctx.author.display_name}', description=f'**Reason:** {reason}', color=discord.Color.blue())
                    await ctx.send(embed=embed)
                except discord.Forbidden:
                    await ctx.send('I do not have sufficient permissions to kick this user.')
                except discord.HTTPException:
                    await ctx.send('An error occurred when trying to kick this user.')
            else:
                await ctx.send('You dont have permissions to kick this user')
                
        @bot.tree.command(
            name='kick',
            description='Kick a member from ur server'
        )
        async def kik(ctx: discord.Interaction, user: discord.Member, reason: str):
            if isinstance(ctx.user, discord.Member) and ctx.user.guild_permissions.ban_members:
                try:
                    await user.kick(reason=reason)
                    embed = discord.Embed(title =f'{user.display_name} has been kicked by {ctx.user.display_name}', description= f'**Reason:** {reason}', color= discord.Color.blue())
                    await ctx.response.send_message(embed=embed)
                except discord.Forbidden:
                    await ctx.response.send_message('I do not have sufficient permissions to kick this user')
                except:
                    await ctx.response.send_message('An error occurred when trying to kick this user')
            else:
                await ctx.response.send_message('You dont have permissions to kick this user')
                
        @bot.command()
        async def timeout(ctx, user: discord.Member, minutes: int, *args):
            reason = " ".join(args).lstrip()
            if isinstance(ctx.author, discord.Member) and ctx.author.guild_permissions.ban_members:
                try:
                    end_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=minutes)
                    await user.edit(timed_out_until=end_time, reason=reason)
                    embed = discord.Embed(title =f'{user.display_name} has been timed out by {ctx.author.display_name}', description= f'**Reason:** {reason}\n**Time left:**<t:{int(end_time.timestamp())}:R>', color= discord.Color.blue())
                    await ctx.send(embed=embed)
                except discord.Forbidden:
                    await ctx.send('I do not have sufficient permissions to timeout this user.')
                except discord.HTTPException:
                    await ctx.send('An error occurred when trying to timeout this user.')
            else:
                await ctx.send('You dont have permissions to timeout this user')
                
        @bot.tree.command(
            name='timeout',
            description='Timeout a member for a specified time'
        )
        async def timeouc(ctx: discord.Interaction, user: discord.Member, minutes: int, reason: str):
            if isinstance(ctx.user, discord.Member) and ctx.user.guild_permissions.ban_members:
                try:
                    end_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=minutes)
                    await user.edit(timed_out_until=end_time, reason=reason)
                    embed = discord.Embed(title =f'{user.display_name} has been timed out by {ctx.user.display_name}', description= f'**Reason:** {reason}\n**Time left:**<t:{int(end_time.timestamp())}:R>', color= discord.Color.blue())
                    await ctx.response.send_message(embed=embed)
                except discord.Forbidden:
                    await ctx.response.send_message('I do not have sufficient permissions to timeout this user')
                except Exception as e:
                    await ctx.response.send_message('An error occurred when trying to timeout this user')
                    print(e)
            else:
                await ctx.response.send_message('You dont have permissions to timeout this user')
