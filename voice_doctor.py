import os
from gtts import gTTS
import platform
import subprocess
from playsound import playsound

def text_to_speech_with_gtts(input_text,output_filepath):
     # Step 1: Check if file already exists
    if os.path.exists(output_filepath):
        try:
            os.remove(output_filepath)  # Step 2: Delete the file
        except Exception as e:
            print(f"Could not remove existing file: {e}")
            return None  # Return early if deletion fails
        
  #Convert text to speech
    language="en"

    audioobj=gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    print(f"[INFO] Audio saved to {output_filepath}")

    os_name=platform.system()
    try:
        if os_name=="Darwin": #macOS
            subprocess.run(['afplay',output_filepath])
        elif os_name == "Windows":  # Windows
            playsound(output_filepath)
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")    
    return output_filepath
# input_text="Hi"
# text_to_speech_with_gtts(input_text=input_text,output_filepath="gtts_testing_autoplay.mp3")        