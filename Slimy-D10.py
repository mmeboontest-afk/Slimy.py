import discord
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# ใช้ Token จาก Environment Variable ที่เราจะตั้งใน Koyeb
token = os.getenv('BOT_TOKEN')
client.run(token)
