# This file looks for new folders inside user uploads and converts them to reel if they are not already converted
import os
from text_to_audio import text_to_speech_file
import time

def text_to_audio(folder):
  with open (f"user_uploads/{folder}/desc.txt","r") as f:
    text = f.read()
    print(text,folder)
  # text_to_speech_file(text, folder)

def create_reel(folder):
  print("CR-",folder)

if __name__ == "__main__":
  while True:
    print("Processing queue...")
    with open("done.txt","r") as f:
      done_folders = [line.strip() for line in f]

    folders = os.listdir("user_uploads")

    for folder in folders:
      if(folder not in done_folders):
        text_to_audio(folder) # Generate the audio.mp3 from desc.txt
        create_reel(folder) # Convert the images and audio.mp3 from the folder to reel
        with open("done.txt","a") as f:
          f.write(folder + "\n")
    time.sleep(4) 