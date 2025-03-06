import pyttsx3

# Pyttsx3 Engine Setup
engine = pyttsx3.init()

# Voice Speed & Volume
engine.setProperty('rate', 160)  # Speed
engine.setProperty('volume', 1.0)  # Full Volume

# Function to Convert Text to Voice
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Testing (Remove later)
if __name__ == "__main__":
    speak("Hello bhai, tu mast hai! Ye voice reply system kaam kar raha hai.")
