from discord.ext import commands
import settings
import youtube_dl
import voicemain

queues = {}


def check_queue(id):
    if queues[id] != []:
        player = queues[id].pop(0)
        voicemain.VoiceMain.players[id] = player
        player.start()


class VoiceQueue:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def queue(self, ctx, url):
        server = ctx.message.server
        voice_client = self.bot.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))

        if server.id in queues:
            queues[server.id].append(player)
        else:
            queues[server.id] = [player]
        await self.bot.say(ctx.message.author.mention + ' ' + settings.video_queue)


def setup(bot):
    bot.add_cog(VoiceQueue(bot))
