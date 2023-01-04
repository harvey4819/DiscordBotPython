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
  
#Help command
@client.command(name='Help List', description='Provides a list of commands that you can use with MrBotty')
async def helplist(ctx):
  commands_names = ['/hi - MrBotty will say Hello',
                   '/cflip - MrBotty will flip a coin',
                   '/about - MrBotty will provide information about himself',
                   '/link - MrBotty will send a link to the GitHub repository']
  for each_item in commands_names:
    await ctx.send(each_item)
  
#Hi command
@client.command(name="Hi", description="Bot will reply with hello whilst mentioning the author of the message")
async def hi(ctx):
  await ctx.send('Hello, ' + ctx.message.author.mention)

#Coin flip command
@client.command(name='CFlip (CoinFlip)', description="Bot will flip a coin and output the result")
async def cflip(ctx):
  response = ['heads', 'tails']
  await ctx.send(ctx.message.author.mention + f' you got {random.choice(response)}!')

#About command
@client.command(name='About', description='Provides information about the bot')
async def about(ctx):
  await ctx.send('MrBotty is a Discord chat bot created in 2023, the link to the repository can be found by using the command /rlink')

#GitHub repository link command
@client.command(name='Link', description='Provides a link to the GitHub repository of this Discord bot.')
async def link(ctx):
  await ctx.send('The repository can be found here: https://github.com/harvey4819/DiscordBotPython.git')

#COMMANDS END

client.run(os.environ['TOKEN1'])