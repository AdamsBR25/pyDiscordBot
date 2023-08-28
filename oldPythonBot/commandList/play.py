from discord.ext import commands
import discord

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vc = None

    @commands.command()
    async def play(self, ctx, *, url):
        channel = ctx.author.voice.channel
        if channel is not None:
            self.vc = await channel.connect()
            player = await self.vc.create_ytdl_player(url)
            player.start()
            

    
    @play.error
    async def play_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please input a youtube link")

    @commands.command()
    async def stop(self, ctx):
        if self.vc is not None:
            await self.vc.disconnect()
            self.vc = None
        elif self.vc is None:
            await ctx.send("Not currently playing anything")

def setup(bot):
    bot.add_cog(Music(bot))
