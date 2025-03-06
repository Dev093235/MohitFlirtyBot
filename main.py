import os
import time
import random
from bot.fb_login import login_with_cookies
from bot.auto_reply import reply_to_messages
from bot.meme_sender import send_meme
from bot.voice_reply import send_voice_reply
from bot.utils import check_new_messages, get_user_name

# Load Facebook Cookies
FB_COOKIES = os.getenv("FB_COOKIES")
if not FB_COOKIES:
    print("[ERROR] Facebook cookies not found! Add them in GitHub Secrets or .env file.")
    exit(1)

# Initialize bot session
session = login_with_cookies(FB_COOKIES)
if not session:
    print("[ERROR] Login failed! Check your cookies.")
    exit(1)

print("[✅] Bot Successfully Logged in!")

# Bot Control Settings
BOT_ACTIVE = True  # Bot ko manually on/off karne ke liye
AUTO_MEME = True  # Agar memes bhejne hain to True rakho
AUTO_VOICE = True  # Agar voice reply chahiye to True rakho

while BOT_ACTIVE:
    print("[📩] Checking for new messages...")
    new_messages = check_new_messages(session)
    
    for msg in new_messages:
        user_id, message_text = msg["user_id"], msg["message"]
        user_name = get_user_name(session, user_id)
        
        print(f"[💬] Message from {user_name}: {message_text}")
        
        # Reply based on message type
        reply_text = reply_to_messages(message_text, user_name)
        session.send_message(user_id, reply_text)
        print(f"[✅] Replied: {reply_text}")
        
        # Send meme randomly
        if AUTO_MEME and random.choice([True, False]):
            meme_path = send_meme()
            session.send_image(user_id, meme_path)
            print("[🔥] Meme sent!")
        
        # Send voice reply randomly
        if AUTO_VOICE and random.choice([True, False]):
            voice_path = send_voice_reply(reply_text)
            session.send_audio(user_id, voice_path)
            print("[🎤] Voice reply sent!")
        
    print("[⏳] Waiting before next check...")
    time.sleep(10)  # Wait before checking again
