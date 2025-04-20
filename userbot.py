from flask import Flask
from telethon import TelegramClient, events
import threading
import os

# Khai báo API ID và API HASH từ môi trường
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_name = 'session_name'

group_a_id = -1001935117991   # Thay bằng nhóm A
group_b_id = -1002611744078   # Thay bằng nhóm B

client = TelegramClient(session_name, api_id, api_hash)

app = Flask(__name__)

# Khởi tạo route để Flask có thể chạy
@app.route('/')
def home():
    return 'Bot đang chạy...'

@client.on(events.NewMessage(chats=group_a_id))
async def handle_msg(event):
    try:
        if event.photo:
            await client.send_file(
                group_b_id,
                file=event.photo,
                caption=event.text or ""
            )
        elif event.text:
            await client.send_message(group_b_id, event.text)

        print("✅ Tin nhắn đã được chuyển tiếp.")
    except Exception as e:
        print(f"❌ Lỗi: {e}")

# Tạo một thread để chạy TelegramClient
def run_telegram_bot():
    client.start()
    print("🤖 Bot đang chạy...")
    client.run_until_disconnected()

# Chạy TelegramClient trong một thread riêng biệt
threading.Thread(target=run_telegram_bot).start()

# Chạy Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)  # Port này cần để Render nhận diện (có thể thay bằng port khác)
