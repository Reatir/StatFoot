import pandas as pd

class stat(object):

    def ListEquipe(self,csv):
        listequipe = []
        for e in csv.HomeTeam.unique():
            listequipe.append(e)
        for e in csv.AwayTeam.unique():
            listequipe.append(e)
        df = pd.DataFrame(listequipe,columns=['A'])
        listequipe = df.A.unique()
        return listequipe

    def nb_match(self,csv,nom):

        list = csv.query('HomeTeam ==' +  "\"" + nom +"\"")
        lista = csv.query('AwayTeam ==' +  "\"" + nom +"\"")
        return 0
