import discord
from discord.ext import commands

import os
from dotenv import load_dotenv
import logging

# log file things
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

load_dotenv()

token = os.getenv('TOKEN')

bot = commands.Bot(command_prefix=',')

@bot.event
async def on_ready():
    print(f"Bot is logged in as {bot.user}")

@bot.command()
async def test(ctx):
    await ctx.send("Hello there")

bot.run(token)