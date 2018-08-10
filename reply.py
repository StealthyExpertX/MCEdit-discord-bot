import discord
from secrets import choice

answers_for_1_13 = ["MCEdit currently does not support 1.13 versions. {faq}",
                    "Please refer to {faq} for more information before asking any questions.",
                    "we don't take kindly to 1.13 around these here parts.",
                    "MCEdit 1.13 support won't be coming for many many months so please be patient.",
                    "FYI - Java 1.13 is currently not supported.",
                    "We don't support 1.13 at the moment but we do support 1.8 through 1.12.2.",
                    "The development team only works on MCEdit in their free-time please be patient with 1.13 support as it will not be done for months.",
                    "MCEdit does not support 1.13 and won't be ready for many months.",
                    "We don't like when somebody mentions the 1.13 word so shh and keep quiet.",
                    "We don't have any release date currently for 1.13 but will certainly keep you posted when we do.",
                    "Hey, MCEdit 1.13 support is still a White Whale we are hunting just give us a few months and check back with us, maybe by then we will catch her with thee harpoon."
                    ]


class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author != self.user and "1.13" in message.content and message.channel.name != "dev":
            author_roles = list(map(str, message.author.roles))
            if "Filter Creator" in author_roles or "Smart People" in author_roles or "Developer" in author_roles:
                return
            faq_channel = [ch for ch in message.guild.channels if ch.name == "faq"][0].mention
            await message.channel.send(choice(answers_for_1_13).format(faq=faq_channel))


client = MyClient()
client.run('XXXXXX')
