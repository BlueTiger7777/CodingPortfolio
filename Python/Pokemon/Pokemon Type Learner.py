import json
import random
from pprint import pprint
typeChart="C:\\Users\\alex\\OneDrive\\Documents\\Python\\Pokemon Type Matchup.json"
pmonChart="C:\\Users\\alex\\OneDrive\\Documents\\Python\\Pokemon Types.json"
types=['Normal','Fighting','Flying','Poison','Ground','Rock','Bug','Ghost','Steel','Fire','Water','Grass','Electric','Phychic','Ice','Dragon','Dark','Fairy']

with open(typeChart, "r") as f:
    chart=json.load(f)
"""#random type, may change random generation method, idk
a=random.choice(types)
d=random.choice(types)
print(a,d,chart['Type'][a][d])
"""
"""#Random mon, ran num 1-9 concatinated to gen for gen
m=random.randint(0,1)
print(chart['Gen1'][m]['Type1'])
"""

q=0
c=0
while True:
    d=random.choice(types)
    print("What type shoud be used against", d)
    a=input()
    q+=1
    if chart['Type'][a][d]=="Super Effective":
        print("Good Job")
        c+=1
    print("Score is:",c,"Out of",q)
