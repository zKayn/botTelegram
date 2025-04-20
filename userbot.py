import threading
import asyncio
from flask import Flask
from telethon import TelegramClient, events

api_id = 24597367
api_hash = '97418f63c13d5575494f820bd3bef756'
session_name = 'session_name'

group_a_id = -1001935117991   # Nhóm A
group_b_id = -1002611744078   # Nhóm B

client = TelegramClient(session_name, api_id, api_hash)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

@client.on(events.NewMessage(chats=group_a_id))
async def handle_msg(event):
    try:
        if event.photo:
            await client.send_file(group_b_id, file=event.photo, caption=event.text or "")
        elif event.text:
            await client.send_message(group_b_id, event.text)
        print("✅ Tin nhắn đã được chuyển tiếp.")
    except Exception as e:
        print(f"❌ Lỗi: {e}")

# ✅ Đây là cách chạy bot đúng trong thread phụ với asyncio
def run_telegram_bot():
    async def main():
        await client.start()
        print("🤖 Bot Telegram đang chạy...")
        await client.run_until_disconnected()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())

if __name__ == '__main__':
    threading.Thread(target=run_telegram_bot).start()
    app.run(host="0.0.0.0", port=10000)
