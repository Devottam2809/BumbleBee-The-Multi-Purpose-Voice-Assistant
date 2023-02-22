import pywhatkit
import pyttsx3
import speech_recognition

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

  if 'google search' in query:
      import wikipedia as googleScrap
      query = query.replace("Bumblebee","")
      query = query.replace("google search","")
      query = query .replace("google","")
      speak("This is what I found for your search...")
      pywhatkit.search(query)

      try:
          result = googleScrap.summary(query,1)
          speak(result)
      except:
          speak("No readable data")
