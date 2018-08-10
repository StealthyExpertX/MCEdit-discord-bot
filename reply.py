import discord
from secrets import choice

TOKEN = 'XXXXX'
client = discord.Client()

answers_for_1_13 = ["MCEdit currently does not support 1.13 versions. {faq}",
                    "Please refer to {faq} for more information before asking any questions.",
                    "we don't take kindly to 1.13 around these here parts.",
                    "MCEdit 1.13 support won't be coming for many many months so please be patient.",
                    "FYI - Java 1.13 is currently not supported.",
                    ]


@client.event
async def on_message(message):
    if message.author != client.user and "1.13" in message.content and message.channel.name != "dev":
        author_roles = list(map(str, message.author.roles))
        if "Filter Creator" in author_roles or "Smart People" in author_roles or "Developer" in author_roles:
            return
        faq_channel = [ch for ch in message.server.channels if ch.name == "faq"][0].mention
        await client.send_message(message.channel, choice(answers_for_1_13).format(faq=faq_channel))


client.run(TOKEN)
