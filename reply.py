# internal version 1.0.1
# bot contributers -  naor2013, stealthyexpert, neonerz, gentlegiantjgc

# required python imports
import json
import time
import discord
from secrets import choice

# user response times cache
users_answered_times = {}

# load json data and return it either all the data or just the key.
def loadJson(json_filename, json_key):
	with open(json_filename) as json_file:

		if json_key != None:
			json_datas = json.load(json_file)
			json_data = json.loads(json_datas)
			return json_data[str(json_key)]

		json_datas = json.load(json_file)
		json_data = json.loads(json_datas)
		return json_data

# client class where all the main code in running.
class MyClient(discord.Client):
	async def on_message(self, message):

		# Get the blacklisted roles list  from the blacklisted_roles.json.
		blacklisted_roles = loadJson("blacklisted_roles.json", "blacklisted_roles")

		# Get the blacklisted channels list from the blacklisted_channels.json.
		blacklisted_channels = loadJson("blacklisted_channels.json", "blacklisted_channels")

		answers = loadJson("answers", None)
		questions = answers.keys()

		# Loop through questions and check if user's message includes it.
		for question in questions:
			if message.author != self.user and question.lower() in message.content.lower():

				# Blacklist any channels in the blacklisted_channels.json
				if message.channel.name not in blacklisted_channels:
					author_roles = list(map(str, message.author.roles))

					# Blacklist any roles in the blacklisted_roles.json
					for role in blacklisted_roles:
						if role in author_roles:
							return

					# If the user was replied to more than 1 day ago, let the bot talk. 
					if time.time() - users_answered_times.get(message.author, 0) > 24*3600:   
						faq_channel = [ch for ch in message.guild.channels if ch.name == "faq"][0].mention
						await message.channel.send(choice(answers.get(question)).format(faq=faq_channel))
						users_answered_times[message.author] = time.time()
#client code
client = MyClient()
client.run('XXXXXX')
