import discord
import os
from flask import Flask
from threading import Thread

# ส่วนหลอกระบบ Koyeb (Health Check)
app = Flask('')
@app.route('/')
def home():
    return "I'm alive"

def run():
    app.run(host='0.0.0.0', port=8000)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ส่วนของบอท Discord
intents = discord.Intents.default()
intents.message_content = True 
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

keep_alive() # เริ่มรันเซิร์ฟเวอร์หลอก
token = os.getenv('MTQ1NzM2MDAyNzk2MTY1NTQyMA.G3abJT.31wJZJyc2HkKyOlSg_j2zg-MIhYfIjllpNzacs')
client.run(token)
