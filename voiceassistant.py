#page 2 of my code
#modules for code


from ctypes.wintypes import WORD
import datetime
from distutils.cmd import Command
from email import message_from_string
from imaplib import Commands
from pprint import pprint
from playsound import playsound
import pyttsx3
import speech_recognition as sr
import webbrowser 
import pywhatkit
import wikipedia
import os
import pyautogui
import keyboard
import pyjokes
import pydictionary as diction
from pywikihow import search_wikihow
from google_translator import Translator


Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voice', voices[2].id)
Assistant.setProperty('rate',170)

def screenshot():
        speak('ok boss ! What should i name the file...')
        path = takecommand()
        path1name = path + ".png"
        path1 = "C:/Users/91745/Pictures/Screenshots/" + path1name
        kk=pyautogui.screenshot()
        kk.save(path1)
        os.startfile('C:/Users/91745/Pictures/Screenshots')
        speak('Screenshot Done !')



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
            #print(f"You said : {query}")

        except Exception as Error:
            return "none"
        
        return query.lower()


def Trans():
    speak("Tell Me the line :")
    line=takecommand()
    translate =Translator()
    result = translate.translate(line)
    Text =result.text
    speak(f"It means that : "+Text)

while True:
    
        query = takecommand()
        #write queries..............:)
        if 'open translator' in query:
            Trans()
        


       