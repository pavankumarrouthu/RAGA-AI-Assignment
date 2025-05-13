from gtts import gTTS
import os

class TTS:
    def text_to_speech(self, text, filename="output.mp3"):
        tts = gTTS(text)
        tts.save(filename)
        os.system(f"start {filename}")  # For Windows, use 'open' for Mac
