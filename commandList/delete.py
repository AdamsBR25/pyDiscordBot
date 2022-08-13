from discord.ext import commands


# clear command definition
@commands.command()
@commands.is_owner()
async def delete(ctx, arg: int):
    try:
        arg = int(arg) + 1
        await ctx.channel.purge(limit=arg)
    except:
        await ctx.send("Input a valid number")

# error handling for the clear command
@delete.error
async def purge_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("ayo you can't do that")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please input a valid number")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please input a valid number")


# the entry point for the extension which loads the cog so that the commands can be used
def setup(bot):
    bot.add_command(delete)