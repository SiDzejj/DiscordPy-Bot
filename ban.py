from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
import discord
import settings


class Ban:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @has_permissions(manage_roles=True, kick_members=True)
    async def ban(self, ctx, member: discord.Member = None):
        await self.bot.send_message(discord.Object(id=settings.main_channel_id), member.name + settings.ban_message)
        await self.bot.ban(member)


def setup(bot):
    bot.add_cog(Ban(bot))