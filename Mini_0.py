import struct
import pyaudio
from winotify import Notification,audio
from urllib.request import urlopen

import face_recognition
import cv2
import numpy as np

import pyttsx3
import speech_recognition as sr

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voice', voices[2].id)
Assistant.setProperty('rate',170)

toast = Notification(app_id = "BumbleBee Launched",title = "Voice Assistant Activated",msg = "Hi! I am BumbleBee, your Mutipurpose Voice Assistant.",duration = "short",icon="C:/Users/91745/Desktop/Final Finished Code/Bumblebeeicon.png")
toast.set_audio(audio.Default,loop=False)
toast.add_actions(label = "Click Here",launch="C:/Users/91745/Desktop/Final Finished Code")

def check_internet():
    try:
        urlopen('https://www.google.com',timeout=1)
        return True
    except:
        return False

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

#speak("Initializing face recognition")
#speak("Checking face match")
speak("initializing face recognition")
speak("checking for a match")

video = cv2.VideoCapture(0)
 
face = face_recognition.load_image_file("image.jpg")
faceencoding = face_recognition.face_encodings(face)[0]
 
face_encodings_list = [
    faceencoding]
 
face_encodings = []
s = True
face_coordinates=[]
 
  
while True:
    _,frame = video.read()
 
    resized_frame = cv2.resize(frame, (0, 0), fx=0.50, fy=0.50)
 
    resized_frame_rgb = resized_frame[:, :, ::-1]

 
    if s:
        face_coordinates = face_recognition.face_locations(resized_frame_rgb)
        face_encodings = face_recognition.face_encodings(resized_frame_rgb, face_coordinates)

        for faces in face_encodings:
            matches = face_recognition.compare_faces(face_encodings_list, faces)
            if matches[0] == True:
                video.release()
                cv2.destroyAllWindows()
                #main_program()
                speak("Access Granted")
                
                speak("Initializing...")
                speak("Checking all ports and connections...")
                speak("Checking Internet connection...")
                #if(check_internet()):
                speak("  ")
                speak("You are now Online !")
                from jGUI import start_animation
                start_animation()
                
                toast.show()
                print("hotword detected")

                from Mini_3 import wishMe
                wishMe()

            #speak("Welcome Boss")
                from Mini_1 import access
                access()
                #else:
                 #   speak("No Internet Connection")

                #speak("Welcome Sir")
                #print("WORKING FACE RECOGNITION")
    else:
       speak("Access denied")
       break
    #cv2.imshow('Face Scan', frame)

    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break
 
video.release()
cv2.destroyAllWindows()