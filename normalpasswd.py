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

def passw(pass_inp):
    password = "aabbccdd"
    passs = str(password)
    if passs==str(pass_inp):
        speak("Access Granted")
    else:
        speak("Access Denied")

if __name__=="__main__":
    speak("Please enter the password :")
    passsss=input()
    passw(passsss)