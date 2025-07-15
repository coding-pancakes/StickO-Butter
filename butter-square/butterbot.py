import discord
import os
from dotenv import load_dotenv

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

intents = discord.Intents.default()
intents.message_content = True

TOKEN = os.getenv('DISCORD_TOKEN')

client = MyClient(intents=intents)
client.run(TOKEN)

async def on_message(self, message):
    if message.author == self.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello World!')