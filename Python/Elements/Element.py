#Version 3

#Notes

#Imports
import random as r
import json
import os
import datetime as t

#Const
fileFormat = ".json"

newFileData={
	"items": [
		{
			"name": "Hydrogen-1",
			"count": 0,
			"baseValue": 100,
			"prevValue": 100,
			"curentValue": 100
		},
		{
			"name": "Hydrogen-2",
			"count": 0,
			"baseValue": 1000,
			"prevValue": 1000,
			"curentValue": 1000
		}
	],
	"shop": {
		"lastUpdate": str(t.datetime.now())[:-7]
	}
}

#File import
print("List of all saves")
Saves = []
for file in os.listdir(): #Finds all files in the folder
    if file.endswith(fileFormat): #For every file with the correct file format
        print(file[:-5]) #Prints the file name without the exstention
        Saves.append(file) #Adds the file to the list
OpenSave = True
while OpenSave == True:
    fileName = input("Save to open: ") #Askes for what save to open
    if fileName + fileFormat in Saves: #Checks to see if the input is a save in the folder
        fileName = fileName + fileFormat
        OpenSave = False
    else:
        print("That was not an option")
        option=input("Do you want to crete a save with that name? y/n: ")
        if option.lower() == "y":
            fileName = fileName + fileFormat
            with open(fileName, 'w') as f:
                json.dump(newFileData, f, indent=4)
                f.close()
                for file in os.listdir(): #Finds all files in the folder
                    if file.endswith(fileFormat): #For every file with the correct file format
                        print(file[:-5]) #Prints the file name without the exstention
                        Saves.append(file) #Adds the file to the list

with open(fileName, 'r') as f:
    data = json.load(f)
    
#Func
#Function to call machines
def Machines():
	HCol()

#Shop
def Shop():
	updateShop=True
	Time=t.datetime.strptime(data["shop"]["lastUpdate"], '%Y-%m-%d %H:%M:%S')
	while updateShop == True:
		if t.datetime.strptime(str(Time+t.timedelta(minutes=30)), '%Y-%m-%d %H:%M:%S') < t.datetime.now():
			Time=t.datetime.strptime(str(Time+t.timedelta(minutes=30)), '%Y-%m-%d %H:%M:%S')
			print(Time)
		else:
			data["shop"]["lastUpdate"]=str(Time)
			with open(fileName, '+r') as f:
				f.write(json.dumps(data, indent=4))
			updateShop=False

#Hydrogen collector
def HCol():
	x=round(r.random()*100,4)
	if x > 99.9855:
		el="Hydrogen-2"
	else:
		el="Hydrogen-1"

	for i in data["items"]:
		if i["name"] == el:
			i["count"]+=1
			with open(fileName, 'r+') as f:
				f.write(json.dumps(data, indent=4))

#Main
while True:
	print("Commands:\nTick <Tick amount, Defults 1>\nInventory\nShop")
	Command=input("Please select a command: ").lower()
	
	if Command[0:4]=="tick":
		if Command=="tick":
			Ticks=1
		else:
			Ticks=int(Command[5:])
		for i in range(0, Ticks):
			Machines()
	elif Command=="inventory":
		print("Elements: ")
		for i in data["items"]:
			print(f'{i["name"].title()}: {i["count"]}')
	elif Command=="shop":
		Shop()
		