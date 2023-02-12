import tkinter as tk
from tkinter import Label
from time import sleep
from PIL import ImageTk, Image 
import time

root=tk.Tk()
root.geometry('800x800')
#root.tk_setPalette("black")
root.config(background="black")
root.wm_attributes('-alpha', 0.5)
width_of_window = 427
height_of_window = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
root.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

image_a=ImageTk.PhotoImage(Image.open('c2.png'))
image_b=ImageTk.PhotoImage(Image.open('c1.png'))

#root.wm_attributes('-fullscreen', 'True')
#root.wm_attributes('-topmost', True)
root.overrideredirect(1)

index=0
txt1=['H|','He|','Hel|','Hell|','Hello|',
'Hello W|','Hello Wo|','Hello Wor|','Hello Worl|','Hello World|']

txt2=['B|','Bu|','Bum|','Bumb|','Bumbl|','Bumble|','BumbleB|','BumbleBe|','BumbleBee']


def load():
    for i in range(5): #5loops
        l1=Label(root, image=image_a, border=0).place(x=180, y=145)
        l2=Label(root, image=image_b, border=0).place(x=200, y=145)
        l3=Label(root, image=image_b, border=0).place(x=220, y=145)
        l4=Label(root, image=image_b, border=0).place(x=240, y=145)
        root.update_idletasks()
        time.sleep(0.5)

        l1=Label(root, image=image_b, border=0).place(x=180, y=145)
        l2=Label(root, image=image_a, border=0).place(x=200, y=145)
        l3=Label(root, image=image_b, border=0).place(x=220, y=145)
        l4=Label(root, image=image_b, border=0).place(x=240, y=145)
        root.update_idletasks()
        time.sleep(0.5)

        l1=Label(root, image=image_b, border=0).place(x=180, y=145)
        l2=Label(root, image=image_b, border=0).place(x=200, y=145)
        l3=Label(root, image=image_a, border=0).place(x=220, y=145)
        l4=Label(root, image=image_b, border=0).place(x=240, y=145)
        root.update_idletasks()
        time.sleep(0.5)

        l1=Label(root, image=image_b, border=0).place(x=180, y=145)
        l2=Label(root, image=image_b, border=0).place(x=200, y=145)
        l3=Label(root, image=image_b, border=0).place(x=220, y=145)
        l4=Label(root, image=image_a, border=0).place(x=240, y=145)
        root.update_idletasks()
        time.sleep(0.5)


def start_animation():
    global index
    if not index+1 > len(txt2):

        text_animation_lb.config(text=txt2[index])
        index+=1
        root.after(500,start_animation)

    else:
        load()
        index=0
        text_animation_lb.config(text='|')
        root.after(500,start_animation)
        root.destroy()
        
        
text_animation_lb=tk.Label(root,text="|",fg="yellow",bg='black')
text_animation_lb.config(font=('snap itc',50))
text_animation_lb.pack(pady=20)

root.after(1000,start_animation)
root.mainloop()