class Jeu:
    def __init__(self, tab):
        self.id = tab[0]
        self.nom = tab[1]

    def getId(self):
        return self.id
    
    def getNom(self):
        return self.nom

    def setId(self, id):
        self.id = id
    
    def setNom(self, nom):
        self.nom = nom