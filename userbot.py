from telethon import TelegramClient, events
import asyncio
import threading
from flask import Flask

# --- Thông tin cấu hình ---
api_id = 24597367
api_hash = '97418f63c13d5575494f820bd3bef756'
session_name = 'session_name'  # Đảm bảo file session_name.session đã được upload
group_a_id = -1001935117991
group_b_id = -1002611744078

# --- Khởi tạo Telethon client ---
client = TelegramClient(session_name, api_id, api_hash)

# --- Hàm xử lý tin nhắn ---
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

# --- Hàm chạy bot trong thread riêng ---
def run_telegram_bot():
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(client.start())
    print("🤖 Bot đang chạy...")
    client.run_until_disconnected()

# --- Flask Web Service để Render không kill app ---
app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Userbot đang chạy!"

# --- Chạy tất cả ---
if __name__ == "__main__":
    threading.Thread(target=run_telegram_bot).start()
    app.run(host="0.0.0.0", port=10000)
