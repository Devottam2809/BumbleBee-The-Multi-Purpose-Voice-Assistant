from tkinter import*
from time import sleep

root=Tk()
root.config(bg="black")
root.attributes("-fullscreen",True)

Label(root,text="Loading...",font=('times new roman',15),bg="black",fg="orange").place(x=490,y=320)

for i in range(16):
    Label(root,bg="orange",width=2,height=1).place(x=(i+22)*22,y=350)

def play_animation():
    for i in range(200):
        for j in range(16):
            Label(root,bg="orange",width=2,height=1).place(x=(j+22)*22,y=350)
            sleep(0.6)
            root.update_idletasks()
            Label(root,bg="orange",width=2,height=1).place(x=(i+22)*22,y=350)  
    else:
        root.destroy()
        root.exit(0)    


root.update()
play_animation()

root.mainloop()
