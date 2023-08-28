from discord.ext import commands

@commands.command()
async def help(ctx):
    ctx.send("This is a placeholder for a future command list")

def setup(bot):
    bot.add_command(help)