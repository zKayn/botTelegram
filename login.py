from telethon.sync import TelegramClient

api_id = 24597367  # Thay bằng của bạn
api_hash = '97418f63c13d5575494f820bd3bef756'

with TelegramClient('session_name', api_id, api_hash) as client:
    client.send_message('me', '✅ Đăng nhập thành công!')
