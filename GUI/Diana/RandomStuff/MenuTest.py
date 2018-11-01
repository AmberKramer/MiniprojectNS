from tkinter import *
#from tkFileDialog import askopenfilename


def NewFile():
    print("New File!")


def OpenFile():
    #name = askopenfilename()
    print("open Test")
    #name


def About():
    print("This is a simple example of a menu")
def TESTS():
    button=Button(root, text="Dutch", image=photo, fg="white")  # , width = 5, height = 2)

root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
photo = PhotoImage(file="C:\\Users\\Diana\\Pictures\\flag.gif")
test = Menu(menu)

menu.add_cascade(label="test", menu=test)
test.add_command(label="test", command=TESTS, image= photo)


helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

mainloop()