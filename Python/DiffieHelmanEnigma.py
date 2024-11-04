# An algorithum that uses the key of Diffie Helman as the seed to generate the random enigma settings

# Libs
import random
from pyenigma import enigma
from pyenigma import rotor
import string

# Funcs
# Checks if a number is a prime number
def isPrime(x):
    for i in range(2, x+1):
        y = x%i
        if y == 0 and i != x:
            return True
        elif i*2 > x or y == 0 and i == x:
            return False

# Generates a random number until it is a prime number
def genPrime():
    gen = True
    while gen:
        x=random.randrange(2, 1000000)
        gen = isPrime(x)
    return x
    
# Diffie Helman key generation
def diffieGen(P, G):
    a = genPrime()
    x = G**a%P
    print(f'Sent Key: {x}')
    y = int(input("Peer Generated Key: "))
    k = y**a%P
    return k
    
# Enigma settings generation
# 3 rotors, 3 rotor positions, reflector, 10 plugboard pairs (20)
def enigmaGen(k, out):
    random.seed(k)
    # Rotor gen
    rotors = []
    for i in range(1, 4):
        r = random.randrange(1, 9)
        if r == 1:
            rotors.append(rotor.ROTOR_I)
        elif r == 2:
            rotors.append(rotor.ROTOR_II)
        elif r == 3:
            rotors.append(rotor.ROTOR_III)
        elif r == 4:
            rotors.append(rotor.ROTOR_IV)
        elif r == 5:
            rotors.append(rotor.ROTOR_V)
        elif r == 6:
            rotors.append(rotor.ROTOR_VI)
        elif r == 7:
            rotors.append(rotor.ROTOR_VII)
        else:
            rotors.append(rotor.ROTOR_VIII)
    key = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
    r = random.randrange(1, 4)
    if r == 1:
        reflec = rotor.ROTOR_Reflector_A
    elif r == 2:
        reflec = rotor.ROTOR_Reflector_B
    else:
        reflec = rotor.ROTOR_Reflector_C
    freeLetters = string.ascii_uppercase
    plugs = ""
    for i in range(1, 11):
        l1 = random.choice(freeLetters)
        freeLetters = freeLetters.replace(l1, "")
        l2 = random.choice(freeLetters)
        freeLetters = freeLetters.replace(l2, "")
        plugs += l1 + l2
        if i != 10:
            plugs += " "
    engine = enigma.Enigma(reflec, rotors[0], rotors[1], rotors[2], key=key, plugs=plugs)
    if out:
        print(f'Machine Settings: {engine}\nPlugs: {plugs}')
    return engine


# Main
# print(genPrime())
k = diffieGen(567661, 9) #23 9
print(f'Shared Key: {k}')
engine = enigmaGen(k, True)

# Tanslate loop
while True:
    msg = input("\nMessage: ").upper()
    for i in msg:
    	if i not in string.ascii_uppercase:
    		msg = msg.replace(i, "")
    j = 0
    out = ""
    for i in msg:
    	j += 1
    	out += i
    	if j % 5 == 0:
    		out += " "
    print(f'Output: {engine.encipher(out)}')
    #engine = enigmaGen(k, False)
