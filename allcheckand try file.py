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

def closeapps():
        speak("Wait a second !")
        if 'gold' in query:
            os.system("TASKKILL/?/in Code.exe")
        elif 'chrome' in query:
            os.system("TASKKILL/F/in chrome.exe")
        speak("Done Boss !")

def openapps():
    speak("Wait a second !")

    if 'vs code' in query:
        speak("Opening vs code...")
        os.startfile("C:/Users/91745/Desktop/Visual Studio Code.lnk")

    elif 'microsoft' in query:
        speak("opening Microsoft edge...")
        os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Edge.lnk")
    
    elif 'access' in query:
        speak('Opening Microsoft Access...')
        os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Access.lnk")
    
    elif 'excel' in query:
        speak('Opening Microsoft Excel...')
        os.startfile('"C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Excel.lnk"')

    elif 'one note' in query:
        speak("Opening Microsoft One note ...")
        os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/OneNote.lnk")

    elif 'outlook' in query:
        speak("Opening Microsoft Outlook...")
        os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Outlook.lnk")

    elif 'power point' in query:
        speak("Opening Microsoft Powerpoint...")
        os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/PowerPoint.lnk")

    elif 'word' in query:
        speak('Opening Microsoft Word...')
        os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Word.lnk")

    elif 'video meeting' in query:
        speak('Opening Zoom...')
        os.startfile("C:/Users/91745/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Zoom/Zoom.lnk")

    elif 'dev' in query:
        speak('Opening Dev c++ ...')
        os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Embarcadero Dev-C++/Dev-C++.lnk")

def youtubeauto():
    comm=takecommand()

    if  'play' in comm:
        keyboard.press_and_release('spacebar')
    
    elif 'mute' in comm:
        keyboard.press_and_release('m')
    
    elif 'seek forward' in comm:
        keyboard.press_and_release('right arrow key')
    
    elif 'seek backward' in comm:
        keyboard.press_and_release('left arrow key')

    elif 'increase volume' in comm:
        keyboard.press_and_release('up arrow key')

    elif 'decrease volume' in comm:
        keyboard.press_and_release('down arrow key')

    elif 'fullscreen' in comm:
        keyboard.press_and_release('f')

    elif 'captions' in comm:
        keyboard.press_and_release('c')
    
    elif 'next video' in comm:
        keyboard.press_and_release('Shift+N')

    elif 'previous video' in comm:
        keyboard.press_and_release("Shift+P")
    
    elif 'miniplayer' in comm:
        keyboard.press_and_release("i")
   
def chromeauto():
        speak('What you want boss !')
        command = takecommand()
        '''if 'google' in command:
            speak("OK Boss , This is what I found for your search !")
            query = query.replace("bumblebee","")
            query =query.replace("google search","")
            pywhatkit.search(query)
            speak("Done Sir !")'''
        
        if 'open new window' in command:
            keyboard.press_and_release('ctrl + n')
        
        elif 'private tab' in command:
            keyboard.press_and_release('Ctrl + Shift + n')

        elif 'new tab' in command:
            keyboard.press_and_release('Ctrl + t')

        elif 'open previous tab' in command:
            keyboard.press_and_release('Ctrl + Shift + t')
        
        elif 'jump on next tab' in command:
            keyboard.press_and_release('Ctrl + Tab')
        
        elif 'jump on previous tab' in command:
            keyboard.press_and_release('Ctrl + Shift + Tab')

        elif 'close current tab' in command:
            keyboard.press_and_release('Ctrl + w')

    #    elif 'minimize' in command:
     #       keyboard.press_and_release('Alt + Space + n')

        elif 'maximize' in command:
            keyboard.press_and_release('Alt + Space + x')
        
        elif 'close chrome' in command:
            keyboard.press_and_release('Alt + f4')
        
        elif 'clear browsing data' in command:
            keyboard.press_and_release('Ctrl + Shift + Delete')
        
        elif 'refresh the page' in command:
            keyboard.press_and_release('f5')
        
        elif 'print this page' in command:
            keyboard.press_and_release('Ctrl + p')
        
        elif 'save current page' in command:
            keyboard.press_and_release('Ctrl + s')

        elif 'bookmark' in command:
            keyboard.press_and_release('Ctrl + d')
        
        elif 'full screen' in command:
            keyboard.press_and_release('f11')
        
        elif 'close full screen' in command:
            keyboard.press_and_release('f11')
        
        #elif 'zoom in' in command:
        #   keyboard.press_and_release('Ctrl + +')
        
       # elif 'zoom out' in command:
        #    keyboard.press_and_release('Ctrl + -')
        
        elif 'end of page' in command:
            keyboard.press_and_release('end')

        elif 'top of the page' in command:
            keyboard.press_and_release('home')

        speak("Done boss !")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Bumblebee Boss. Please tell me how may I help you")       


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

if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takecommand()

