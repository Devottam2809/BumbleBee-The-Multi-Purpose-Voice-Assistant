def notepad():
    #speak("Tell me what I need to write ?")
    speak("I am ready to write")
    writes = takecommand()
    speak("Do you want to save the file")
    ask=takecommand()
    if 'yes' in ask:
        speak("Name the file...")
        time = takecommand()
    #time = int(datetime.now().strftime("%H:%M"))
        filename = str(time)+"_note.txt"
        with open(filename,"w") as file:
            file.write(writes)
        path1 = ""+str(filename)
        os.startfile(path1)
        speak("File Saved...")
    else:
        speak("Draft Dumped")
 
notepad()
