from telethon.sync import TelegramClient

api_id = 24597367
api_hash = '97418f63c13d5575494f820bd3bef756'

with TelegramClient('session_name', api_id, api_hash) as client:
    for dialog in client.iter_dialogs():
        if dialog.is_group or dialog.is_channel:
            print(f"{dialog.name}: {dialog.id}")
