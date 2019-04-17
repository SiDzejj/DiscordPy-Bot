import discord
import settings
from discord.ext import commands

client = commands.Bot(command_prefix="!")

client.load_extension('kick')
client.load_extension('hey')
client.load_extension('purge')
client.load_extension('ban')
client.load_extension('meme')
client.load_extension('memebase')
client.load_extension('flipacoin')
client.load_extension('voicemain')
client.load_extension('voicequeue')


@client.event
async def on_member_join(member):  # when someone join the server
    await client.send_message(member, settings.Welcome_message + member.name + settings.Welcome_message2)  # sending a direct welcome message
    await client.send_message(discord.Object(id=settings.main_channel_id), settings.Welcome_message + member.mention + ".")  # welcoming a new user publicly
    role = discord.utils.get(member.server.roles, name=settings.base_role_name)
    await client.add_roles(member, role)


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name=settings.name))  # setting up a "Playing" status
    print(discord.__version__, settings.name, settings.on_ready)  # printing a API version in console

if settings.login_type is True:
    client.run(settings.TOKEN)
else:
    client.run(settings.email, settings.password)
