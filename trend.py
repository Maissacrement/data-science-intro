import pandas as pnd
import numpy as np

def createTable(array, field1='NOTES'):
    return pnd.DataFrame({field1:np.array(array)})

def observate(feature):
    print("-- NOMBRE D’OBSERVATIONS --")
    return feature.count()

def min(feature):
    print ("\n-- MIN --")
    valeursTriees = feature.sort_values()
    valeursTriees = valeursTriees.reset_index(drop=True)
    print("Valeur minimale : "+str(valeursTriees[0]))

def max(feature):
    print ("\n-- MAX --")
    valeursTriees = feature.sort_values()
    valeursTriees = valeursTriees.reset_index(drop=True)
    print("Valeur maximale : " +
    str(valeursTriees[len(valeursTriees)-1]))

def main():
    myNote = [3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16]
    table = createTable(myNote);
    feature = observate(table)
    min(feature)
    max(feature)

main()
