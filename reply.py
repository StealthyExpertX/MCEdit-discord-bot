# bot contributers -  naor2013, stealthyexpert, neonerz, gentlegiantjgc, BluCode

# required python imports
import json
import time
from random import choice
import re
import discord
from discord_token import token

# user response times cache
users_answered_times = {}

class MCEdit(discord.Client):
  def __init__(self, *args):
    super().__init__(*args)

    with open("blacklisted_roles.json") as f:
      self.blacklisted_roles = set(json.load(f)["blacklisted_roles"])
    with open("blacklisted_channels.json") as f:
      self.blacklisted_channels = set(json.load(f)["blacklisted_channels"])
    with open("answers.json") as f:
      answers = json.load(f)
    self.answers = {}
    for question, answer in answers.items():
      # 'questions' are space separated regular expressions which must
      # all match somewhere in a message to flag it
      compiled = tuple(re.compile(match) for match in question.split())
      self.answers[compiled] = answer

  async def on_message(self, message):
    if message.author == self.user:
      return
    if message.channel.name in self.blacklisted_channels:
      return
    for role in message.author.roles:
      if str(role) in self.blacklisted_roles:
        return
    # If the user was replied to less than 1 day ago, don't talk.
    #if time.time() - users_answered_times.get(message.author, 0) < 24*3600:
    #  return

    # Loop through questions and check if user's message includes it.
    for question in self.answers.keys():
      for match in question:
        res = match.search(message.content.lower())
        if not res:
          break
      else:
        channels = {ch.name: ch.mention for ch in message.guild.channels}
        reply = choice(self.answers.get(question))
        for name, mention in channels.items():
          reply = reply.replace("{" + name + "}", mention)
        await message.channel.send(reply)
        users_answered_times[message.author] = time.time()
        return

client = MCEdit()
client.run(token)
