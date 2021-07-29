#import discord package
import discord
from webserver import keep_alive
import os

#client (our bot)
client = discord.Client()

#@client.event
#async def on_ready():
    # DO STUFF...
    #general_channel = client.get_channel(841365211944714324)
    #wait to find the channel, then send a message when the bot comes online
    #await general_channel.send("Carrota hath cometh aliveth!!")

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
        '```$info \n$simp \n$thunder \n$technosimp \n$selfdestruct \n$SOS```'
      )

    ################### COMMANDS #########################
    if message.content == '$info':
      await message.channel.send(
          "My name is Carrota version 1.0 and I am a bot <3\nI shall only ever obey Minh and noone else >:)"
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
      await message.channel.send(file=discord.File('minhanh.jpeg'))
      await message.channel.send('```Technosimp identified and confirmed```')

    if message.content == '$selfdestruct':
      await message.channel.send('Thats funnyyy >:)')

    if message.content.lower() == '$sos':
      await message.channel.send("Yikess. There's a rope that can save you! **Climb** it or **Perish**!")
      # This will make sure that the response will only be registered if the following
      # conditions are met:
      def check(msg):
          return msg.author == message.author and msg.channel == message.channel and \
          msg.content.lower() in ["climb", "perish"]

      msg = await client.wait_for("message", check=check)
      if msg.content.lower() == "climb":
          await message.channel.send("HAHA *SNIP* I cut the rope now you're dead too :3")
      elif msg.content.lower() == "perish":
          await message.channel.send("RIP :3")

    #################### message contains #####################
    if 'this is so sad' in message.content or 'This is so sad' in message.content:
      await message.channel.send('https://music.youtube.com/watch?v=kJQP7kiw5Fk&list=RDAMVMkJQP7kiw5Fk')

    if 'simp' in message.content or 'Simp' in message.content or 'SIMP' in message.content:
      await message.channel.send('```A friendly reminder to limit the simping. It is not healthy :3```')

    if 'eat' in message.content or 'Eat' in message.content or 'EAT' in message.content:
      await message.channel.send(file=discord.File('delicious.jpg'))

    if 'giyu' in message.content or 'Giyu' in message.content or 'GIYU' in message.content or 'tomioka' in message.content or 'Tomioka' in message.content or 'TOMIOKA' in message.content:
      await message.channel.send(file=discord.File('tomioka.png'))
      await message.channel.send('Tapioca?')

#Run the client on the server (channel id: right click on channel)
keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
