from discord.ext import commands


class AddAFK:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def afkadd(self, ctx):
        name = 'Andrzej'
        afk_time = '13sek'
        afkuser = [[name, afk_time]]
        print(afkuser['name'])



def setup(bot):
    bot.add_cog(AddAFK(bot))