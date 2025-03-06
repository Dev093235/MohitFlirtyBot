import random

# Memes ka data (direct links ya local images)
memes = [
    "https://i.imgflip.com/4/30b1gx.jpg",  # Popular meme link
    "https://i.imgflip.com/4/1bij.jpg",
    "https://i.imgflip.com/4/aag.jpg",
    "https://i.imgflip.com/4/dq7.jpg",
    "https://i.imgflip.com/4/26am.jpg"
]

# Function to get a random meme
def get_meme():
    return random.choice(memes)

# Testing (Remove later)
if __name__ == "__main__":
    print(get_meme())
