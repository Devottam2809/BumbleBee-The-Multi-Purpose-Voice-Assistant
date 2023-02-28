import pyttsx3
import speech_recognition as sr
import os
import screen_brightness_control as sbc
import keyboard
import datetime
import pyjokes
import speedtest
import requests
import pywhatkit
import pyautogui
import wikipedia
from bs4 import BeautifulSoup
from pydub import AudioSegment 
from pydub.playback import play
import pywikihow
import webbrowser
from pywikihow import search_wikihow
from winotify import Notification,audio

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voice', voices[2].id)
Assistant.setProperty('rate',170)

toast = Notification(app_id = "BumbleBee Launched",title = "Voice Assistant Activated",msg = "Assistant Listening....",duration = "short",icon="C:/Users/91745/Desktop/Final Finished Code/Bumblebeeicon.png")
toast.set_audio(audio.Default,loop=False)
toast.add_actions(label = "Click Here",launch="C:/Users/91745/Desktop/Final Finished Code")
     


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

def SpeedTest(query):
    speak("Checking Speed...")
    speed = speedtest.Speedtest()
    downloading =speed.download()
    correctDown = int(downloading/800000)
    uploading=speed.upload()
    correctupload=int(uploading/800000)
    if 'upload speed' in query:
        speak(f"The uploading speed is : {correctupload} mbps")

    elif 'download speed' in query:
        speak(f"The downloading speed is : {correctDown} mbps")

    else:
        speak(f"The uploading speed is : {correctupload} mbps and the downloading speed is {correctDown} mbps")


    '''def My_Location():
        ip_add =requests.get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/'+ip_add+'.json'
        geo_q=requests.get(url)
        geo_d= geo_q.json()
        state = geo_d['city']
        country=geo_d['country']
        speak(f"Sir you are now in {state , country}")

    def temperature():
        search = 'Temperature in kanpur'
        url = f"https://www.google.com/search?q= + {search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text , "html.parser")
        temperature = data.find("div",class_= "BNeawe").text
        speak(f"The temperature is :{temperature}")

    def notepad():
        #speak("Tell me what I need to write ?")
        speak("I am ready to write")
        writes = takecommand()
        speak("Name the file...")
        time = takecommand()
        #time = int(datetime.now().strftime("%H:%M"))
        filename = str(time)+"_note.txt"
        with open(filename,"w") as file:
            file.write(writes)
        path1 = ""+str(filename)
        os.startfile(path1)
        speak("File Saved...")'''

'''    def SpeedTest():
        speak("Checking Speed...")
        speed = speedtest.Speedtest()
        downloading =speed.download()
        correctDown = int(downloading/800000)
        uploading=speed.upload()
        correctupload=int(uploading/800000)
        if 'upload speed' in query:
            speak(f"The uploading speed is : {correctupload} mbps")

        elif 'download speed' in query:
            speak(f"The downloading speed is : {correctDown} mbps")

        else:
            speak(f"The uploading speed is : {correctupload} mbps and the downloading speed is {correctDown} mbps")'''


def taskxe():
    query = takecommand()
        
    if 'hello' in query:
        speak("Hey DC, your assistant at your service")
        #speak("Ready for your service")
    
    elif 'go sleep' in query:
        speak("Bye Bye")
        audio=AudioSegment.from_wav("NAintro.wav")
        play(audio)
        #break 
    
    elif 'how are you' in query:
        speak("I am feeling A1")
        speak("And You ?")
    
    elif 'get lost' in query:
        speak("I am a virtual assistant , but you words are still very real")
        speak("please keep them respectful. ")

    elif 'thanks' in query:
        speak("It was the least I could do")

    elif 'thank you' in query:
        speak("It was the least I could do")

#OS COMMAND
    elif 'restart' in query:
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
    
#Windows Automation
    elif 'Show desktop' in query:
        speak("Ok, switching to desktop")
        keyboard.press_and_release('windows + D')
    
    elif 'windows explorer' in query:
        speak("Ok, launching windows explorer")
        keyboard.press_and_release('windows + E')
    
    elif 'setting' in query:
        speak("launching windows settings")
        keyboard.press_and_release('windows + I')
    
    elif 'lock windows' in query:
        keyboard.press_and_release('windows + L')
        speak("Ok, locking the system")
        speak("I will take care of your data")

    elif 'run' in query:
        keyboard.press_and_release('windows + R')
        speak("What do you want to search ?")
        query=takecommand()
        keyboard.write(query)
        keyboard.press_and_release('enter')

    elif 'clipboard' in query:
        speak("Lets, see what you have collected")
        keyboard.press_and_release('windows + V')
    
    elif 'windows search' in query:
        keyboard.press_and_release('windows + Q')
        speak("What do you want to search ?")
        query=takecommand()
        keyboard.write(query)
        keyboard.press_and_release('enter')
#Alarm
    elif 'set alarm' in query:
        speak("Enter the time :")
        time = input(": Enter the time :")

        while True:
            Time_Ac = datetime.datetime.now()
            now = Time_Ac.strftime("%H:%M:%S")

            if now == time:
                speak("Time to wake up Boss...")
                from Mini_2 import startalarm
                startalarm()
                speak("Alarm Closed !")
            elif now>time:
                break
    
    elif 'joke' in query:
        get  =pyjokes.get_joke()
        speak(get)
        from Mini_2 import laugh
        laugh()

    elif 'upload speed' in query:
        SpeedTest(query)
    
    elif 'download speed' in query:
        SpeedTest(query)
    
    elif 'internet speed' in query:
        SpeedTest(query)
    
    elif 'notepad' in query:
        from Mini_6 import notepad
        notepad()
    
    elif 'temperature' in query:
        from Mini_6 import temperature
        temperature()
    
    elif 'my location' in query:
        from Mini_6 import My_Location
        My_Location()
    
    elif 'screenshot' in query:
        kk=pyautogui.screenshot()
        speak('ok boss ! What should i name the file...')
        path = takecommand()
        path1name = path + ".png"
        path1 = "" + path1name
        kk.save(path1)
        speak('Snap captured')

    elif 'remember that' in query:
        remembermsg=query.replace('remember that',"")
        remembermsg=remembermsg.replace("bumblebee","")
        speak("You tell me to remind you that : "+remembermsg)
        remember = open('data.txt','w')
        remember.write(remembermsg)
        remember.close()

    elif 'what do you remember' in query:
        remember = open('data.txt','r')
        speak("You tell me that" + remember.read())
    
