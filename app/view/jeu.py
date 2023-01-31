from tkinter import * 
from tkinter.ttk import *

from app.controller import controller_menu
from app.view.snake import View_Snake
from app.view.pong import View_Pong

class View_jeu():
    def __init__(self, master, jeu, score):
        self.master = master

        self.Frame1 = Frame(self.master, borderwidth=2, relief=GROOVE)
        self.Frame1.grid(row=0, column=0)

        titre = Label(self.Frame1, text=jeu[0][1])
        titre.grid(row=0, column=0, columnspan=2)

        score_titre = Label(self.Frame1, text="Meilleur score : ")
        score_titre.grid(row=1, column=0)

        score = Label(self.Frame1, text=score[0][1])
        score.grid(row=1, column=1)

        bouton_retour = Button(self.Frame1, command=self.vue_menu, text="Retour")
        bouton_retour.grid(row=2, column=0)

        bouton_jouer = Button(self.Frame1, command= lambda :self.lancement_jeu(jeu[0][0]), text="Jouer")
        bouton_jouer.grid(row=2, column=1)

    def vue_menu(self):
        self.Frame1.grid_forget()
        
        controller_menu.ControllerMenu().menu(self.master)

    def lancement_jeu(self, id):
        self.Frame1.grid_forget()

        if id == 0:
            View_Snake(self.master)
        elif id == 1 :
            View_Pong(self.master)


        