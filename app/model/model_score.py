from app.model.model import Model
from app.classe.score import Score

class ScoreModel(Model):
    def __init__(self):
        table = "Score"
        Model.__init__(self, table)

    def get_all(self):
        Scores = Model.get_all_data(self)

        tab_Score = []

        for i in range(len(Scores)):
            tab_Score.append(Score(Scores[i]))

        return tab_Score

    def get(self, id):
        score = Model.get_score_data(self,id)

        return score