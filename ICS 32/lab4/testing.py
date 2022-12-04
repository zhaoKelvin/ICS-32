from tkinter import *

class App:
    def __init__(self, root):
        self.root = root
        self.number = 4 #change me to get more buttons
        self.buttons = []
        for i in range(self.number):
            self.buttons.append(Button(self.root, text="Change!", bg="white", command=lambda c=i: self.command(c)))
            self.buttons[i].pack()
    def command(self, var):
        for i in range(self.number):
            self.buttons[i].configure({"bg": "white", "activebackground": "white"})
        self.buttons[var].configure({"bg": "lightblue", "activebackground": "lightblue"})

root = Tk()
App(root)
root.mainloop()