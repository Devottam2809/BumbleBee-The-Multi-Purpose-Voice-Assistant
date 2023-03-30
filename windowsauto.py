import keyboard
import speech_recognition as sr
import pyttsx3

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


while True:
    query = takecommand()
    
    if 'show desktop' in query:
        keyboard.press_and_release('windows + D')
    
    elif 'windows explorer' in query:
        keyboard.press_and_release('windows + E')
    
    elif 'setting' in query:
        keyboard.press_and_release('windows + I')
    
    elif 'lock windows' in query:
        keyboard.press_and_release('windows + L')

    elif 'run' in query:
        keyboard.press_and_release('windows + R')
        speak("What do you want to search ?")
        kk=takecommand()
        keyboard.write(query)
        keyboard.press_and_release('enter')

    elif 'clipboard' in query:
        keyboard.press_and_release('windows + V')
    
    elif 'search' in query:
        keyboard.press_and_release('windows + Q')
        speak("What do you want to search ?")
        kk=takecommand()
        keyboard.write(query)
        keyboard.press_and_release('enter')
