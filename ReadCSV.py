import csv
import StatFoot.CSaison
import StatFoot.CDivision
import StatFoot.Cmatch

saison = StatFoot.CSaison.CSaison()

def readCSV():

        division = StatFoot.CDivision.CDivision()
        with open('F1.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:

                #if line_count == 0:
                 #   print(f'Column names are {", ".join(row)}')

                if line_count>1:
                    match = StatFoot.Cmatch.Cmatch(row["FTHG"],row["FTAG"],row["HomeTeam"],row["AwayTeam"])
                    division.add_match(match)
                line_count += 1

        saison.add_division(division)



readCSV()

