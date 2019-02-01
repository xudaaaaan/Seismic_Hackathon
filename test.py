import json
import csv

with open("./Data/json/data50.json") as f:
	a = json.load(f)

#print(type(a)) #list
#print(len(a)) #50
#print(a[49]) #dictionary

with open("Data/FakeInfo.csv") as f:
	reader = csv.reader(f)
	b = list(reader)
print (list(zip(*b)))