#Packages
import discord
import os
from discord.ext import commands

#Intents
client = commands.Bot(command_prefix = "/", intents = discord.Intents.all())

#Bot ready sequence along with changing bots activity status
@client.event
async def on_ready():
  print('{0.user} We have lift off!'.format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='bleep bloop bop'))

#Commands
@client.command()
async def hi(ctx):
  await ctx.send('Hello, ' + ctx.message.author.mention)

client.run(os.environ['TOKEN1'])