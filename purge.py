from discord.ext import commands
import settings


class Purge:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def purge(self, ctx, amount=100):  # a chat cleaning command
        if ctx.message.channel.permissions_for(ctx.message.author).administrator is True:  # check if user has an administrator privellage
            channel = ctx.message.channel
            messages = []
            amount = amount + 1
            async for message in self.bot.logs_from(channel, limit=int(amount)):  # downloading messages
                messages.append(message)
            await self.bot.delete_messages(messages)  # deleting them
            amount = amount - 1
            await self.bot.say(settings.message_delete + str(amount) + settings.message_delete2)  # information about deleted messages
        else:
            await self.bot.say(settings.permission_error)  # return a permission error when not having an administrator


def setup(bot):
    bot.add_cog(Purge(bot))
