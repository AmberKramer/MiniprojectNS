from tkinter import *
#Root = Tk()
root=Tk()
hello = Label(master = root, text = "") #master was niet duidelijk genoeg text staat voor de text in de GUI
yellow = Label(master = root, background = "#ffc917", width =  100, height = 100) # width height spreekt voorzich
#blue= Label(master = Root, background = "#003082", width =  120, height = 100)
bluerec=Label(master = root, background = "#003082", width =  100, height = 3)
bluerec.place(x=0, y=975)
#blue.pack(side="left", fill="y")

photo = PhotoImage(file="C:\\Users\\Diana\\Pictures\\logo.gif")
label = Label(root, image=photo)
label.pack()
yellow.pack()
hello.pack() # zorgt voor de uiteindelijke text output
root.mainloop() # deze regel zou bij het runnen van de code een window moeten geven