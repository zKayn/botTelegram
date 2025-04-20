import asyncio
from telethon import TelegramClient, events

# Thông tin Telegram
api_id = 24597367
api_hash = '97418f63c13d5575494f820bd3bef756'
session_name = 'session_name'  # Không có .session

# ID nhóm
group_a_id = -1001935117991   # Nhóm nguồn
group_b_id = -1002611744078   # Nhóm đích

# Khởi tạo client với session đã tồn tại
client = TelegramClient(session_name, api_id, api_hash)

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

# Chạy bot trong async
async def main():
    await client.start()
    print("🤖 Bot đang chạy...")
    await client.run_until_disconnected()

# Gọi hàm main
asyncio.run(main())
