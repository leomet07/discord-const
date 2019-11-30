import sys
import os
import random

KEY = ""
channel_to_target = "lennys-bot"
#load key
with open("key.txt","r") as file:
	#read first line
	for line in file:
		KEY = line
		#print(line)
		break


import discord
print("Client is starting...")
client = discord.Client()
print('Client has started')



@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	print(message.content)

	messagechannel = message.channel.name
	print(messagechannel)

	other_than_trigger_word = message.content
	other_than_trigger_word = other_than_trigger_word.lower()
	
	messagelowered = other_than_trigger_word
	#print("LOWER" + other_than_trigger_word)
	other_than_trigger_word = other_than_trigger_word.split()
	del other_than_trigger_word[0]
	if messagechannel == channel_to_target:
		if messagelowered.startswith('$random'):

			#message contents do not matter since this is a random bot
			messagewithouttrigger = "".join(other_than_trigger_word)

			#getting the random value
			randomv  =random.randrange(0,100)

			#getting the positive or negative status from that
			status = "negative"
			if randomv >= 50:
				status = "positive"
			print(randomv)
			
			#configuring the channel to send the message to
			channel = message.channel

			#send the status the message channel
			await channel.send(status)
			texttosend = "Your percentage is: " + str(randomv) + "%"
			await channel.send(texttosend)

			#log what was sent
			with open("log.txt", "a") as file:
				file.write(str(messagewithouttrigger) + '\n')
		# print a separator
		print("-" * 50 )
		print("-" * 50 )
		#log any message in targeted channe;
		with open("allmessagelog.txt", "a") as file:
			file.write(str(message.content) + '\n')
	else:
		print("A message sent in another channel is detected")

	#to quit after first message
	

#client.run('NjAwMzIwODU1Nzg0MDMwMjQ5.XSyCdg.MJoLNUKyHvPb-adw5g9OHuWl3oM')
client.run(KEY)