## Version 1.0.0
import json
import os
from pprint import pprint
fileName="Oswin Fullthorn.json"
fileLocation = "C:\\Users\\alex\\OneDrive\\Documents\\DnD\\"
fileFormat = ".json"

newFileData={
    "inventory": {
        "equipment": [],
        "backpack": [],
        "coinPouch": []
        },
    "spells": {
        "spellbook": []
        },
    "character": {
        "persona": {
            "class": [],
            "race": {}
            },
        "stats": {
            "baseAbility": [],
            "saveingStats": [],
            "sences": [],
            "combat": [],
            "skills": []
            }
        }
    }

print("List of all character sheets")
Sheets = []
for file in os.listdir(fileLocation): #Finds all files in the folder
    if file.endswith(fileFormat): #For every file with the correct file format
        print(file[:-5]) #Prints the file name without the exstention
        Sheets.append(file) #Adds the file to the list
OpenSheet = True
while OpenSheet == True:
    fileName = input("Sheet to open: ") #Askes for what save to open
    if fileName + fileFormat in Sheets: #Checks to see if the input is a save in the folder
        fileName = fileLocation + fileName + fileFormat
        OpenSheet = False
    else:
        print("That was not an option")
        option=input("Do you want to crete a sheet with that name? y/n: ")
        if option.lower() == "y":
            fileName = fileLocation + fileName+fileFormat
            with open(fileName, 'w') as f:
                json.dump(newFileData, f, indent=4)
                f.close()
                for file in os.listdir(fileLocation): #Finds all files in the folder
                    if file.endswith(fileFormat): #For every file with the correct file format
                        print(file[:-5]) #Prints the file name without the exstention
                        Sheets.append(file) #Adds the file to the list
   
def Menu():
    with open(fileName, 'r+') as f:
        data = json.load(f)
    while True:
        print("\nInventory\nSpells\nCharacter")
        option = input("Option: ")
        if option.lower() == "inventory":
            Inventory(data)
        elif option.lower() == "spells":
            Spells(data)
        elif option.lower() == "character":
            Character(data)
        else:
            print("That's not an option")

def Inventory(data):
    while True:
        print("\nEquipment\nBackpack\nCoin Pouch")
        option = input("Option: ")
        if option.lower() == "equipment":
            InvEquipment(data)
        elif option.lower() == "backpack":
            InvBackpack(data)
        elif option.lower() == "coin pouch":
            InvCoinPouch(data)
        elif option.lower() == "back":
            return
        else:
            print("That's not an option")
            
