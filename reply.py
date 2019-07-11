import time
import discord
from secrets import choice

answers = {

	"1.13": [
		"MCEdit does not support 1.13 you can read more about it in {faq}.",
		"Please refer to {faq} for more information before asking any questions about 1.13.",
		"we don't take kindly to 1.13 around these here parts. {faq}",
		"FYI - Java 1.13 is not supported by MCEdit see {faq} for more information.",
		"We do not support Java 1.13 but we do support 1.8 through 1.12.2 on MCEdit",
		"MCEdit does not support 1.13 but we are making Amulet which will support 1.13 and previous versions.",
		"The development team only works in their free-time so please be patient with us.,
		"MCEdit does not support Java 1.13 but we are working on a new editor called Amulet which will support 1.13+ on Java and past versions too!",
		"We don't like when somebody mentions the 1.13 word around here so shh and keep quiet and read. {faq}",
		"We don't have any release dates currently for 1.13 but will certainly keep you posted when we do.",
		"Hey, 1.13 support is a White Whale check back in a few months maybe by then we will catch her with thee harpoon."
	],

	"1.14":[
		"MCEdit does not support 1.14 you can read more about it in {faq}.",
		"Please refer to {faq} for more information before asking any questions about 1.14.",
		"we don't take kindly to 1.14 around these here parts. {faq}",
		"FYI - Java 1.14 is not supported by MCEdit see {faq} for more information.",
		"We do not support Java 1.14 but we do support 1.8 through 1.12.2 on MCEdit",
		"MCEdit does not support 1.14 but we are making Amulet which will support 1.14 and previous versions.",
		"The development team only works in their free-time so please be patient with us.,
		"MCEdit does not support Java 1.14 but we are working on a new editor called Amulet which will support 1.14+ on Java and past versions too!",
		"We don't like when somebody mentions the 1.14 word around here so shh and keep quiet and read. {faq}",
		"We don't have any release dates currently for 1.14 but will certainly keep you posted when we do.",
		"Hey, 1.14 support is a White Whale check back in a few months maybe by then we will catch her with thee harpoon."
	],

	"what is amulet" : [
		"Powerful-wizards such as Podshot are creating Amulet to support 1.13+ worlds on both Java and Bedrock platforms.",
		"Amulet is a new world editor that is being developed but if you would like to help contribute here is the GitHub link: https://github.com/Amulet-Team/Amulet-Map-Editor",
		"The new world editor Amulet will replace MCEdit and it's actively being worked and we expect a few months of work at least before its ready for an alpha-test.",
		"Amulet is a ground-up rewrite of a world editor for Minecraft to handle the new (and old) world formats for Java and Bedrock platforms.",
		"Amulet will be a new Minecraft world editor to handle 1.13 - 1.14+ worlds and all prior versions too but it's still being worked on so please be patient and see {amulet-dev} for updates on progress."
	],

	"thank you bot" : [
		"You got it.",
		"Don’t mention it.",
		"My pleasure.",
		"It was nothing.",
		"I'm happy to help.",
		"Anytime.",
		"It's my pleasure.",
		"I know you’d do the same for me.",
		"Live long and prosper.",
		"Anything for a fellow Minecrafter.",
		"Live long and prosper, fellow Minecrafter.",
		"The pleasure is mine.",
		"Absolutely.",
		"Definitely.",
		"No problemo.",
		"Don't sweat it.",
		"Sure thing.",
		"Glad to be of service.",
		"Awesomesauce.",
		":)",
		"No problem mate!",
		":smile:",
		":smiley:",
		":sunglasses:",
		":blush:",
		":wink:"
	]

}

# Store username and last bot reply timestamps in this dictionnary. 
users_answered_times = {}

#Questions of text for the bot to respond to note: an anwser list key must be added to the anwsers dictionary of the possible replies.
questions = [
	"1.13",
	"1.14",
	"what is amulet",
	"thank you bot"
]

#Blacklisted channels
blacklisted_channels = [
	"faq",
	"announcements",
	"server-log",
	"dev",
	"amulet-dev-private",
	"amulet-dev",
	"amulet-github-log",
	"amulet-discussion",
	"testing-release",
	"test-releases-linux",
	"bug-reports"
]

#Blacklisted roles
blacklisted_roles = [
	"Filter Creator",
	"Smart People",
	"Developer"
]

class MyClient(discord.Client):
	async def on_message(self, message):
		for question in questions:
			if message.author != self.user and question in message.content.lower():

				# Only respond in non-blacklisted channels.
				if message.channel.name not in blacklisted_channels:
					author_roles = list(map(str, message.author.roles))
					# Only respond to non-blacklisted roles.
					for role in blacklisted_roles:
						if role in author_roles:
							return

					# If the user was replied to more than 1 day ago, let the bot talk. 
					if time.time() - users_answered_times.get(message.author, 0) > 24*3600:   
						faq_channel = [ch for ch in message.guild.channels if ch.name == "faq"][0].mention
						await message.channel.send(choice(answers.get(question)).format(faq=faq_channel))
						users_answered_times[message.author] = time.time()

client = MyClient()
client.run('XXXXXX')
