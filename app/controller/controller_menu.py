from app.model.model_jeu import JeuModel

from app.view.menu import View_menu

class ControllerMenu():
    def __init__(self):
        self.model = JeuModel()

    def menu(self, master):
        jeux = self.model.get_all()

        View_menu(master, jeux)
