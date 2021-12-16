import pandas as pd
import itertools

#importing defs
from defs import heatmap, threeVenn, twoVenn,findPath


path  = findPath()
inputFile = input("Enter file path:")
selection = input("Select task:\n A) Heatmap\n B) Create all venn diagrams\n C) Create select venn diagrams\n")

if selection == "A":
    #creating heatmap
    df = pd.read_csv(inputFile, header=0)
    heatmap(df,path)

if selection == "B":
    dfvd = pd.read_csv(inputFile, header=0, index_col=0)

    #create all threeWay venns
    for subset in itertools.combinations(dfvd.columns.values, 3):
        list1 = list(subset)
        threeVenn(dfvd,path,list1)

    #create all twoWay venns
    for subset in itertools.combinations(dfvd.columns.values, 2):
        list2 = list(subset)
        twoVenn(dfvd,path,list2)

if selection == "C":
    list3 = []
    dfvd = pd.read_csv(inputFile, header=0, index_col=0)
    selection1 = "y"
    print(list(dfvd.columns.values))
    while True:
        selection1 = input("Please select columns for comparison. Input x to stop selection.")
        if selection1 == 'x':
            break
        list3.append(selection1)
        length = len(list3)

        if length == 3:
            threeVenn(dfvd,path,list3)

        if length == 2:
            twoVenn(dfvd,path,list3)