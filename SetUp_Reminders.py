import speech_recogniton
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

if 'remember that' in query:
    remembermsg=query.replace('remember that',"")
    remembermsg=remembermsg.replace("bumblebee","")
    speak("You tell me to remind you that : "+remembermsg)
    remember = open('data.txt','w')
    remember.write(remembermsg)
    remember.close()

elif 'what do you remember' in query:
    remember = open('data.txt','r')
    speak("You tell me that" + remember.read())
