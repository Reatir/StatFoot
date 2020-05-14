
import pandas as pd

class readcsv(object):

    def readCSV(self,path):

        csv = pd.read_csv(path,usecols=[0,1,2,3,4,5,6,7,8,9,10])
        return csv