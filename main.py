#import discord package
import discord
from webserver import keep_alive
import os

#client (our bot)
intents = discord.Intents.all()
client = discord.Client(intents=intents)
#client = discord.Client()
#----------------------------------------------------------
#features to be added:
#output random statements
#make the bot have a personality
#a dictionary: send link to word
#----------------------------------------------------------
#@client.event
#async def on_ready():
# DO STUFF...
#general_channel = client.get_channel(841365211944714324)
#wait to find the channel, then send a message when the bot comes online
#await general_channel.send("Carrota hath cometh aliveth!!")


@client.event
async def on_member_join(member):
	await member.send(file=discord.File('welcome.jpg'))


@client.event
async def on_message(message):
	username = str(message.author).split('#')[0]

	#i think this is to prevent the bot from replying to itself
	if message.author == client.user:
		return

	if message.content.startswith('hello') or message.content.startswith('Hello'):
		await message.channel.send(f'Hello {username}!')

	#Dictionary
	#word = ''
	#if message.content.startwith == '$meaning' + word:
	#  await message.channel.send('https://www.urbandictionary.com/define.php?term=' + word)

#ping pong
	if message.content == 'ping' or message.content == 'Ping':
		await message.channel.send('pong')

#meow
	if message.content == 'meow' or message.content == 'Meow':
		await message.channel.send('meoww')

	#Show list of commands
	if message.content == '$commands':
		await message.channel.send(
		 '```$info \n$thunder \n$selfdestruct \n$SOS \n$emotionalSupport \n$insomnia \n$fact```'
		)

	################### COMMANDS #########################
	if message.content == '$info':
		await message.channel.send(
		 "My name is Carrota version 1.0 and I am a bot <3\nI shall only ever obey minojuno and noone else >:)"
		)
	#send attatchment
	if message.content == '$thunder':
		await message.channel.send(file=discord.File('zenitsu.gif'))

#emotional support
	if message.content == '$emotionalSupport':
		await message.channel.send(
		 'Carrota wants you to know that everything will be ok. Just pretend like nothing is on fire right now.'
		)

#insomnia
	if message.content == '$insomnia':
		await message.channel.send(
		 'pff who needs sleep anyway, what a waste of time .-.')

#fact of the day
	if message.content == '$fact':
		await message.channel.send(
		 "```Fact of the day: You're doing great! Keep up the good work!```")

#selfdestruct
	if message.content == '$selfdestruct':
		await message.channel.send(
		 'Warning: This action is destructive and cannot be reversed. **Confirm** self-destruct, or **Cancel**'
		)

		def check(msg):
			return msg.author == message.author and msg.channel == message.channel and \
   msg.content.lower() in ["confirm", "cancel"]

		#wait for user input
		msg = await client.wait_for("message", check=check)
		if msg.content.lower() == "confirm":
			await message.channel.send("Thats funnyyy >:) Do you think I'm dumb?")

			def check(msg):
				return msg.author == message.author and msg.channel == message.channel and \
    msg.content.lower() in ["yes", "no"]

			#wait for user input again
			msg2 = await client.wait_for("message", check=check)
			if msg2.content.lower() == "yes":
				await message.channel.send("No u <3")
			else:
				await message.channel.send("awh thanks!")
		elif msg.content.lower() == "cancel":
			await message.channel.send("Self-destruct cancelled")

#SOS
	if message.content.lower() == '$sos':
		await message.channel.send(
		 "Yikess. There's a rope that can save you! **Climb** it or **Perish**!")

		# This will make sure that the response will only be registered if the following
		# conditions are met:
		def check(msg):
			return msg.author == message.author and msg.channel == message.channel and \
   msg.content.lower() in ["climb", "perish"]

		#wait for user input
		msg = await client.wait_for("message", check=check)
		if msg.content.lower() == "climb":
			await message.channel.send(file=discord.File('laugh.gif'))
			await message.channel.send(
			 "HAHA *SNIP* I cut the rope now you're dead too :3")
		elif msg.content.lower() == "perish":
			await message.channel.send(file=discord.File('laugh.gif'))
			await message.channel.send("RIP :3")

	#################### message contains #####################
	if 'this is so sad' in message.content or 'This is so sad' in message.content or 'sad' in message.content or 'Sad' in message.content:
		await message.channel.send('https://www.youtube.com/watch?v=kJQP7kiw5Fk')

	if 'simp' in message.content or 'Simp' in message.content or 'SIMP' in message.content:
		await message.channel.send(
		 '```A friendly reminder to limit the simping. It is not healthy :3```')

	if 'food' in message.content or 'Food' in message.content or 'FOOD' in message.content:
		await message.channel.send(file=discord.File('delicious.jpg'))


#Run the client on the server
keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
