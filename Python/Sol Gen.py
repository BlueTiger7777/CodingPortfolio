#Setup code
import random
BlackHoleLength = 3

#Options to output
SolOut = True
SunOut = False
PlanetOut = False
MoonPlanetOut = False
ShipOut = False
BlackHoleOut = False
AstroidFeildOut = False
GateWayOut = False
StationOut = False

#Prefixes for Sol Name
Letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SSNP1 = ['Razz', 'Syrinx', 'Celestal', 'Sadalsuud', 'Apolo', 'Kepler', 'Milky', 'Sulafat', 'Acubens', 'Sharcedon', 'Alula', 'Tranguli', 'Aerocia', 'Magna', 'Zoinks', 'Pherkad', 'Epingi', 'Ardentee', 'Menkib', 'Alphecca', 'Glados']
SSNP2 = ['Omega', 'Alpha', 'Bata', 'Prime', 'Rest', 'Mire', 'Legion', 'Way', 'Mass', 'Morass', 'Stream', 'Borealis', 'Rim', 'Veil', 'Precipice', 'Swarm']
Sun_Type = ['Red Dwarf', 'Brown Dwarf', 'White Dwarf', 'Subdwarf', 'Subgiant', 'Giant', 'Bright Giant', 'Supergiant', 'Hypergiant', 'Gentle', 'Tempearate', 'Radioactive', 'Frozen', 'Firey']
Planet_Type = ['Barren', 'Garden', 'Forest', 'Desert', 'Ocean', 'Savannah', 'Mutated', 'Toxic', 'Snow', 'Jungle', 'Artic', 'Midnight', 'Tundra', 'Decayed', 'Magma', 'Volcanic', 'Gas Giant']
Ship_Type = ['Friendly', 'Hostile']
Station = ['Yes', 'No']

#Code that genrates and prints result
while True:
    Planet_Num = random.randrange(3, 6)
    PI = 1

    #Genrates sol system name
    if SolOut == True:
        print("> Sol Name - ", random.choice(SSNP1), random.choice(SSNP2))

    #Genrates sun type
    if SunOut == True:
        print(" > Sun Type - ", random.choice(Sun_Type))

    #Genrates planets with a chance of a sub planet or moon
    if PlanetOut == True:
        while Planet_Num >= PI:
            print("  > Planet Type - ", random.choice(Planet_Type))
            MI = random.randrange(1, 3)

            #Will make a sub planet or moon if set to true
            if MoonPlanetOut == True:
                while MI == 1:
                    PRM = random.randrange(1, 3)
                    SI = random.randrange(1, 6)
                    if PRM == 1:
                        print("   > Moon")
                        MI = 0
                        MI2 = random.randrange(1, 11)
                    else:
                        print("   > Sub Planet Type - ", random.choice(Planet_Type))
                        MI = 0
                        MI2 = random.randrange(1, 11)

                    #Chance to have a second sub planet or moon
                    while MI2 == 1:
                        PRM2 = random.randrange(1, 3)
                        if PRM2 == 1:
                            print("   > Moon")
                            MI2 = 0
                            MI3 = random.randrange(1, 3)
                        else:
                            print("   > Sub Planet Type - ", random.choice(Planet_Type))
                            MI2 = 0
                            MI3 = random.randrange(1, 16)

                        #Chance to have a third sub planet or moon
                        while MI3 == 1:
                            PRM3 = random.randrange(1, 3)
                            if PRM3 == 1:
                                print("   > Moon")
                                MI3 = 0
                            else:
                                print("   > Sub Planet Type - ", random.choice(Planet_Type))
                                MI3 = 0

                    #Chance to have a ship orbiting the planet
                    if ShipOut == True:
                        if SI == 1:
                            print("   > Ship - ", random.choice(Ship_Type))
            PI += 1

    #Chance to generate a black hole
    if BlackHoleOut == True:
        BHI1 = random.randrange(1, 6)
        while BHI1 == 1:
                BHL1 = "".join(random.choice(Letter) for i in range(BlackHoleLength))
                BHN1 = "".join(random.choice(Number) for i in range(BlackHoleLength))
                print(" > ", BHL1, "-", BHN1)
                BHI1 = 0
                BHI2 = random.randrange(1, 11)

                #Chance to make a second black hole
                while BHI2 == 1:
                    BHL2 = "".join(random.choice(Letter) for i in range(BlackHoleLength))
                    BHN2 = "".join(random.choice(Number) for i in range(BlackHoleLength))
                    print(" > ", BHL2, "-", BHN2)
                    BHI2 = 0
                    BHI3 = random.randrange(1, 16)

                    #Chance to make a third black hole
                    while BHI3 == 1:
                        BHL3 = "".join(random.choice(Letter) for i in range(BlackHoleLength))
                        BHN3 = "".join(random.choice(Number) for i in range(BlackHoleLength))
                        print(" > ", BHL3, "-", BHN3)
                        BHI3 = 0

    #Chance to genrate a astroid feild
    if AstroidFeildOut == True:
        AFI = random.randrange(1, 10)
        while AFI == 1:
            print(" > Astroid Feild")
            AFI = 0

    #Chance to genrate a gateway
    if GateWayOut == True:
        GI = random.randrange(1,21)
        while GI == 1:
            print(" > Gateway")
            GI = 0

    #Chance to genrate a space station
    if StationOut == True:
        SI = random.randrange(1, 6)
        while SI == 1:
            print(" > Space Station - ", random.choice(Station))
            SI = 0

    input("> Press ENTER To Generate A New Sol System\n")
