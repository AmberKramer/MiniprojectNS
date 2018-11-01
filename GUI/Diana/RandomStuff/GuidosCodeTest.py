from tkinter import *



import os
import tkinter
Root=tkinter.Tk()
#Root=Tk()
Root['background'] = '#ffc917'
Root.overrideredirect(True)
Root.geometry("{0}x{1}+0+0".format(Root.winfo_screenwidth(), Root.winfo_screenheight()))
Root.bind("<Escape>", lambda e: e.widget.quit())

def helloCallBack():
    os.system('python GuidosCode.py')

#B=tkinter.Button(Root,text="spam",command= helloCallBack,  bg="#003082", fg="white", width = 20, height = 4)
#B.pack()
#top.mainloop()

photo = PhotoImage(file="C:\\Users\\Diana\\Pictures\\flag-small.gif")
photo_2 = PhotoImage(file="C:\\Users\Diana\\Pictures\\UK.png")
blue = Label(Root, background="#003082", height = 3)
#Button_1=Button(Root, text="Single", bg="#003082", fg="white", width = 20, height = 4)
Button_1=Button(Root, text="Single", command= helloCallBack, bg="#003082", fg="white", width = 20, height = 4)
Button_1.pack()
Button_2=Button(Root, text="Dag Retour", bg="#003082", fg="white", width = 20, height = 4)
Button_3=Button(Root, text="5 Return Ticket", bg="#003082", fg="white", width = 20, height = 4)
Button_4=Button(Root, text="Weekend Return", bg="#003082", fg="white", width = 20, height = 4)
Button_5=Button(Root, text="Railrunner ", bg="#003082", fg="white", width = 20, height = 4)
Button_6=Button(Root, text="Other Ticket", bg="#003082", fg="white", width = 20, height = 3)
Button_7=Button(Root, text="'via' Station", bg="#003082", fg="white", width = 20, height = 3)
Button_8=Button(Root, text="Dutch", image = photo, fg="white", width = 50, height = 30)
Button_9=Button(Root, text="English", image = photo_2, fg="white", width = 50, height = 30)
Button_10=Button(Root, text="Stop\n Clear all", bg="#fe0000", fg="white", width = 20, height = 2)

#label = Label(Root, image=photo)
#label.pack(side=RIGHT, expand=FALSE)
#label.place(x=0, y=0)

blue.pack(side = BOTTOM, fill = "x")

Button_1.place(x = 5, y = 5)
Button_2.place(x = 5, y = 80)
Button_3.place(x = 5, y = 155)
Button_4.place(x = 5, y = 230)
Button_5.place(x = 5, y = 305)
Button_6.place(x = 5, y = 593)
Button_7.place(x = 160, y = 593)
Button_8.place(x = 20, y = 658)
Button_9.place(x = 100 , y = 658)
Button_10.place(x = 1210, y = 660)
T = Label(Root, text="Nederlands", bg="#003082")#, height=2, width=30)
T.place(x = 20, y = 695)

#Root.attributes('-transparentcolor', T["bg"])


Root.mainloop()