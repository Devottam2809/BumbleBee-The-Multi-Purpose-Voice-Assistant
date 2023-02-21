from datetime import datetime
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
            

one='''
In this time ,you have to workout.
'''

two='''
In this time you have to study Maths, because the CT marks are just disgusting.
'''

three='''
Time to code.
Make a post on Github.

Check your linkedin
'''

four='''
In this time you have to study.
'''
def time():
    hour=int(datetime.now().strftime("%H"))
    if hour>6  and hour<=7:
        speak(f'In this time ,you have to workout.')

    elif hour>=9 and hour<=12:
        speak(two)
    
    elif hour>=16 and hour<=18:
        speak(three)

    elif hour >= 20 and hour<=25:
        speak(four)
    else:
        speak("Take Rest")
