import discord
import re

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.author.id == '184383426202173441':
            await client.send_message(message.channel, content = 'IS THAT THE REAL <@184383426202173441> ??')

        elif checkSam(message.content):
            await client.send_message(message.channel, content = '<@184383426202173441> hi Sam :)')

def checkSam(message):
  return re.search(r"\b" + re.escape('sam') + r"\b", message, re.IGNORECASE)

client = MyClient()
client.run('TOKEN')
