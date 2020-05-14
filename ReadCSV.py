import csv
import StatFoot.CSaison
import StatFoot.CDivision
import StatFoot.Cmatch
import StatFoot.Cequipe
import pandas as pd

class readcsv(object):

    def readCSV(self,path):

        csv = pd.read_csv(path)
        

        return csv