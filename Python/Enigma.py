#Letters
L=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
i=0

#Rotors [[config],[turnover],[pos],[notch]]
I=[["E","K","M","F","L","G","D","Q","V","Z","N","T","O","W","Y","H","X","U","S","P","A","I","B","R","C","J"],["Q"]]
II=[["A","J","D","K","S","I","R","U","X","B","L","H","W","T","M","C","Q","G","Z","N","P","Y","F","V","O","E"],["E"]]
III=[["B","D","F","H","J","L","C","P","R","T","X","V","Z","N","Y","E","I","W","G","A","K","M","U","S","Q","O"],["V"]]
IV=[]
V=[]
VI=[]
VII=[]
VIII=[]

#Reflectors
UKWB=["Y","R","U","H","Q","S","L","D","P","X","N","G","O","K","M","I","E","B","F","Z","C","W","V","J","A","T"]
UKWC=[]

#Setup
print("Order of Operations:\nIn>Plugboard>R3>R2>R1>Reflector>R1>R2>R3>Plugboard>Out\n\nRotor Setup:")
#Rotors and Reflector
#Rotor 1
R1=input("Rotor 1 (I-VIII): ").upper()
R1Pos=input("Rotor 1 Position: ").upper()
R1Notch=input("Rotor 1 Notch: ").upper()

if R1 == "I":
    R1=I[0]
    i=L.index(R1Notch)
    for j in range (0,i):
        R1=R1[1:]+R1[:1]
elif R1 == "II":
    R1=II[0]
    i=L.index(R1Notch)
    for j in range (0,i):
        R1=R1[1:]+R1[:1]
elif R1 == "III":
    R1=III[0]
    i=L.index(R1Notch)
    for j in range (0,i):
        R1=R1[1:]+R1[:1]
elif R1 == "IV":
    R1=IV[0]
    i=L.index(R1Notch)
    for j in range (0,i):
        R1=R1[1:]+R1[:1]
elif R1 == "V":
    R1=V[0]
    i=L.index(R1Notch)
    for j in range (0,i):
        R1=R1[1:]+R1[:1]
elif R1 == "VI":
    R1=VI[0]
    i=L.index(R1Notch)
    for j in range (0,i):
        R1=R1[1:]+R1[:1]
elif R1 == "VII":
    R1=VII[0]
    i=L.index(R1Notch)
    for j in range (0,i):
        R1=R1[1:]+R1[:1]
elif R1 == "VIII":
    R1=VIII[0]
    i=L.index(R1Notch)
    for j in range (0,i):
        R1=R1[1:]+R1[:1]

#Rotor 2
R2=input("\nRotor 2 (I-VIII): ").upper()
R2Pos=input("Rotor 2 Position: ").upper()
R2Notch=input("Rotor 2 Notch: ").upper()

if R2 == "I":
    R2=I[0]
    i=L.index(R2Notch)
    for j in range (0,i):
        R2=R2[1:]+R2[:1]
elif R2 == "II":
    R2=II[0]
    i=L.index(R2Notch)
    for j in range (0,i):
        R2=R2[1:]+R2[:1]
elif R2 == "III":
    R2=III[0]
    i=L.index(R2Notch)
    for j in range (0,i):
        R2=R2[1:]+R2[:1]
elif R2 == "IV":
    R2=IV[0]
    i=L.index(R2Notch)
    for j in range (0,i):
        R2=R2[1:]+R2[:1]
elif R2 == "V":
    R2=V[0]
    i=L.index(R2Notch)
    for j in range (0,i):
        R2=R2[1:]+R2[:1]
elif R2 == "VI":
    R2=VI[0]
    i=L.index(R2Notch)
    for j in range (0,i):
        R2=R2[1:]+R2[:1]
elif R2 == "VII":
    R2=VII[0]
    i=L.index(R2Notch)
    for j in range (0,i):
        R2=R2[1:]+R2[:1]
elif R2 == "VIII":
    R2=VIII[0]
    i=L.index(R2Notch)
    for j in range (0,i):
        R2=R2[1:]+R2[:1]

#Rotor 3
R3=input("\nRotor 3 (I-VIII): ").upper()
R3Pos=input("Rotor 3 Position: ").upper()
R3Notch=input("Rotor 3 Notch: ").upper()

if R3 == "I":
    R3=I[0]
    i=L.index(R3Notch)
    for j in range (0,i):
        R3=R3[1:]+R3[:1]
elif R3 == "II":
    R3=II[0]
    i=L.index(R3Notch)
    for j in range (0,i):
        R3=R3[1:]+R3[:1]
elif R3 == "III":
    R3=III[0]
    i=L.index(R3Notch)
    for j in range (0,i):
        R3=R3[1:]+R3[:1]
elif R3 == "IV":
    R3=IV[0]
    i=L.index(R3Notch)
    for j in range (0,i):
        R3=R3[1:]+R3[:1]
elif R3 == "V":
    R3=V[0]
    i=L.index(R3Notch)
    for j in range (0,i):
        R3=R3[1:]+R3[:1]
elif R3 == "VI":
    R3=VI[0]
    i=L.index(R3Notch)
    for j in range (0,i):
        R3=R3[1:]+R3[:1]
elif R3 == "VII":
    R3=VII[0]
    i=L.index(R3Notch)
    for j in range (0,i):
        R3=R3[1:]+R3[:1]
elif R3 == "VIII":
    R3=VIII[0]
    i=L.index(R3Notch)
    for j in range (0,i):
        R3=R3[1:]+R3[:1]

#Reflector
Reflec=input("\nReflector (UKWB or UKWC): ").upper()
if Reflec == "UKWB":
    Reflec=UKWB
elif Reflec == "UKWC":
    Reflec=UKWC

print(f'\nSet Rotor 1 to {R1} at position {R1Pos} with notch at {R1Notch}\nSet Rotor 2 to {R2} at position {R2Pos} with notch at {R2Notch}\nSet Rotor 3 to {R3} at position {R3Pos} with notch at {R3Notch}\nUsing the reflector {Reflec}')

#Encodeing
TextOut=""
TextIn=input("\nPlain Text: ").upper()
for char in TextIn:
    if char == " ":
        break
    #Rotates rotors
    R3=R3[25:]+R3[:25]
    i=L.index(char)
    i=R3[i]
    print("Rotor 3:",i)
    i=L.index(i)
    i=R2[i]
    print("Rotor 2:",i)
    i=L.index(i)
    i=R1[i]
    print("Rotor 1:",i)
    i=L.index(i)
    i=Reflec[i]
    print("Reflector:",i)
    i=R1.index(i)
    i=L[i]
    print("Rotor 1:",i)
    i=R2.index(i)
    i=L[i]
    print("Rotor 2:",i)
    i=R3.index(i)+2
    i=R3[i]
    print("Rotor 3:",i)
    TextOut=TextOut+i

print(TextOut)
