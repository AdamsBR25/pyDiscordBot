from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def say(self, ctx, channel, *, args):
        """Say a channel to send a specified message to"""

        id = channel.replace('<', "")
        id = id.replace('>', "")
        id = id.replace('#', "")
        destination = await self.bot.fetch_channel(int(id))
        await destination.send(args)

        await ctx.message.delete()
        # await ctx.channel.purge(limit=1)

    @say.error
    async def say_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("ayo you can't do that here")

def setup(bot):
    bot.add_cog(Say(bot))