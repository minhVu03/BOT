#import discord package
import discord
from webserver import keep_alive
import os

#client (our bot)
client = discord.Client()

@client.event
async def on_ready():
    # DO STUFF...
    general_channel = client.get_channel(841365211944714324)
    #wait to find the channel, then send a message when the bot comes online
    await general_channel.send("Carrota hath cometh aliveth!!")

@client.event
async def on_message(message):
    #i think this is to prevent the bot from replying to itself
    if message.author == client.user:
      return

    #if message starts with this
    if message.content.startswith('hello'):
      await message.channel.send('Hello!')

    #Show list of commands
    if message.content == '$commands':
      await message.channel.send(
        '```$info \n$simp \n$thunder \n$technosimp```'
      )

    ################### COMMANDS #########################
    if message.content == '$info':
      await message.channel.send(
          "My name is Carrota version 1.0 and I am a bot <3"
      )
    if message.content == '$simp':
      await message.channel.send(
          "https://i.pinimg.com/originals/e0/41/fa/e041fa5038a055ff62d51fdbcc15dbc9.jpg"
      )
    #send attatchment
    if message.content == '$thunder':
      await message.channel.send(file=discord.File('zenitsu.gif'))
      await message.channel.send('BOOM! Flash warning')

    if message.content == '$technosimp':
      await message.channel.send(file=discord.File('minhanh.PNG'))
      await message.channel.send('Technosimp confirmed')

    ################## message contains ###################
    if 'simp' in message.content:
      await message.channel.send('A friendly reminder to limit the simping. It is not healthy :3')

#Run the client on the server (channel id: right click on channel)
keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
