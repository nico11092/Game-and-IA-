from app.view.reglage import View_reglage
from app.model.model_parametre import ParametreModel

class ControllerReglage():
    def __init__(self):
        self.model_parametre = ParametreModel()

    def reglage(self, master):
        parametre = self.model_parametre.get_all()
        View_reglage(master, parametre[0])