#Chrome Automation
    elif 'google search' in query:
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
    
    elif 'how to' in query:
        speak("Getting data from the internet...")
        op=query.replace("bumblebee","")
        result = 1
        howtofunc= search_wikihow(op,result)
        assert len(howtofunc)==1
        howtofunc[0].print()
        speak(howtofunc[0].summary)
    
    elif 'open new window' in query:
        keyboard.press_and_release('ctrl + n')
    
    elif 'anonymous' in query:
        keyboard.press_and_release('Ctrl + Shift + n')

    elif 'new tab' in query:
        keyboard.press_and_release('Ctrl + t')

    elif 'open previous tab' in query:
        keyboard.press_and_release('Ctrl + Shift + t')
    
    elif 'jump on next tab' in query:
        keyboard.press_and_release('Ctrl + Tab')
    
    elif 'jump on previous tab' in query:
        keyboard.press_and_release('Ctrl + Shift + Tab')

    elif 'close current tab' in query:
        keyboard.press_and_release('Ctrl + w')

    elif 'minimise' in query:
        keyboard.press('Alt')
        keyboard.press('Space')
        keyboard.press('n')
        keyboard.release('n')
        keyboard.release('Space')
        keyboard.release('Alt')

    #elif 'maximize' in query:
        #   keyboard.press_and_release('Alt + Space + X')
    
    elif 'close chrome' in query:
        keyboard.press_and_release('Alt + f4')
    
    elif 'clear browsing data' in query:
        keyboard.press_and_release('Ctrl + Shift + Delete')
    
    elif 'refresh the page' in query:
        keyboard.press_and_release('f5')
    
    elif 'print this page' in query:
        keyboard.press_and_release('Ctrl + p')
    
    elif 'save current page' in query:
        keyboard.press_and_release('Ctrl + s')

    elif 'bookmark' in query:
        keyboard.press_and_release('Ctrl + d')
        keyboard.press('enter')
    
    elif 'full screen' in query:
        keyboard.press_and_release('f11')
    
    elif 'close full screen' in query:
        keyboard.press_and_release('f11')
        
    elif 'zoomin' in query:
        keyboard.press('Ctrl')
        keyboard.press('+')
        keyboard.release('Ctrl')
        keyboard.release('+')
    
    #elif 'zoom out' in query:
        #   keyboard.press('Ctrl')
        #  keyboard.press('-')
        # keyboard.release('Ctrl')
        #keyboard.release('-')
    
    elif 'end of page' in query:
        keyboard.press_and_release('End')

    elif 'top of the page' in query:
        keyboard.press_and_release('Home')

    elif 'switch tab' in query:
        tab = query.replace("switch tab","")
        Tab = tab.replace("to","")
        num=Tab

        bb = f'Ctrl + {num}'
        keyboard.press_and_release(bb)

#youtube automation
    elif 'youtube search'  in query:
        speak("OK Boss , This is what I found for your search !")
        query = query.replace("bumblebee","")
        query =query.replace("youtube search","")
        web='https://www.youtube.com/results?search_query=' + query
        webbrowser.open(web)
        speak("Done Sir !")

    elif 'play' in query:
        keyboard.press_and_release('spacebar')

    elif 'pause' in query:
        keyboard.press_and_release('spacebar')

    elif 'mute' in query:
        keyboard.press_and_release('m')

    #elif 'forward' in query:
        #  keyboard.press_and_release('Right arrow')

    #elif 'backward' in query:
    #    keyboard.press_and_release('Left arrow')

    elif 'increase volume' in query:
        keyboard.press_and_release('Up Arrow')

    elif 'decrease volume' in query:
        keyboard.press_and_release('Down Arrow')

    elif 'fullscreen' in query:
        keyboard.press_and_release('f')

    elif 'caption' in query:
        keyboard.press_and_release('c')

    elif 'next video' in query:
        keyboard.press_and_release('Shift+N')

    elif 'past video' in query:
        keyboard.press_and_release("Shift+P")

    elif 'miniplayer' in query:
        keyboard.press_and_release("i")
    
    elif 'close youtube' in query:
        keyboard.press_and_release("alt+f4")

#IOT Module
    elif 'turn on' in query or 'turn off' in query:
        from Mini_5 import IOT
        IOT(query)

# SQL QUERIES
    elif 'get me names' in query:
        speak("Fetching records from the database")
        from Mini_7 import names
        names()
    
    elif 'give me' in query:
        speak("Fetching records from the database")
        #query = query.replace("bumblebee","")
        #query =query.replace("give me","")
        #query = query.replace("bumblebee","")
        #query =query.replace("list","")
        from Mini_7 import feesubmit
        feesubmit()
    
    elif 'name starts with' in query:
        speak("Fetching records from the database")
        from Mini_7 import kname
        kname()
    
    elif 'roll number' in query:
        speak("Fetching records from the database")
        # 16 to 115
        from Mini_7 import betweenrollno
        betweenrollno()
        
    elif 'time table' in query:
        from Mini_8 import time
        time()

