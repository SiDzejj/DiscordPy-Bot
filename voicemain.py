from discord.ext import commands
import voicequeue
import settings


class VoiceMain:

    def __init__(self, bot):
        self.bot = bot

    connected = False
    playing = False
    players = {}


    @commands.command(pass_context=True)
    async def join(self, ctx):
        channel = ctx.message.author.voice.voice_channel
        if channel is None:
            await self.bot.say(ctx.message.author.mention + ' ' + settings.no_voice_msg)
        elif VoiceMain.connected is True:
            await self.bot.say(ctx.message.author.mention + ' ' + settings.already_connected)
        else:
            await self.bot.join_voice_channel(channel)
            VoiceMain.connected = True

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        server = ctx.message.server
        voice_client = self.bot.voice_client_in(server)
        if VoiceMain.connected is False:
            await self.bot.say(ctx.message.author.mention + ' ' + settings.already_disconnected)
        else:
            await voice_client.disconnect()
        VoiceMain.connected = False

    @commands.command(pass_context=True)
    async def play(self, ctx, url):
        server = ctx.message.server
        voice_client = self.bot.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url, after=lambda: voicequeue.check_queue(server.id))
        VoiceMain.players[server.id] = player
        VoiceMain.playing = True
        player.start()

    @commands.command(pass_context=True)
    async def pause(self, ctx):
            id = ctx.message.server.id
            if VoiceMain.playing is True:
                VoiceMain.players[id].pause()
            else:
                await self.bot.say(ctx.message.author.mention + ' ' + settings.not_playing)

    @commands.command(pass_context=True)
    async def resume(self, ctx):
            id = ctx.message.server.id
            if VoiceMain.playing is True:
                VoiceMain.players[id].resume()
            else:
                await self.bot.say(ctx.message.author.mention + ' ' + settings.not_playing)

    @commands.command(pass_context=True)
    async def skip(self, ctx):
            id = ctx.message.server.id
            if VoiceMain.playing is True:
                VoiceMain.players[id].stop()
            else:
                await self.bot.say(ctx.message.author.mention + ' ' + settings.not_playing)

def setup(bot):
    bot.add_cog(VoiceMain(bot))
