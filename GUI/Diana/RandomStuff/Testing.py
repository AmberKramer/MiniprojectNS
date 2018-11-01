from tkinter import *
#import ImageTk

t = Tk()
t.title("Transparency")

frame = Frame(t)
frame.pack()

canvas = Canvas(frame, bg="black", width=500, height=500)
canvas.pack()

photoimage = PhotoImage(file="C:\\Users\\Diana\\Pictures\\NSlogo.png")
canvas.create_image(150, 150, image=photoimage)

t.mainloop()


import Image
im = Image.open("button.png")
print(im.mode)