# basic manner commands

        if 'hello' in query:
            speak("Hello Boss , I am bumblebee")
            speak("Ready for your service")
        
        elif 'nap time' in query:
            speak("You can call me any time")
            break 
        
        elif 'how are you' in query:
            speak("I am Fine")
            speak("And You ?")
        
        elif 'get lost' in query:
            speak("I am a virtual assistant , but you words are still very real")
            speak("please keep them respectful. ")

        elif 'thanks' in query:
            speak("It was the least I could do")

        elif 'thankyou' in query:
            speak("It was the least I could do")
        
# google automation commands
# 22commands in totoal

        elif 'google' in query:
            speak("OK Boss , This is what I found for your search !")
            query = query.replace("bumblebee","")
            query =query.replace("google search","")
            pywhatkit.search(query)
            speak("Done Sir !")
        
        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')
        
        elif 'private tab' in query:
            keyboard.press_and_release('Ctrl + Shift + n')

        elif 'new tab' in query:
            keyboard.press_and_release('Ctrl + t')

        elif 'open previous tab' in query:
            keyboard.press_and_release('Ctrl + Shift + t')
        
        elif 'jump on next tab' in query:
            keyboard.press_and_release('Ctrl + Tab')
        
        elif 'jump on previous tab' in query:
            keyboard.press_and_release('Ctrl + Shift + Tab')

        elif 'close current tab' in query:
            keyboard.press_and_release('Ctrl + w')

    #    elif 'minimize' in query:
     #       keyboard.press_and_release('Alt + Space + n')

        elif 'maximize' in query:
            keyboard.press_and_release('Alt + Space + x')
        
        elif 'close chrome' in query:
            keyboard.press_and_release('Alt + f4')
        
        elif 'clear browsing data' in query:
            keyboard.press_and_release('Ctrl + Shift + Delete')
        
        elif 'refresh the page' in query:
            keyboard.press_and_release('f5')
        
        elif 'print this page' in query:
            keyboard.press_and_release('Ctrl + p')
        
        elif 'save current page' in query:
            keyboard.press_and_release('Ctrl + s')

        elif 'bookmark' in query:
            keyboard.press_and_release('Ctrl + d')
        
        elif 'full screen' in query:
            keyboard.press_and_release('f11')
        
        elif 'close full screen' in query:
            keyboard.press_and_release('f11')
        
        #elif 'zoom in' in query:
        #   keyboard.press_and_release('Ctrl + +')
        
       # elif 'zoom out' in query:
        #    keyboard.press_and_release('Ctrl + -')
        
        elif 'end of page' in query:
            keyboard.press_and_release('end')

        elif 'top of the page' in query:
            keyboard.press_and_release('home')

        elif 'chrome tools'  in query:
            chromeauto()

# youtube automation commands
# 12 command in youtube automation
        elif 'youtube search' in query:
            speak("OK Boss , This is what I found for your search !")
            query = query.replace("bumblebee","")
            query =query.replace("youtube search","")
            web='https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("Done Sir !")


        elif 'play' in query:
            keyboard.press_and_release('spacebar')
    
        elif 'mute' in query:
            keyboard.press_and_release('m')
    
        elif 'seek forward' in query:
            keyboard.press_and_release('right arrow key')
    
        elif 'seek backward' in query:
            keyboard.press_and_release('left arrow key')

        elif 'increase volume' in query:
            keyboard.press_and_release('up arrow key')

        elif 'decrease volume' in query:
            keyboard.press_and_release('down arrow key')

        elif 'fullscreen' in query:
            keyboard.press_and_release('f')

        elif 'captions' in query:
            keyboard.press_and_release('c')
    
        elif 'next video' in query:
            keyboard.press_and_release('Shift+N')

        elif 'previous video' in query:
            keyboard.press_and_release("Shift+P")
    
        elif 'miniplayer' in query:
            keyboard.press_and_release("i")
        
        elif 'youtubetools' in query:
            youtubeauto()

#system applications automation 
#10 apps to be opened

        elif 'vs code' in query:
            openapps()
        
        elif 'microsoft' in query:
            openapps()
        
        elif 'access' in query:
            openapps()

        elif 'execl' in query:
            openapps()

        elif 'one note' in query:
            openapps()
        
        elif 'outlook' in query:
            openapps()
        
        elif 'Powerpoint' in query:
            openapps()
        
        elif 'word' in query:
            openapps()
        
        elif 'video meeting' in query:
            openapps()
        
        elif 'dev' in query:
            openapps()
        elif 'close gold' in query:
            closeapps()
        
        elif 'screenshot' in query:
            screenshot()
#make function of closing of the apps
#make queries for closing of the apps
#make function of closing of the apps
#make queries for closing of the apps

#make function of closing of the apps
#make queries for closing of the apps


#make function of closing of the apps
#make queries for closing of the apps


#make function of closing of the apps
#make queries for closing of the apps
