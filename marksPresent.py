import plotly.express as px
import csv
import numpy as np

def getDataSource(dataPath):
    marks = []
    days = []

    with open(dataPath) as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            days.append(float(row["Days"]))
            marks.append(float(row["Marks"]))

    return {"x":days, "y":marks}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print(correlation[0,1])

def setup():
    dataPath = "p106/marksPresent.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

setup()

#medium direct proportional