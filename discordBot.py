import discord
import os
from dotenv import load_dotenv

# commands folder to be used at a later date with a command handler
# import commands as commands

load_dotenv()

token = os.getenv('TOKEN')
client = discord.Client()


@client.event
async def on_ready():
    print("Bot logged in!")

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content).lower()
    channel = message.channel
    print(f"{username}: {user_message} ({str(channel.name)})")

    if message.author == client.user:
        return

    if user_message[0] != '.':
        return
    elif user_message[0] == '.':
        user_message = user_message.split('.')
        msg = user_message[1].split(' ')
        cmd = msg[0]
        args = msg[1:]

        if cmd == "hello":
            client.send_message(channel, "Hello there!")

        


client.run(token)