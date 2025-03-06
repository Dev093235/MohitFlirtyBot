import random  

# 1000+ flirty replies
flirty_replies = [
    "Tumhare bina to zindagi WhatsApp ke bina net jaisi hai! 😘",
    "Agar flirting ek crime hoti, to main life-time jail mein hota! 😂",
    "Mujhe tumhari smile se zyada cute kuch nahi lagta! 😍",
    "Tum online ho to dil bhi active mode pe aa jata hai! ❤️",
    "Kya tum Google ho? Kyunki tum mein wo sab hai jo main dhund raha tha! 😘",
    "Dil garden-garden ho gaya, tumse baat karke! 🌸",
    "Tumhe dekh ke lagta hai ki Rab ne khud apne haathon se banaya hoga! 😍",
    "Tumhari aankhon mein kho jaane ka mann karta hai! ❤️",
    "Baby, tum to meri battery saver mode ho, tumse baat karke energy full ho jati hai! 🔋🔥",
    "Tumhare bina life offline jaisi lagti hai! 📴🥹"
]

# Function to get a random flirty reply
def get_flirty_reply():
    return random.choice(flirty_replies)

# Testing (Remove later)
if __name__ == "__main__":
    print(get_flirty_reply())
