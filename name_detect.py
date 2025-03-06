import re
from replies import get_flirty_reply

# Function to Detect Name & Auto-Reply
def detect_name_and_reply(message, user_name="Baby"):
    words = message.lower().split()
    detected_name = None

    # List of names to detect
    special_names = ["mohit", "Bot", "babu", "baby", "jaan", "dev", "bot"]

    # Check if message contains a name
    for word in words:
        if word in special_names:
            detected_name = word
            break

    if detected_name:
        reply = f"{detected_name.capitalize()} 🤭, {get_flirty_reply()}"  # Name + Flirty Reply
    else:
        reply = get_flirty_reply()  # Normal Flirty Reply

    return reply

# Testing (Remove later)
if __name__ == "__main__":
    test_messages = [
        "Mohit tum kya kar rahe ho?",
        "bot tumhare bina maza nahi aata!",
        "Bot tu kya kar raha hai?",
        "Dev kaise ho bhai?",
        "Koi mujhe yaad nahi karta 😢"
    ]
    
    for msg in test_messages:
        print(f"Message: {msg}")
        print(f"Bot Reply: {detect_name_and_reply(msg)}\n")
