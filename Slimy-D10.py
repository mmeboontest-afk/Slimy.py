import discord
import os
from flask import Flask
from threading import Thread

# ส่วนที่ 1: สร้าง Server ปลอมเพื่อหลอก Koyeb (Health Check)
app = Flask('')

@app.route('/')
def home():
    return "Bot is Online!"

def run():
    app.run(host='0.0.0.0', port=8000)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ส่วนที่ 2: ตั้งค่าบอท Discord
intents = discord.Intents.default()
# หากบอทต้องอ่านข้อความ อย่าลืมเปิด Message Content Intent ใน Discord Developer Portal
intents.message_content = True 

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# รัน Server ปลอมก่อนรันบอท
keep_alive()

# ดึงรหัส Token จาก Environment Variable ที่ตั้งไว้ใน Koyeb
token = os.getenv('BOT_TOKEN')
client.run(token)

