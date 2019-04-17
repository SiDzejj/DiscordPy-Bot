from discord.ext import commands
import random
import settings
import time


class CoinFlip:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def flipacoin(self, ctx):
        flip = [0, 1]
        result = random.choice(flip)
        await self.bot.say(settings.coin_flip)
        time.sleep(1.5)
        if result == 0:
            await self.bot.say('Heads')
        else:
            await self.bot.say('Tails')


def setup(bot):
    bot.add_cog(CoinFlip(bot))