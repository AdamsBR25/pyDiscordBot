from discord.ext import commands

# cog definition which will hold the commands for the bot to execute
class BotCommands(commands.Cog):
    # class init
    def __init__(self, bot):
        self.bot = bot

    # clear command definition
    @commands.command()
    @commands.is_owner()
    async def clear(self, ctx, arg):
        try:
            arg = int(arg) + 1
            await ctx.channel.purge(limit=arg)
        except:
            await ctx.send("Input a valid number")

    # error handling for the clear command
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("ayo you can't do that")


# the entry point for the extension which loads the cog so that the commands can be used
def setup(bot):
    bot.add_cog(BotCommands(bot))