def InvEquipment(data):
    while True:
        print("")
        for i in data['inventory']['equipment']:
            if i['quantity'] > 1:
                print(f'{i["quantity"]} {i["plural"]}')
            elif i['quantity'] == 1:
                print(f'{i["name"]}')
        option = input("Option: ")
        print("")
        if option.lower()[0:4] == "edit":
            for i in data['inventory']['equipment']:
                if option.lower()[5:] == str(i['name'].lower()):
                    if "details" in i:
                        option=input("Option to edit(name,quantity,weight,value,details,damage,damage type,attack bonus,enabled,charges,all): ").lower()
                        if option == "name":
                            i['name']=input("Name: ")
                        elif option == "quantity":
                            i['quantity']=int(input("Weight(int): "))
                        elif option == "weight":
                            i['weight']=float(input("Weight(float): "))
                        elif option == "value":
                            i['value']=float(input("Value(float): "))
                        elif option == "details":
                            i['details']=input("Details: ")
                        elif option == "damage":
                            i['damage']=input("Damage: ")
                        elif option == "damage type":
                            i['damageType']=input("Damage Type: ")
                        elif option == "attack bonus":
                            i['attackBonus']=input("Attack Bonus: ")
                        elif option == "enabled":
                            isEnabled=(input("Enabled(bool): "))
                            if isEnabled.lower() == "true":
                                i['enabled']=True
                            else:
                                i['enabled']=False
                        elif option == "charges":
                            i['charges']=input("Charges: ")
                        else:
                            i['name']=input("Name: ")
                            i['quantity']=int(input("Weight(int): "))
                            i['weight']=float(input("Weight(float): "))
                            i['value']=float(input("Value(float): "))
                            i['details']=input("Details: ")
                            i['damage']=input("Damage: ")
                            i['damageType']=input("Damage Type: ")
                            i['attackBonus']=input("Attack Bonus: ")
                            isEnabled=(input("Enabled(bool): "))
                            i['charges']=input("Charges: ")
                            if isEnabled.lower() == "true":
                                i['enabled']=True
                            else:
                                i['enabled']=False
                        out=json.dumps(data, indent=4)
                        with open(fileName, 'r+') as f:
                            f.write(out)
                    else:
                        option=input("Option to edit(name,quantity,weight,value,enabled,description,charges,all): ").lower()
                        if option == "name":
                            i['name']=input("Name: ")
                        elif option == "quantity":
                            i['quantity']=int(input("Weight(int): "))
                        elif option == "weight":
                            i['weight']=float(input("Weight(float): "))
                        elif option == "value":
                            i['value']=float(input("Value(float): "))
                        elif option == "enabled":
                            isEnabled=(input("Enabled(bool): "))
                            if isEnabled.lower() == "true":
                                i['enabled']=True
                            else:
                                i['enabled']=False
                        elif option == "description":
                            i['description']=input("Description: ")
                        elif option == "charges":
                            i['charges']=input("Charges: ")
                        else:
                            i['name']=input("Name: ")
                            i['quantity']=int(input("Weight(int): "))
                            i['weight']=float(input("Weight(float): "))
                            i['value']=float(input("Value(float): "))
                            isEnabled=(input("Enabled(bool): "))
                            i['description']=input("Description: ")
                            i['charges']=input("Charges: ")
                            if isEnabled.lower() == "true":
                                i['enabled']=True
                            else:
                                i['enabled']=False
                        out=json.dumps(data, indent=4)
                        with open(fileName, 'r+') as f:
                            f.write(out)
        if option.lower()[0:6] == "create":
            if option.lower()[7:] == "weapon":
                new={"name": "nul", "quantity": 1, "weight": "nul", "value": "nul", "details": "nul", "damage": "nul", "damageType": "nul", "attackBonus": "nul", "enabled": "nul", "charges": "nul"}
                data['inventory']['equipment'].append(new)
                out=json.dumps(data, indent=4)
                with open(fileName, 'r+') as f:
                            f.write(out)
            else:
                new={"name": "nul", "quantity": 1, "weight": "nul", "value": "nul", "enabled": "nul", "description": "nul", "charges": "nul"}
                data['inventory']['equipment'].append(new)
                out=json.dumps(data, indent=4)
                with open(fileName, 'r+') as f:
                            f.write(out)
        else:
            for i in data['inventory']['equipment']:
                if option.lower() == str(i['name']).lower():
                    if "details" in i:
                        print(f'{i["name"]}:\n Weight: {i["weight"]}\n Value: {i["value"]}\n Details: {i["details"]}\n Damage: {i["damage"]}\n Damage Type: {i["damageType"]}\n Attack Bonus: {i["attackBonus"]}\n Enabled: {i["enabled"]}')
                    else:
                        print(f'{i["name"]}:\n Weight: {i["weight"]}\n Value: {i["value"]}\n Enabled: {i["enabled"]}\n Description: {i["description"]}')
                elif option.lower() == "back":
                    return

def InvBackpack(data):
    while True:
        print("")
        for i in data['inventory']['backpack']:
            if i['quantity'] > 1:
                print(f'{i["quantity"]} {i["plural"]}')
            elif i['quantity'] == 1:
                print(f'{i["name"]}')
        option = input("Option: ")
        print("")
        for i in data['inventory']['backpack']:
            if option.lower() == str(i['name']).lower() or option.lower() == str(i['plural']).lower():
                if "details" in i:
                    print(f'{i["name"]}:\n Weight: {i["weight"]}\n Value: {i["value"]}\n Details: {i["details"]}\n Damage: {i["damage"]}\n Damage Type: {i["damageType"]}\n Attack Bonus:{i["attackBonus"]}\n Enabled: {i["enabled"]}')
                else:
                    print(f'{i["name"]}:\n Plural: {i["plural"]}\n Quantity: {i["quantity"]}\n Weight: {i["weight"]}\n Value: {i["value"]}\n Enabled: {i["enabled"]}\n Description: {i["description"]}')
            elif option.lower() == "back":
                return
                    
