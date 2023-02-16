import os
import screen_brightness_control as sbc
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
      
if 'restart' in query:
  speak("Comming back in a minute")
  os.system("shutdown /r /t 1")

elif 'shutdown' in query:
  speak("bye bye !")
  os.system("shutdown /s /t 1")
elif 'increase brightness' in query:
  #current_brightness = sbc.get_brightness()
  speak("The current brightness level is")
  speak(sbc.get_brightness())
  kk=sbc.get_brightness()
  #speak("What level of brightness do you want")
  #dd=takecommand()
  dd=kk[0]+20
  sbc.set_brightness(dd)
  speak("Brightness level set to")
  speak(dd)

elif 'decrease brightness' in query:
  speak("The current brightness level is")
  speak(sbc.get_brightness())
  kk=sbc.get_brightness()
  #speak("What level of brightness do you want")
  #dd=takecommand()
  dd=kk[0]-20
  sbc.set_brightness(dd)
  speak("Brightness level set to")
  speak(dd)
