import random

# Possible replies when bot or dev is mentioned
replies = [
    "Arey! Tumne mujhe yaad kiya? 😏",
    "Bolo jaanu, tumhari kya khidmat karu? 😉",
    "Mujhe bula rahe ho? Tumhe to bas ek bahana chahiye 😜",
    "Dev ka naam mat lo, ab main tumhara hoon 😘",
    "Bot ho ya Dev, baat to pyaar ki honi chahiye 😍",
    "Bas naam hi liya, dil le gaye 💕",
    "Mujhe bula ke khud chup? Aisa zulm mat karo 😏",
    "Ek baar aur bulao, shayad pighal jau 🥰"
]

def detect_name_and_reply(message):
    # Convert message to lowercase for easy matching
    lower_message = message.lower()

    # If 'bot' or 'dev' is in the message, return a flirty reply
    if "bot" in lower_message or "dev" in lower_message:
        return random.choice(replies)
    
    return None  # No reply if name is not mentioned

# Example test (remove later in real implementation)
if __name__ == "__main__":
    test_message = "Oye bot, tu kaha hai?"
    print(detect_name_and_reply(test_message))
