import discord
import os

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
  print('We have lift off {0.user} yay!'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('/hello'):
    await message.channel.send('Hello!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
    
  if message.content.startswith('/ping'):
    await message.channel.send('Pong!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("/hru"):
    await message.channel.send('I am good thank you!')



client.run(os.environ['TOKEN'])