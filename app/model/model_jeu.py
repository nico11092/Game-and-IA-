from app.model.model import Model
from app.classe.jeu import Jeu

class JeuModel(Model):
    def __init__(self):
        table = "Jeu"
        Model.__init__(self, table)

    def get_all(self):
        Jeux = Model.get_all_data(self)

        tab_Jeux = []

        for i in range(len(Jeux)):
            tab_Jeux.append(Jeu(Jeux[i]))

        return tab_Jeux

    def get(self, id):
        jeu = Model.get_data(self, id)
  
        return jeu