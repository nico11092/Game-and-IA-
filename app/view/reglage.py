from multiprocessing.sharedctypes import Value
from tkinter import * 
from tkinter.ttk import *

from app.controller import controller_menu

class View_reglage():
    def __init__(self, master, tab):
        self.master = master

        self.Frame1 = Frame(self.master, borderwidth=2, relief=GROOVE)
        self.Frame1.grid(row=0, column=0)

        self.chkValue = BooleanVar() 
        self.chkValue.set(tab.getEtat_Clavier())
        C1 = Checkbutton(self.Frame1, text = "Clavier", variable=self.chkValue, width = 20)
        C1.grid(row=0, column=0)

        self.chkValue1 = BooleanVar() 
        self.chkValue1.set(tab.getEtat_Cam())
        C2 = Checkbutton(self.Frame1, text = "Caméra", variable=self.chkValue1, width = 20)
        C2.grid(row=1, column=0)

        bouton_sauv = Button(self.Frame1, command=self.vue_menu, text="Sauvegarder")
        bouton_sauv.grid(row=2, column=0)

    def vue_menu(self):
        self.Frame1.grid_forget()
        
        controller_menu.ControllerMenu().menu(self.master)

