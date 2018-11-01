from tkinter import *
Root=Tk()
Root['background'] = '#ffc917'

photo = PhotoImage(file="C:\\Users\\Diana\\Pictures\\flag.gif")
blue = Label(Root, background="#003082", height = 3)
#blue = Label(Root, background="#003082", height = 3)
Button_1=Button(Root, text="Single", bg="#003082", fg="white", width = 20, height = 5)
Button_2=Button(Root, text="Dag Retour", bg="#003082", fg="white", width = 20, height = 5)
Button_3=Button(Root, text="5 Return Ticket", bg="#003082", fg="white", width = 20, height = 5)
Button_4=Button(Root, text="Weekend Return", bg="#003082", fg="white", width = 20, height = 5)
Button_5=Button(Root, text="Railrunner ", bg="#003082", fg="white", width = 20, height = 5)
Button_6=Button(Root, text="Other Ticket", bg="#003082", fg="white", width = 20, height = 5)
Button_7=Button(Root, text="'via' Station", bg="#003082", fg="white", width = 20, height = 5)
Button_8=Button(Root, text="Dutch", image = photo, fg="white")#, width = 5, height = 2)
Button_9=Button(Root, text="English", bg="#003082", fg="white", width = 5, height = 2)
Button_10=Button(Root, text="Stop\n Clear all", bg="#fe0000", fg="white", width = 20, height = 2)



#label = Label(Root, image=photo)
#label.pack(side=RIGHT, expand=FALSE)
#label.place(x=0, y=0)


#blue.grid(row = 50)
blue.pack(side=BOTTOM, fill= 'x')


Button_1.pack()
Button_2.pack()
Button_3.pack()
Button_4.pack()
Button_5.pack()
Button_6.pack()
Button_7.pack()
Button_8.pack()
Button_9.pack()
Button_10.pack()
Root.mainloop()