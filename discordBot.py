import discord
from discord import app_commands
from discord import abc


import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")

intents = discord.Intents.default()
# intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name='sync', description='Owner only', guild=discord.Object(id=751171768026267797))
async def sync(interaction: discord.Interaction):
    if interaction.user.id == 528722055810514944:
        await tree.sync()
        print('Command tree synced.')
        await interaction.response.send_message("synced", delete_after=1)
    else:
        await interaction.response.send_message('You must be the owner to use this command!')

@tree.command(name = "echo", description = "echo-ish command")
async def first_command(interaction, channel: abc.GuildChannel, args: str):
    await channel.send(args)
    await interaction.response.send_message("sent", delete_after=1)

@client.event
async def on_ready():
    # await tree.sync(guild=751171768026267797)
    await tree.sync(guild=discord.Object(id=751171768026267797)) # syncs sync command to my server
    print(f'We have logged in as {client.user}')

client.run(token)