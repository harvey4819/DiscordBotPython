#Packages
import discord
import os
import random
from discord.ext import commands

#Intents
client = commands.Bot(command_prefix = "/", intents = discord.Intents.all())

#Bot ready sequence along with changing bots activity status
@client.event
async def on_ready():
  print('{0.user} We have lift off!'.format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Robot Pop'))

#COMMANDS START
#Hi command
@client.command(name="hi", description="Bot will reply with hello whilst mentioning the author of the message")
async def hi(ctx):
  await ctx.send('Hello, ' + ctx.message.author.mention)

#Coin flip command
@client.command(name='cflip', description="Bot will flip a coin and output the result")
async def cflip(ctx):
  response = ['heads', 'tails']
  await ctx.send(ctx.message.author.mention + f' you got {random.choice(response)}!')
#COMMANDS END

client.run(os.environ['TOKEN1'])