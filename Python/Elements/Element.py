#Version 2

#Notes

#Imports
import random as r
import json
import os
import datetime as t

#Const
fileFormat = ".json"

newFileData={
	"elements": {
		"hydrogen-1": 0,
		"hydrogen-2": 0
	},
	"shop": {
		"lastUpdate": str(t.datetime.now())
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
	if t.datetime.strptime(str(t.datetime.now()-t.datetime.strptime(data["shop"]["lastUpdate"], '%Y-%m-%d %H:%M:%S.%f')),'%H:%M:%S.%f') > t.datetime.strptime("0:30:00.000000", '%H:%M:%S.%f'):
		print('idk')

#Hydroget collector
def HCol():
	x=round(r.random()*100,4)
	if x > 99.9855:
		print("Hydrogen - 2")
		data["elements"]["hydrogen-2"]+=1
		with open(fileName, 'r+') as f:
			f.write(json.dumps(data, indent=4))
	else:
		print("Hydrogen - 1")
		data["elements"]["hydrogen-1"]+=1
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
		print(data["elements"]["hydrogen-1"])
		for i in data["elements"]:
			print(f'{i.title()}: {data["elements"][i]}')
	elif Command=="shop":
		Shop()
		