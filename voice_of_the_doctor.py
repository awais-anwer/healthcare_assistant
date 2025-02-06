import os
from gtts import gTTS
from playsound import playsound

def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"

    # Generate Speech
    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(output_filepath)
    # Play Sound (Cross-Platform) 
    playsound(output_filepath)

# Example Usage
# input_text = "Hello, this is Awais, a CS student."
# text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing.mp3")


