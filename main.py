from tkinter import * 
from tkinter.ttk import * 

from app.controller.controller_menu import ControllerMenu

class main(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Jeux")
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid(sticky="NSEW")
        self.createWidgets()
        self.frame()

    def createWidgets(self):
        mainFrame = Frame(self.master, borderwidth=2, relief="groove")
        mainFrame.grid(column=0, row=0, sticky="NSEW",rowspan=2)

    def frame(self):
        ControllerMenu().menu(self.master)

if __name__ == '__main__':
    main().mainloop()

