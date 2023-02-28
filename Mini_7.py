import pyttsx3
import speech_recognition as sr
import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',passwd='psit1234',database="finalproject")
mycursor=mydb.cursor()


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

#mycursor.execute("show databases")
#for i in mycursor:
#   print(i)

def names():
    from Mini_2 import push_notifications
    push_notifications()
    mycursor.execute("select name from student")
    for i in mycursor:
        speak(i)

def feesubmit():
    from Mini_2 import push_notifications
    push_notifications()
    mycursor.execute("select name from student where feesubmit='No'")
    for i in mycursor:
        speak(i)
    
def aname():
    from Mini_2 import push_notifications
    push_notifications()
    mycursor.execute("select name from student where name like 'A%'")
    for i in mycursor:
        speak(i)

def dname():
    from Mini_2 import push_notifications
    push_notifications()
    mycursor.execute("select name from student where name like 'D%'")
    for i in mycursor:
        speak(i)

    
def kname():
    from Mini_2 import push_notifications
    push_notifications()
    mycursor.execute("select name from student where name like 'K%'")
    for i in mycursor:
        speak(i)

def sname():
    from Mini_2 import push_notifications
    push_notifications()
    mycursor.execute("select name from student where name like 'S%'")
    for i in mycursor:
        speak(i)

def betweenrollno():
    from Mini_2 import push_notifications
    push_notifications()
    mycursor.execute("select name from student where rollno between 2101640100016 and 2101640100115")
    for i in mycursor:
        speak(i)


