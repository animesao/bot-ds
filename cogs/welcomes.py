import discord
from discord.ext import commands
import json
from database import Database

class Welcomes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = Database()

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def set_welcome_channel(self, ctx, channel: discord.TextChannel):
        settings = self.db.get_or_create_server_settings(ctx.guild.id)
        settings.welcome_channel_id = channel.id
        session = self.db.get_session()
        session.commit()
        session.close()
        await ctx.send(f'Welcome channel set to {channel.mention}')

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def set_welcome_message(self, ctx, *, message):
        settings = self.db.get_or_create_server_settings(ctx.guild.id)
        settings.welcome_message = message
        session = self.db.get_session()
        session.commit()
        session.close()
        await ctx.send(f'Welcome message set to: {message}')

async def setup(bot):
    await bot.add_cog(Welcomes(bot))
