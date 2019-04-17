from discord.ext import commands


class Hey:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def hey(self, ctx):
        await self.bot.say("What's up, " + ctx.message.author.mention + "?")


def setup(bot):
    bot.add_cog(Hey(bot))
