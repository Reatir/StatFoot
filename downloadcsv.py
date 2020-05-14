import urllib.request
def downloadFile():
    url = "https://www.football-data.co.uk/mmz4281/1920/F1.csv"
    urllib.request.urlretrieve(url, "/Users/gabrieldesseresusini/Desktop/Gabe/Programming/Random_project/StatFoot/Fichier.csv")
downloadFile()
