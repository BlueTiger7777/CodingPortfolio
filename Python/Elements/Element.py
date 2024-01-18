#Version 1

#Notes

#Imports
import random as r
import json
import os

#Const
fileFormat = ".json"

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
        fileName = fileLocation + fileName + fileFormat
        OpenSave = False
    else:
        print("That was not an option")


with open(fileName, 'r') as f:
    data = json.load(f)
    
#Func
#Function to call machines
def Machines():
	HCol()

#Hydroget collector
def HCol():
	x=round(r.random()*100,4)
	if x > 99.9855:
		print("Hydrogen - 2")
	else:
		print("Hydrogen - 1")

#Main
while True:
	print("Commands:\nTick <Tick amount, Defults 1>\nInventory")
	Command=input("Please select a command: ").lower()
	
	if Command[0:4]=="tick":
		if Command=="tick":
			Ticks=1
		else:
			Ticks=int(Command[5:])
		for i in range(0, Ticks):
			Machines()
	elif Command=="inventory":
		print("Stuff hear")
