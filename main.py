import discord
from discord.ext import commands
import json
import os
import random
from dotenv import load_dotenv
from database import Database
import logging

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Load config
with open('config.json', 'r') as f:
    config = json.load(f)

# Set up logging
logging.basicConfig(level=getattr(logging, config['logging']['level']), filename=config['logging']['file'], format='%(asctime)s - %(levelname)s - %(message)s')

# Intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Bot setup
bot = commands.Bot(command_prefix='!', intents=intents)
db = Database()

@bot.event
async def on_ready():
    logging.info(f'Bot is ready. Logged in as {bot.user}')
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # XP gain
    xp_gain = random.randint(*config['default_settings']['xp_per_message'])
    db.update_user_xp(message.author.id, message.guild.id, xp_gain)

    # Auto-moderation: banned words
    settings = db.get_or_create_server_settings(message.guild.id)
    banned_words = json.loads(settings.banned_words)
    if any(word in message.content.lower() for word in banned_words):
        await message.delete()
        await message.channel.send(f'{message.author.mention}, your message contained banned words!')
        db.add_warning(message.author.id, message.guild.id)
        if db.get_or_create_user(message.author.id, message.guild.id).warnings >= settings.auto_mute_warnings:
            # Mute logic (simplified)
            pass  # Implement mute

    # Spam detection (simplified)
    # This would need more complex logic for consecutive messages

    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    settings = db.get_or_create_server_settings(member.guild.id)
    if settings.welcome_channel_id:
        channel = bot.get_channel(settings.welcome_channel_id)
        if channel:
            message = settings.welcome_message.format(user=member.mention, server=member.guild.name)
            await channel.send(message)

# Load cogs
bot.load_extension('cogs.moderation')
bot.load_extension('cogs.welcomes')
bot.load_extension('cogs.leveling')

if __name__ == '__main__':
    bot.run(TOKEN)