def InvCoinPouch(data):
    while True:
        print("")
        for i in data['inventory']['coinPouch']:
            if i['quantity'] > 1:
                print(f'{i["quantity"]} {i["plural"]}')
            elif i['quantity'] == 1:
                print(f'{i["name"]}')
        option = input("Option: ")
        print("")
        for i in data['inventory']['coinPouch']:
            if option.lower() == str(i['name']).lower() or option.lower() == str(i['plural']).lower():
                print(f'{i["name"]}:\n {i["plural"]}\n {i["quantity"]}\n {i["weight"]}\n {i["value"]}')
            elif option.lower() == "back":
                return

def Spells(data):
    while True:
        print("\nPrepared\nUnprepared")
        option = input("Option: ")
        if option.lower() == "prepared":
            SpePreped(data)
        elif option.lower() == "unprepared":
            SpeUnpreped(data)
        elif option.lower() == "back":
            return
        else:
            print("That's not an option")

def SpePreped(data):
    while True:
        print("")
        for i in data['spells']['spellbook']:
            if i['prepared'] == True:
                print(f'{i["name"]}')
        option = input("Option: ")
        print("")
        for i in data['spells']['spellbook']:
            if option.lower() == str(i['name']).lower() and i['prepared'] == True:
                if "details" in i:
                    print(f'Name: {i["name"]}:\n Level: {i["level"]}\n Class: {i["class"]}\n School: {i["school"]}\n Ritual: {i["ritual"]}\n Cast Time: {i["castTime"]}\n Range: {i["range"]}\n Verbal: {i["verbal"]}\n Somatic: {i["somatic"]}\n Concentration: {i["concentration"]}\n Material: {i["material"]}\n Duration: {i["duration"]}\n Description: {i["description"]}\n Details: {i["details"]}\n Damage: {i["damage"]}\n Damage Type: {i["damageType"]}\n Attack Bonus: {i["attackBonus"]}\n Prepared: {i["prepared"]}')
                else:
                    print(f'Name: {i["name"]}:\n Level: {i["level"]}\n Class: {i["class"]}\n School: {i["school"]}\n Ritual: {i["ritual"]}\n Cast Time: {i["castTime"]}\n Range: {i["range"]}\n Verbal: {i["verbal"]}\n Somatic: {i["somatic"]}\n Concentration: {i["concentration"]}\n Material: {i["material"]}\n Duration: {i["duration"]}\n Description: {i["description"]}\n Prepared: {i["prepared"]}')
            elif option.lower() == "back":
                return

def SpeUnpreped(data):
    while True:
        print("")
        for i in data['spells']['spellbook']:
            if i['prepared'] == False:
                print(f'{i["name"]}')
        option = input("Option: ")
        print("")
        for i in data['spells']['spellbook']:
            if option.lower() == str(i['name']).lower() and i['prepared'] == False:
                if "details" in i:
                    print(f'Name: {i["name"]}:\n Level: {i["level"]}\n Class: {i["class"]}\n School: {i["school"]}\n Ritual: {i["ritual"]}\n Cast Time: {i["castTime"]}\n Range: {i["range"]}\n Verbal: {i["verbal"]}\n Somatic: {i["somatic"]}\n Concentration: {i["concentration"]}\n Material: {i["material"]}\n Duration: {i["duration"]}\n Description: {i["description"]}\n Details: {i["details"]}\n Damage: {i["damage"]}\n Damage Type: {i["damageType"]}\n Attack Bonus: {i["attackBonus"]}\n Prepared: {i["prepared"]}')
                else:
                    print(f'Name: {i["name"]}:\n Level: {i["level"]}\n Class: {i["class"]}\n School: {i["school"]}\n Ritual: {i["ritual"]}\n Cast Time: {i["castTime"]}\n Range: {i["range"]}\n Verbal: {i["verbal"]}\n Somatic: {i["somatic"]}\n Concentration: {i["concentration"]}\n Material: {i["material"]}\n Duration: {i["duration"]}\n Description: {i["description"]}\n Prepared: {i["prepared"]}')
            elif option.lower() == "back":
                return

