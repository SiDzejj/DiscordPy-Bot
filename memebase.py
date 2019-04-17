from discord.ext import commands
import driveapi
import discord
import settings
import time
mp4_file = False

class Memebase:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def memebase(self, ctx):
        await self.bot.send_typing(discord.Object(id=settings.main_channel_id))
        driveapi.main()
        time.sleep(2)
        if mp4_file is False:
            await self.bot.send_file(discord.Object(id=settings.main_channel_id), 'discordfile.jpg')
        else:
            await self.bot.send_file(discord.Object(id=settings.main_channel_id), 'discordfile.mp4')


def setup(bot):
    bot.add_cog(Memebase(bot))
