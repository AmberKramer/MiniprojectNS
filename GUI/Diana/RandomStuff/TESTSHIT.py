from tkinter import *


def write_slogan():
    print("Tkinter is easy to use!")

#import ctypes  # An included library with Python install.
#def Mbox(title, text, style):
#    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
#Mbox('Your title', 'Your text', 1)

root = Tk()
frame = Frame(root)
frame.pack()
photo = PhotoImage(file="C:\\Users\\Diana\\Pictures\\flag.gif")
button = Button(frame,
                   text="QUIT",
                   fg="red",

                   command=quit)
button.pack(side=LEFT)
slogan = Button(frame,
                   bg="#003082",
                   image=photo,
                   text="Hello",
                   command=write_slogan)
slogan.pack(side=LEFT)
#label = Label(root, image=photo)
#label.pack()

root.mainloop()
