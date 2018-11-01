from tkinter import *
#Root = Tk()
root=Tk()
root.title("Kut NS")

#frame = Frame(root)
#frame.pack()
hello = Label(master = root, text = "") #master was niet duidelijk genoeg text staat voor de text in de GUI
yellow = Label(master = root, background = "#ffc917", width =  100, height = 100) # width height spreekt voorzich
#blue= Label(master = Root, background = "#003082", width =  120, height = 100)
bluerec=Label(master = root, background = "#003082", width =  100, height = 3)
bluerec.place(x=0, y=975)
#blue.pack(side="left", fill="y")
#root.wm_attributes('-alpha', 0.7)
photo = PhotoImage(file="C:\\Users\\Diana\\Pictures\\NSlogo.png")
label = Label(root, borderwidth=0, image=photo)
label.place(x=0, y=0,)



yellow.pack()
hello.pack() # zorgt voor de uiteindelijke text output
root.mainloop() # deze regel zou bij het runnen van de code een window moeten geven

import Image
im = Image.open("button.png")
print(im.mode)