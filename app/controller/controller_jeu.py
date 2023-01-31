from app.model.model_score import ScoreModel
from app.model.model_jeu import JeuModel

from app.view.jeu import View_jeu

class ControllerJeu():
    def __init__(self):
        self.model_score = ScoreModel()
        self.model_jeu = JeuModel()

    def jeu(self, master, id):
        score =  self.model_score.get(id)
        jeu = self.model_jeu.get(id)
        
        View_jeu(master, jeu, score)