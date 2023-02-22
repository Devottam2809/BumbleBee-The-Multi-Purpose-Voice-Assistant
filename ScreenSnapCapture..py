  import pyautogui
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

  if 'screenshot' in query:
      kk=pyautogui.screenshot()
      speak('ok boss ! What should i name the file...')
      path = takecommand()
      path1name = path + ".png"
      path1 = "" + path1name
      kk.save(path1)
      speak('Snap captured')
