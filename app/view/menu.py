from tkinter import * 
from tkinter.ttk import *

from app.controller.controller_reglage import ControllerReglage
from app.controller.controller_jeu import ControllerJeu

class View_menu():
    def __init__(self, master, jeux):
        self.master = master
        
        self.Frame1 = Frame(self.master, borderwidth=2, relief=GROOVE)
        self.Frame1.grid(row=0, column=0)

        taille = len(jeux)
        for i in range(taille):
            bouton_snake = Button(self.Frame1, command= lambda id = jeux[i].getId(): self.vue_jeu(id)  , text=jeux[i].getNom())
            bouton_snake.grid(row=i+1, column=0)

        bouton_parametre = Button(self.Frame1, command=self.vue_para, text="Parametre")
        bouton_parametre.grid(row=taille+1, column=0)

    def vue_para(self):
        self.Frame1.grid_forget()
        ControllerReglage().reglage(self.master)

    def vue_jeu(self, id):
        self.Frame1.grid_forget()
        ControllerJeu().jeu(self.master, id)