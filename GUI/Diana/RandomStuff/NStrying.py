from tkinter import *
Root=Tk()
blue = Label(Root, background="#003082")
#Button_1=Button(Root, text="Single", bg="#003082", fg="white")
photo = PhotoImage(file="C:\\Users\\Diana\\Pictures\\flag.gif")
label = Label(Root, image=photo)
label.pack()
Button_1=Button(Root, text="Single", bg="#003082", fg="white")
Button_1.pack()
Root['background'] = '#ffc917'
blue.pack(side=BOTTOM, fill= 'x')
Root.mainloop()
