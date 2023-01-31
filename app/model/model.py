from app.config.database import Database

class Model:
    def __init__(self, table):
        self.table = table

        bd = Database()
        self.connexion = bd.getConnexion()

    def get_all_data(self):
        sql = "Select * from " + self.table

        lien = self.connexion.cursor()
        lien.execute(sql)

        result = lien.fetchall()

        return result

    def get_score_data(self,id):
        sql = "Select * from " + self.table + " where id_jeu = " + str(id)

        lien = self.connexion.cursor()
        lien.execute(sql)

        result = lien.fetchall()
        return result

    def get_data(self, id):
        sql = "Select * from " + self.table + " where id = " + str(id)

        lien = self.connexion.cursor()
        lien.execute(sql)

        result = lien.fetchall()

        return result