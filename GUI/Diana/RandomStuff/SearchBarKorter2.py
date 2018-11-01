from tkinter import *
from tkinter.constants import *
from tkinter.messagebox import showinfo

class SearchBox(Frame):
    def __init__(self, master, entry_width=30, button_text="Search", command=None):
        Frame.__init__(self, master)
        self._command = command
        self.entry = Entry(self, width=entry_width)
        self.entry.pack(side=LEFT, fill=BOTH)
        self.entry.bind("<Return>", self._on_execute_command)
        self.button_label = Label(self, text=button_text, bg="#009688")
        self.button_label.pack(side=LEFT, fill=Y)
        self.button_label.bind("<ButtonRelease-1>", self._on_execute_command)

    def get_text(self):
        entry = self.entry
        return entry.get()

    def _on_execute_command(self, event):
        text = self.get_text()
        self._command(text)

def command(text):
    showinfo("search command", "searching:%s" % text)

root = Tk()
root['background'] = '#ffc917'
SearchBox(root, command=command).pack(pady=6, padx=3)
root.mainloop()
