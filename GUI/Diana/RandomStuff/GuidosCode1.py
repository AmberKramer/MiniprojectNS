from tkinter import *
import os

Root = Tk()
Root['background'] = '#ffc917'

def GUI2():
    os.system('py NS_GUI_2.py')

photo = PhotoImage(file="C:\\Users\\Diana\\Pictures\\flag-small.gif")
photo_2 = PhotoImage(file="C:\\Users\Diana\\Pictures\\UK.png")
blue = Label(Root, background="#003082", height = 3)
Button_1=Button(Root, command = GUI2 , text="Single", bg="#003082", fg="white", width = 20, height = 4, anchor= "w", borderwidth = 0, font = ("", 9, "bold"))
Button_2=Button(Root, text="Day Return", bg="#003082", fg="white", width = 20, height = 4, anchor= "w", borderwidth = 0, font = ("", 9, "bold"))
Button_3=Button(Root, text="5 Return Ticket", bg="#003082", fg="white", width = 20, height = 4, anchor= "w", borderwidth = 0, font = ("", 9, "bold"))
Button_4=Button(Root, text="Weekend Return", bg="#003082", fg="white", width = 20, height = 4, anchor= "w", borderwidth = 0, font = ("", 9, "bold"))
Button_5=Button(Root, text="Railrunner            \n4-11 (incl) years ", bg="#003082", fg="white", width = 20, height = 4, anchor= "w", borderwidth = 0, font = ("", 9, "bold"))
Button_6=Button(Root, text="Other Ticket", bg="#003082", fg="white", width = 20, height = 3, anchor= "w" ,borderwidth = 0, font = ("", 9, "bold"))
Button_7=Button(Root, text="'Via' Station", bg="#003082", fg="white", width = 20, height = 3, anchor= "w", borderwidth = 0, font = ("", 9, "bold"))
Button_8=Button(Root, text="Dutch", image = photo, fg="white", width = 45, height = 25, borderwidth = 1.5)
Button_9=Button(Root, text="English", image = photo_2, fg="white", width = 45, height = 25, borderwidth = 1.5)
Button_10=Button(Root, text="Stop       \nClear all", bg="#fe0000", fg="white", width = 20, height = 2, anchor = "w", borderwidth = 0, font = ("", 9, "bold" ))

#label = Label(Root, image=photo)
#label.pack(side=RIGHT, expand=FALSE)
#label.place(x=0, y=0)

blue.pack(side = BOTTOM, fill = "x")

Button_1.place(x = 5, y = 5)
Button_2.place(x = 5, y = 80)
Button_3.place(x = 5, y = 155)
Button_4.place(x = 5, y = 230)
Button_5.place(x = 5, y = 305)
Button_6.place(x = 5, y = 660)
Button_7.place(x = 160, y = 660)
Button_8.place(x = 20, y = 720)
Button_9.place(x = 100 , y = 720)
Button_10.place(x = 1210, y = 725)
T = Label(Root, text="Nederlands", bg = "#003082", fg = "white", borderwidth = 0, font = ("", 8, "bold"))
T.place(x = 11, y = 750)
T = Label(Root, text="English", bg = "#003082", fg = "white", borderwidth = 0, font = ("", 8, "bold"))
T.place(x = 103, y = 750)

Root.overrideredirect(True)
Root.geometry("{0}x{1}+0+0".format(Root.winfo_screenwidth(), Root.winfo_screenheight()))
Root.bind("<Escape>", lambda e: e.widget.quit())
Root.mainloop()