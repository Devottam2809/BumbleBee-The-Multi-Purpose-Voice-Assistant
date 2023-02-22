import pyttsx3
import speech_recognitiono
import pywikihow

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
        toast.show()
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing....")
            query = command.recognize_google(audio,language='en-in')
            print(f"You said : {query}")

        except Exception as Error:
            return "none"
        
        return query.lower()
     
   if 'how to' in query:
    speak("Getting data from the internet...")
    op=query.replace("bumblebee","")
    result = 1
    howtofunc= search_wikihow(op,result)
    assert len(howtofunc)==1
    howtofunc[0].print()
    speak(howtofunc[0].summary)
