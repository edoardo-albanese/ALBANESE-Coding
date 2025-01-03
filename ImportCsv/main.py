import csv
import os

elements = os.listdir("C:\Coding Projects\Python\ImportCsv")
print(elements)

path = elements[0]

with open(path, "r") as file:
    reader = csv.reader(file)
    print(reader)