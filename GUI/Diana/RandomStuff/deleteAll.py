from tkinter import *

buttons = []

def remove():
    for btn in buttons:
        btn.destroy()

def main():

    root = Tk()
    rem_btn = Button(command=remove, text="Remove all")
    rem_btn.grid(row=8, column=0, columnspan=8, sticky="ew")

    for pos in range(0, 64):
        btn = Button(command=lambda pos=pos: print(pos), width=5, height=2, relief=RIDGE, text=pos)
        btn.grid(row=pos // 8, column=pos % 8)
        buttons.append(btn)

    root.mainloop()

main()