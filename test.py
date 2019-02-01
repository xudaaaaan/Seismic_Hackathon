import json

with open("./Data/json/data50.json") as f:
	a = json.load(f)

print(type(a)) #list
print(len(a)) #50
print(a[49]) #dictionary