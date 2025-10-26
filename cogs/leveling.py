import discord
from discord.ext import commands
from database import Database

class Leveling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = Database()

    @commands.command()
    async def rank(self, ctx):
        user = self.db.get_or_create_user(ctx.author.id, ctx.guild.id)
        await ctx.send(f'{ctx.author.mention}, your level is {user.level} with {user.xp} XP.')

    @commands.command()
    async def top10(self, ctx):
        users = self.db.get_top_users(ctx.guild.id, 10)
        leaderboard = '\n'.join([f'{i+1}. <@{user.user_id}> - Level {user.level} ({user.xp} XP)' for i, user in enumerate(users)])
        embed = discord.Embed(title='Top 10 Users', description=leaderboard)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Leveling(bot))
