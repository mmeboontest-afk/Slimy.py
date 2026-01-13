import discord
import os
from flask import Flask
from threading import Thread

# ส่วนสร้างหน้าเว็บหลอกเพื่อผ่าน Health Check ของ Koyeb
app = Flask('')
@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ส่วนการทำงานของบอท Discord
intents = discord.Intents.default()
intents.message_content = True 
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'บอทออนไลน์แล้วในชื่อ: {client.user}')

keep_alive() # สั่งรันเว็บหลอก
token = os.getenv('BOT_TOKEN') # ดึง Token จากค่าที่เราจะตั้งใน Koyeb
client.run(token)
