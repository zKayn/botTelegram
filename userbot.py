from telethon import TelegramClient, events
import asyncio
import threading
from flask import Flask

# --- Cấu hình Telegram ---
api_id = 24597367
api_hash = '97418f63c13d5575494f820bd3bef756'
session_name = 'session_name'  # Đảm bảo đã có file session_name.session trong repo

group_a_id = -1001935117991
group_b_id = -1002611744078

# --- Khởi tạo client ---
client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(chats=group_a_id))
async def forward_message(event):
    try:
        if event.photo:
            await client.send_file(group_b_id, file=event.photo, caption=event.text or "")
        elif event.text:
            await client.send_message(group_b_id, event.text)
        print("✅ Tin nhắn đã được chuyển tiếp.", flush=True)
    except Exception as e:
        print(f"❌ Lỗi: {e}", flush=True)

# --- Chạy Telethon bot ---
def run_telegram_bot():
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot(loop))

async def start_bot(loop):
    await client.connect()
    if not await client.is_user_authorized():
        print("❌ Chưa đăng nhập Telegram.", flush=True)
        return
    print("🤖 Bot Telegram đang chạy...", flush=True)
    await client.run_until_disconnected()

# --- Flask giữ cho app luôn 'alive' ---
app = Flask(__name__)

@app.route('/')
def index():
    return "✅ Userbot is running on Render!"

# --- Khởi động cả bot và web ---
if __name__ == "__main__":
    threading.Thread(target=run_telegram_bot).start()
    app.run(host="0.0.0.0", port=10000)
