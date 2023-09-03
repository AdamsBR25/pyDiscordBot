import discord
from discord import app_commands, abc

# .env for bot token
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("TOKEN")

# sets intents and creates the bot client
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# command tree for slash commands
tree = app_commands.CommandTree(client)

# server list
serv = discord.Object(id=751171768026267797)
bhssmp = discord.Object(id=796571893775859772)
guildlist = [serv, bhssmp]

# my account for commands sake
unclebeedy = 528722055810514944

# sends a message from the bot account
@tree.command(name = "echo", description = "echo-ish command", guilds=guildlist)
async def first_command(interaction, channel: abc.GuildChannel, message: str):
    await interaction.response.defer(ephemeral=True, thinking=True)
    if not interaction.user.id == unclebeedy:
        await interaction.followup.send("You do not have permission to use that command")
        return
    await channel.send(message)
    await interaction.followup.send(f"Sent '{message}' to {channel}")

# bulk delete command
@tree.command(name = "delete", description = "deletes a specified number of messages", guilds=guildlist)
async def delete(interaction, num: int):
    await interaction.response.defer(ephemeral=True, thinking=True)
    if not interaction.user.id == unclebeedy:
        await interaction.followup.send("You do not have permission to use that command")
        return
    await interaction.channel.purge(limit=num)
    await interaction.followup.send(f"Deleted {num} messages")

# @tree.command(name='sync', description='Owner only', guilds=guildlist)
# async def sync(interaction: discord.Interaction):
#     if interaction.user.id == 528722055810514944:
#         await tree.sync()
#         print('Command tree synced.')
#         await interaction.response.send_message("synced", delete_after=1)
#     else:
#         await interaction.response.send_message('You must be the owner to use this command!')

# syncs commands to any server in the list
async def sync_init():
    for guild in guildlist:
        await tree.sync(guild=guild)

# occurs once when the bot connects
@client.event
async def on_ready():
    # await tree.sync(guild=751171768026267797)
    # await tree.sync(guilds=guildlist) # syncs sync command to my server
    await sync_init()
    print(f'We have logged in as {client.user}')

# runs the bot
client.run(token)