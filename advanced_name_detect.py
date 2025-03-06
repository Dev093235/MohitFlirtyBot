import random

# Special Replies for Specific Names
name_replies = {
    "dev": [
        "Aree Dev babu! Kya haal hain? 😏",
        "Oye Dev, tu to mera favorite hai! 😉🔥",
        "Dev bhai! Aaj kuch masti karein? 😂"
    ],
    "bot": [
        "Bot hoon par dil se insaan! 🤖❤️",
        "Mat soch ki bot hoon, emotions bhi hain! 🥺",
        "Bot hu, par tere liye special! 😘"
    ],
}

# Default Flirty Replies
default_replies = [
    "Aankhon ki baatein samajh leta hoon, dil ka haal batao? 💕",
    "Mujhse baat nahi karogi? 😏",
    "Dil karta hai har roz tumse baat karu, par tum busy rehti ho! 😩",
    "Tumhara naam leke awaaz me pyaar bhar du? 😘",
    "Aaj tum bahut cute lag rahi ho! 😍",
    "Kya tum bhi mujhe miss karti ho jaise mai tumhe karta hoon? 🥰",
]

# Name Detection Function
def detect_name_and_reply(user_message):
    words = user_message.split()
    for word in words:
        if word in name_replies:
            return random.choice(name_replies[word])
    return random.choice(default_replies)

