from tkinter import *
root = Tk()

photo = PhotoImage(file="C:\\Users\\Diana\\Pictures\\logo.gif")
label = Label(root, image=photo)
label.pack()

root.mainloop()