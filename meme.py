from discord.ext import commands
import os
import random
import discord
import settings


class Meme:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def meme(self, ctx):
        directory = 'memes/'
        file = random.choice(os.listdir(directory))
        await self.bot.send_file(discord.Object(id=settings.main_channel_id), directory + '/' + file)


def setup(bot):
    bot.add_cog(Meme(bot))
