from tkinter import *
root = Tk()

blue = Label(root, background="#003082")
#Button_1=Button(Root, text="Single", bg="#003082", fg="white")
#photo = PhotoImage(file="C:\\Users\\Diana\\Pictures\\vlag.gif")
#label = Label(root, image=photo)
#label.pack()

photo = PhotoImage(file="C:\\Users\\Diana\\Pictures\\flag.gif")
#label = Label(root, image=photo)
#label.pack()

Button_1=Button(root, text="Single", image=photo, fg="white")
Button_1.pack()
root['background'] = '#ffc917'
blue.pack(side=BOTTOM, fill= 'x')
#root.mainloop()

root.mainloop()