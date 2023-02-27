import pyttsx3
import speech_recognition as sr
import pvporcupine
import struct
import pyaudio
from winotify import Notification,audio

from Mini_3 import wishMe


porcupine=None
paud=None
audio_stream=None

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voice', voices[2].id)
Assistant.setProperty('rate',170)


def speak(audio):
    print("  ")
    Assistant.say(audio)
    print("  ")
    print(f" : {audio}")

    Assistant.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing....")
            query = command.recognize_google(audio,language='en-in')
            print(f"You said : {query}")

        except Exception as Error:
            return "none"
        
        return query.lower()


def access():
    try:
        porcupine=pvporcupine.create(keywords=["bumblebee"]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)
            keyword_index=porcupine.process(keyword)
            if keyword_index>=0:
                from Mini_2 import start
                start()
                
                from Mini_4 import taskxe
                taskxe()

    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()








