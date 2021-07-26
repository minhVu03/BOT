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
    if message.author == client.user:
        return

    #if message starts with this
    if message.content.startswith('hello') or message.content.startswith('$hi'):
        await message.channel.send('Hello!')

    #if the whole message is this
    if message.content == '$info':
        await message.channel.send(
            "My name is Carrota and I am a bot <3"
        )

#Run the client on the server (channel id: right click on channel)
keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
