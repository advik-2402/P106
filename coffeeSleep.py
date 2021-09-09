import plotly.express as px
import csv
import numpy as np

def getDataSource(dataPath):
    sleep = []
    coffee = []

    with open(dataPath) as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            sleep.append(float(row["sleep"]))
            coffee.append(float(row["Coffee"]))

    return {"x":coffee, "y":sleep}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print(correlation[0,1])

def setup():
    dataPath = "p106/coffeeSleep.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

setup()

#high inversely proportional