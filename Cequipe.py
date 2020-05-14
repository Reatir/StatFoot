import StatFoot.statEquipe as se
class equipe(object):

    name = ''
    nb_match = 0
    nb_but = 0

    def __init__(self,name_):
        self.name = name_

    def calcul_nb_match(self,csv):
        stat =se.stat()
        self.nb_match = stat.nb_match(csv,self.name)
