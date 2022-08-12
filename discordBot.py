# just the import for the discord.py thing using the discord.ext.commands.Bot instead of discord.Client previously used
from discord.ext import commands

# stuff for .env
import os
from dotenv import load_dotenv

# log file module
import logging

# logs things to the discord.log file
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# loads the discord bot token from the .env file
load_dotenv()
token = os.getenv('TOKEN')

# command prefix
bot = commands.Bot(command_prefix=',')

# prints a message to the terminal when the bot connects
@bot.event
async def on_ready():
    print(f"Bot is logged in as {bot.user}")

# loads commands from a discord extension + cog (commandExtension.py)
bot.load_extension("commandExtension")

bot.run(token)