def Character(data):
    while True:
        print("\nPersona\nStats")
        option = input("Option: ")
        if option.lower() == "persona":
            ChaPersona(data)
        elif option.lower() == "stats":
            ChaStats(data)
        elif option.lower() == "back":
            return
        else:
            print("That's not and option")

def ChaPersona(data):
    while True:
        print("\nClass\nRace")
        option = input("Option: ")
        if option.lower() == "class":
            ChaPerClass(data)
        elif option.lower() == "race":
            ChaPerRace(data)
        elif option.lower() == "back":
            return
        else:
            print("That's not an option")

def ChaPerClass(data):
    while True:
        print("")
        for i in data['character']['persona']['class']:
            print(f'Class: {i["name"]}\n Level: {i["level"]}')
        option = input("Option: ")
        print("")
        for i in data['character']['persona']['class']:
            if option.lower() == str(i['name']).lower():
                print(f'Name: {i["name"]}\n Level: {i["level"]}\n Spellcaster: {i["spellcaster"]}\n Languages: {i["languages"]}\n Proficiencies: {i["proficiencies"]}\n Extra: {i["extra"]}')
            elif option.lower() == "back":
                return

def ChaPerRace(data):
    print("")
    print(f'Race: {data["character"]["persona"]["race"]["race"]}\nGender: {data["character"]["persona"]["race"]["gender"]}\nLanguages: {data["character"]["persona"]["race"]["languages"]}')
    return

def ChaStats(data):
    while True:
        print("\nAbility\nSaving\nSences\nCombat\nDefenses\nConditions\nSkills")
        option = input("Option: ")
        if option.lower() == "ability":
            ChaStaAbility(data)
        elif option.lower() == "saving":
            ChaStaSaving(data)
        elif option.lower() == "sences":
            ChaStaSences(data)
        elif option.lower() == "combat":
            ChaStaCombat(data)
        elif option.lower() == "defenses":
            ChaStaDefenses(data)
        elif option.lower() == "conditions":
            ChaStaConditions(data)
        elif option.lower() == "skills":
            ChaStaSkills(data)
        elif option.lower() == "back":
            return
        else:
            print("That's not an option")

def ChaStaAbility(data):
    while True:
        print("")
        for i in data['character']['stats']['baseAbility']:
            print(f'Ability: {i["ability"]} - {i["score"]}')
        option = input("Option: ")
        print("")
        for i in data['character']['stats']['baseAbility']:
            if option.lower() == str(i['ability']).lower():
                print(f'Ability: {i["ability"]}\n Score: {i["score"]}\n Mod {i["mod"]}')
            elif option.lower() == "back":
                return

def ChaStaSaving(data):
    print("")
    for i in data['character']['stats']['savingStats']:
        print(f'Save: {i["name"]}\n Score: {i["score"]}\n Proficient: {i["proficient"]}')
    return

def ChaStaSences(data):
    print("")
    for i in data['character']['stats']['sences']:
        print(f'Sence: {i["sence"]} - {i["mod"]}')
    return

def ChaStaCombat(data):
    print("")
    for i in data['character']['stats']['combat']:
        if str(i['name']) == "Defenses" or str(i['name']) == "Conditions":
            pass
        else:
            print(f'{i["name"]} - {i["value"]}')
    return

def ChaStaDefenses(data):
    print("")
    for i in data['character']['stats']['combat'][7]['value']:
        print(f'Name: {i["name"]}\n Defense: {i["description"]}')
    return

def ChaStaConditions(data):
    print("")
    for i in data['character']['stats']['combat'][8]['value']:
        print(f'Name: {i["name"]}\n Defense: {i["description"]}')
    return

def ChaStaSkills(data):
    while True:
        print("")
        for i in data['character']['stats']['skills']:    
            print(f'Name: {i["name"]}')
        option = input("Option: ")
        print("")
        for i in data['character']['stats']['skills']:
            if option.lower() == str(i['name']).lower():
                print(f'Skill: {i["name"]}\n Stat: {i["stat"]}\n Bonus: {i["bonus"]}\n Advantage: {i["advantage"]}\n Proficient {i["proficient"]}')
            elif option.lower() == "back":
                return

while True:
    Menu()
