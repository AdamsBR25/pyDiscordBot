# just the import for the discord.py thing using the discord.ext.commands.Bot instead of discord.Client previously used
import discord
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

    game = discord.Game("bot under development")
    await bot.change_presence(activity=game)

# loads commands from a discord extension
bot.load_extension("commandList.delete")
# bot.load_extension("commandList.play")
bot.load_extension("commandList.Music")

# command that reloads the extensions without restarting the bot
@bot.command()
@commands.is_owner()
async def reload(ctx):
    bot.reload_extension("commandList.delete")
    # bot.reload_extension("commandList.play")
    bot.reload_extension("commandList.Music")

    await ctx.send("Reloaded all extensions")

# error handling for commands that don't exist
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found")

bot.run(token)