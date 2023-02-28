import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import os

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

def My_Location():
        ip_add =requests.get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/'+ip_add+'.json'
        geo_q=requests.get(url)
        geo_d= geo_q.json()
        state = geo_d['city']
        country=geo_d['country']
        speak(f"Sir you are now in {state , country}")

def temperature():
    search = 'Temperature in kanpur'
    url = f"https://www.google.com/search?q= + {search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text , "html.parser")
    temperature = data.find("div",class_= "BNeawe").text
    speak(f"The temperature is :{temperature}")

def notepad():
    #speak("Tell me what I need to write ?")
    speak("I am ready to write")
    writes = takecommand()
    speak("Do you want to save the file")
    ask=takecommand()
    if 'yes' in ask:
        speak("Name the file...")
        time = takecommand()
    #time = int(datetime.now().strftime("%H:%M"))
        filename = str(time)+"_note.txt"
        with open(filename,"w") as file:
            file.write(writes)
        path1 = ""+str(filename)
        os.startfile(path1)
        speak("File Saved...")
    else:
        speak("Draft Dumped")


