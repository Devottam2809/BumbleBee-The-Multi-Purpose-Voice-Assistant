import pyttsx3
import speech_recognition as sr

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

def task_ui():
    while True:
    
        query = takecommand()
# basic manner commands
# 6 commands

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

        elif 'thank you' in query:
            speak("It was the least I could do")

task_ui()