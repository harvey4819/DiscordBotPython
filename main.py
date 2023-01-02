import discord
import os

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
  print('We have lift off {0.user} yay!'.format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="bleep bloop bop"))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('/hello'):
    await message.channel.send('Hello!')

client.run(os.environ['TOKEN'])