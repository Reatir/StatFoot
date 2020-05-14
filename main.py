import StatFoot.ReadCSV
import StatFoot.CDivision
import StatFoot.CSaison

saison = StatFoot.CSaison.CSaison()

reader = StatFoot.ReadCSV.readcsv()
division = reader.readCSV("F1.csv")
print("ok")