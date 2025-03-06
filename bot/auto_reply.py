import random
from replies import flirty_replies
from voice_reply import text_to_speech
from meme_sender import send_meme

def auto_reply(message, sender):
    """
    Handles automatic replies based on the message received.
    """
    lower_msg = message.lower()
    
    if "meme" in lower_msg:
        return send_meme()
    
    # Generate a flirty response
    reply = random.choice(flirty_replies)
    
    # Convert text to voice in Hindi
    voice_reply = text_to_speech(reply, lang='hi')
    
    return {"text": reply, "voice": voice_reply}

if __name__ == "__main__":
    test_message = "Hey baby, send me something special!"
    response = auto_reply(test_message, "User")
    print("Text Reply:", response["text"])
    print("Voice Reply:", response["voice"])
