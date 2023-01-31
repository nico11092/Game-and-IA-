class Parametre:
    def __init__(self, tab):
        self.etat_clavier = tab[0]
        self.etat_cam = tab[1]

    def getEtat_Clavier(self):
        return self.etat_clavier

    def getEtat_Cam(self):
        return self.etat_cam

    def setEtat_Clavier(self, etat):
        self.etat_clavier = etat

    def setEtat_Cam(self, etat):
        self.etat_cam = etat