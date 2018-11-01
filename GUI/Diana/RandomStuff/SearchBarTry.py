from tkinter import *
tests=[['test','9:04' ], ['Utrecht CS', '9:05'],['test','9:06' ], ['test', '9:07'],['test','9:08' ], ['test', '9:09'],['Utrecht CS','9:09' ], ['test','9:10']]
def meuk(name):
    testing=""
    for naam in tests:

        if naam[0]==name:
            testing+=(name+" vertrekt om "+naam[1]+"\n")
    label=Label(text=testing, anchor = E, width = 20, bg="pink")
    label.place(x=10, y=300)



def reply(name):
    label=Label( text = "Hello %s!" % name)
    label.place(x=10,y=10)
    meuk(name)
top = Tk()

ent = Entry(top,font=("",36))
ent.bind("<Return>", (lambda event: reply(ent.get())))
ent.place(x=30,y=30, width=500, height =50)
btn = Button(top,text="Submit", command=(lambda: reply(ent.get())))
btn.pack()

top.mainloop()