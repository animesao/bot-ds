import discord
from discord.ext import commands
import json
from database import Database

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = Database()

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention} for: {reason}')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention} for: {reason}')

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, time=None):
        # Simplified mute, assuming a 'Muted' role exists
        muted_role = discord.utils.get(ctx.guild.roles, name='Muted')
        if muted_role:
            await member.add_roles(muted_role)
            await ctx.send(f'Muted {member.mention} for {time}')
        else:
            await ctx.send('Muted role not found.')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        self.db.add_warning(member.id, ctx.guild.id)
        user = self.db.get_or_create_user(member.id, ctx.guild.id)
        await ctx.send(f'Warned {member.mention} for: {reason}. Total warnings: {user.warnings}')
        settings = self.db.get_or_create_server_settings(ctx.guild.id)
        if user.warnings >= settings.auto_mute_warnings:
            await self.mute(ctx, member)

async def setup(bot):
    await bot.add_cog(Moderation(bot))
