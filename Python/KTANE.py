#Module Setup
import random as r

#Variable Setup
serialLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Z"]
serialNumbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
indicators = ["SND", "CLR", "CAR", "IND", "FRQ", "SIG", "NSA", "MSA", "TRN", "BOB", "FRK"]
ports = ["DVI-D", "Parallel", "PS/2", "RJ-45", "Serial", "Stereo RCA"]
batteries = ["AA", "D"]
modual=r.randrange(1, 2)

#Serial Number Generation
serial = ""
serialLetPos = r.randrange (1, 6)
for i in range(1, 6):
    if i == serialLetPos:
        serial+=r.choice(serialLetters)
    else:
        x=r.randrange(1, 3)
        if x == 1:
            serial+=r.choice(serialLetters)
        else:
            serial+=r.choice(serialNumbers)
serial+=r.choice(serialNumbers)
x=None
serialLetPos=None
print(serial)

#Modual Stuff
match modual:
    #Wires
    case 1:
        print("Wires")
        wireNum=r.randrange(3,4)
        wireColours = ["Yellow", "Red", "Blue", "Black", "White"]
        wires = []
        match wireNum:
            case 3:
                for i in range(0,wireNum):
                    wires.append(r.choice(wireColours))

                if "Red" in wires == False:
                    ans=1
                elif wires[2] == "White":
                    ans=2
                elif wires.count("Blue") > 1:
                    ans=next(i for i in reversed(range(len(wires))) if wires[i] == "Blue")
                else:
                    ans=2
                
                print(f'Three Wires\n{wires[0]}, {wires[1]}, {wires[2]}')
                x=int(input("Wire index to cut: "))

                if x == ans:
                    print("Good Job")
                else:
                    print("Strike")
            case 4:
                print("Four Wires")
            case 5:
                print("Five Wires")
            case 6:
                print("Six Wires")

    #Button
    case 2:
        print("Button")

    #Keypad
    case 3:
        print("Keypad")

    #Simon Says
    case 4:
        print("Simon Says")

    #Who's First
    case 5:
        print("Who's First")

    #Memory
    case 6:
        print("Memory")

    #Morse
    case 7:
        print("Morse")

    #Complicated Wires
    case 8:
        print("Complicated Wires")

    #Wire Sequences
    case 9:
        print("Wire Sequences")

    #Mazes
    case 10:
        print("Mazes")

    #Password
    case 11:
        print("Password")
