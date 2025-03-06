import json
import random
import time
from fbchat import Client
from fbchat.models import Message, ThreadType
from replies import get_flirty_reply
from meme import get_random_meme
from voice_reply import generate_voice_reply
from advanced_name_detect import detect_name_and_reply

# Load Facebook Cookies
def load_cookies():
    with open("cookies.json", "r") as file:
        return json.load(file)

cookies = load_cookies()
client = Client("", "", session_cookies=cookies)

print(f"✅ Logged in as: {client.uid}")

# Auto-Reply Function
def auto_reply():
    while True:
        unread_messages = client.fetch_unread()
        for message in unread_messages:
            sender_id = message.author
            if sender_id != client.uid:  # Apne aap ko reply na kare
                user_message = message.text.lower()

                # Name Detect & Flirty Reply
                reply_text = detect_name_and_reply(user_message)
                if not reply_text:
                    reply_text = get_flirty_reply()

                # 30% Chance to Send a Meme
                if random.random() < 0.3:
                    meme_text = get_random_meme()
                    reply_text = f"{reply_text}\n\n🎭 {meme_text}"

                # 20% Chance to Send a Voice Reply
                if random.random() < 0.2:
                    voice_path = generate_voice_reply(reply_text)
                    client.sendLocalFiles(voice_path, thread_id=sender_id, thread_type=ThreadType.USER)
                else:
                    client.send(Message(text=reply_text), thread_id=sender_id, thread_type=ThreadType.USER)

                print(f"🔥 Replied to {sender_id}: {reply_text}")
        
        time.sleep(5)  # 5 sec wait kare next check ke liye

# Start Bot
if __name__ == "__main__":
    auto_reply()
