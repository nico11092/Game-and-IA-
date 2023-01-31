from tkinter import *

from app.controller import controller_menu

class View_Pong():
    def __init__(self, master):
        self.master = master

        self.Frame1 = Frame(self.master, borderwidth=2, relief=GROOVE)
        self.Frame1.grid(row=0, column=0)

        self.PosX=60
        self.PosY=10
        self.PosX2=200
        self.PosY2=480
        self.dx=10
        self.dy=7
        self.score=0

        self.canvas = Canvas(self.Frame1,width = 500, height = 500 , bd=0, bg="grey")
        self.canvas.grid(row=0, column=0, columnspan=3)

        self.balle = self.canvas.create_oval(self.PosX,self.PosY,self.PosX+20,self.PosY+20,fill='white')
        self.raquette = self.canvas.create_rectangle(self.PosX2,self.PosY2,self.PosX2+100,self.PosY2+10,fill='black')

        self.TextGame = StringVar()
        LabelGame = Label(self.Frame1, textvariable = self.TextGame , bg ="grey")
        self.TextGame.set("Score : "+ str(self.score))
        LabelGame.grid(row=1, column=1)

        ButtonJouer = Button(self.Frame1, text ="Jouer", command=self.deplacement)
        ButtonJouer.grid(row=1, column=0)
        
        ButtonQuitter = Button(self.Frame1, text ="Menu", command= self.retour)
        ButtonQuitter.grid(row=1, column=2)

        self.Key = ''
        self.canvas.focus_set()
        self.canvas.bind('<Key>', self.KeyBoard)

    
    def KeyBoard(self, event):
        self.Key = event.keysym

    def deplacement(self):
        if self.canvas.coords(self.balle)[1]<0:
            self.dy=-1*self.dy
        if self.canvas.coords(self.balle)[2]>500:
            self.dx=-1*self.dx
        if self.canvas.coords(self.balle)[0]<0:
           self. dx=-1*self.dx
        if self.canvas.coords(self.balle)[3]>=self.PosY2 and self.canvas.coords(self.balle)[2]>=self.canvas.coords(self.raquette)[0] and self.canvas.coords(self.balle)[0]<=self.canvas.coords(self.raquette)[2] and self.canvas.coords(self.balle)[3]<=490:
            self.dy=-1*self.dy
            self.score=self.score+1
            self.TextGame.set("Score : "+ str(self.score))
        if self.canvas.coords(self.balle)[3]<550:
            self.master.after(10,self.deplacement)
        self.canvas.move(self.balle,self.dx,self.dy)
        
        if self.Key == 'Right':
            self.canvas.move(self.raquette,30,0)
        if self.Key == 'Left':
            self.canvas.move(self.raquette,-30,0)
        self.Key = ''

    def retour(self):
        self.Frame1.grid_forget()

        controller_menu.ControllerMenu().menu(self.master)