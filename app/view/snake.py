from tkinter import *
from tkinter.ttk import * 
from random import randrange

from app.controller import controller_menu

class View_Snake():
    def __init__(self, master):
        self.master = master

        self.Frame1 = Frame(self.master, borderwidth=2, relief=GROOVE)
        self.Frame1.grid(row=0, column=0)

        x = 245
        y = 24        
        self.dx, self.dy = 10, 10
        self.flag = 0
        self.direction = 'haut'
        self.Serpent=[[x,y],[x+2.5,y+2.5],[x+5,y+5],[0,0]]
        self.score = 0

        self.pX = randrange(5, 495)
        self.pY = randrange(5, 495)

        self.can = Canvas(self.Frame1, width=500, height=500, bg='black')
        self.can.grid(row=1, column=0, columnspan=3)

        oval1= self.can.create_oval(self.Serpent[1][0], self.Serpent[1][1], self.Serpent[1][0] +10, self.Serpent[1][1]+10, outline='green', fill='red')
        oval = self.can.create_oval(self.Serpent[0][0], self.Serpent[0][1], self.Serpent[0][0]+10, self.Serpent[0][1]+10, outline='green', fill='green')
        self.pomme = self.can.create_rectangle(self.pX, self.pY, self.pX+5, self.pY+5, outline='green', fill='black')

        b1 = Button(self.Frame1, text='Lancer', command=self.newGame)
        b1.grid(row=2, column=0)

        b2 = Button(self.Frame1, text='Menu', command= self.retour)
        b2.grid(row=2, column=2)

        tex1 = Label(self.Frame1, text="Cliquez sur 'New Game' pour commencer le jeu.")
        tex1.grid(row=2, column=1)

        self.TextGame = StringVar()
        LabelGame = Label(self.Frame1, textvariable = self.TextGame)
        self.TextGame.set("Score : "+ str(self.score))
        LabelGame.grid(row=0, column=1)

        self.master.bind('<d>', self.right)
        self.master.bind('<q>', self.left)
        self.master.bind('<z>' , self.up)
        self.master.bind('<s>', self.down)

    def move(self):
        self.can.delete('all')

        i = len(self.Serpent)-1
        j = 0
        while i > 0:
            self.Serpent[i][0]=self.Serpent[i-1][0]
            self.Serpent[i][1]=self.Serpent[i-1][1]
            self.can.create_oval(self.Serpent[i][0], self.Serpent[i][1], self.Serpent[i][0] +10, self.Serpent[i][1]+10,outline='green', fill='black')
            i=i-1

        self.can.create_rectangle(self.pX, self.pY, self.pX+5, self.pY+5, outline='green', fill='black')
        
        if self.direction  == 'gauche':
            self.Serpent[0][0]  = self.Serpent[0][0] - self.dx
            if self.Serpent[0][0] < 0:
                self.Serpent[0][0] = 493
        elif self.direction  == 'droite':
            self.Serpent[0][0]  = self.Serpent[0][0] + self.dx
            if self.Serpent[0][0] > 493:
                self.Serpent[0][0] = 0
        elif self.direction  == 'haut':
            self.Serpent[0][1]  = self.Serpent[0][1] - self.dy
            if self.Serpent[0][1] < 0:
                self.Serpent[0][1] = 493
        elif self.direction  == 'bas':
            self.Serpent[0][1]  = self.Serpent[0][1] +self.dy
            if self.Serpent[0][1] > 493:
                self.Serpent[0][1] = 0

        self.can.create_oval(self.Serpent[0][0], self.Serpent[0][1], self.Serpent[0][0]+10, self.Serpent[0][1]+10,outline='green', fill='blue')
        
        self.test()
        self.test()
        
        if self.flag != 0:
            self.master.after(60, self.move)

    def newGame(self):
        if self.flag == 0:
            self.flag = 1
        self.move()
        
    def test(self):
        if self.Serpent[1][0]> self.pX-7 and  self.Serpent[1][0]< self.pX+7:        
            if self.Serpent[1][1]> self.pY-7 and self.Serpent[1][1]< self.pY+7:
                self.pX = randrange(5, 495)
                self.pY = randrange(5, 495)
                self.can.coords(self.pomme,self.pX, self.pY, self.pX+5, self.pY+5)
                self.Serpent.append([0,0])

                self.score=self.score+1
                self.TextGame.set("Score : "+ str(self.score))

    def left(self, event):
        self.direction = 'gauche'
        
    def right(self, event):
        self.direction = 'droite'
        
    def up(self, event):
        self.direction = 'haut'
        
    def down(self, vent):
        self.direction = 'bas'

    def retour(self):
        self.Frame1.grid_forget()

        controller_menu.ControllerMenu().menu(self.master)
	   

