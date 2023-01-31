from app.model.model import Model
from app.classe.parametre import Parametre

class ParametreModel(Model):
    def __init__(self):
        table = "Parametre"
        Model.__init__(self, table)

    def get_all(self):
        Parametres = Model.get_all_data(self)

        tab_parametre = []

        for i in range(len(Parametres)):
            tab_parametre.append(Parametre(Parametres[i]))

        return tab_parametre