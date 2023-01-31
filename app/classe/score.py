class Score:
    def __init__(self, tab):
        self.id = tab[0][0]
        self.score = tab[0][1]
        self.id_jeu = tab[0][2]

    def getId(self):
        return self.id

    def getScore(self):
        return self.score

    def getId_jeu(self):
        return self.id_jeu

    def setId(self, id):
        self.id = id

    def setScore(self, score):
        self.score = score

    def setId_jeu(self, id_jeu):
        self.id_jeu = id_jeu

       
