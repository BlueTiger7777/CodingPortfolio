# An algorithum that uses the key of Diffie Helman as the seed to generate the random enigma settings

# Libs
import random
from pyenigma import enigma
from pyenigma import rotor
import string

# Constants
styled = True
reset = False
P = 8623961 #567661
G = 9
ranMax = 1000000 #10000000
rotorList = [
    rotor.ROTOR_I,
    rotor.ROTOR_II,
    rotor.ROTOR_III,
    rotor.ROTOR_IV,
    rotor.ROTOR_V,
    rotor.ROTOR_VI,
    rotor.ROTOR_VII,
    rotor.ROTOR_VIII
    ]
reflectors = [
    rotor.ROTOR_Reflector_A,
    rotor.ROTOR_Reflector_B,
    rotor.ROTOR_Reflector_C
    ]

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
        x=random.randrange(2, ranMax)
        gen = isPrime(x)
    #print(x)
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
    for i in range(0, 3):
        rotors.append(random.choice(rotorList))
        rotorList.remove(rotors[i])
    key = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
    ring = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
    reflec = random.choice(reflectors)
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
    engine = enigma.Enigma(reflec, rotors[0], rotors[1], rotors[2], key=key, plugs=plugs, ring=ring)
    if out:
        print(f'Machine Settings: {engine}\nPlugs: {plugs}')
    return engine


# Main
# print(genPrime())
k = diffieGen(P, G)
print(f'Shared Key: {k}')
engine = enigmaGen(k, True)

# Tanslate loop
while True:
    msg = input("\nMessage: ")
    if styled:
        msg = msg.upper()
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
    else:
        out = msg
    print(f'Output: {engine.encipher(out)}')
    if reset:
        engine = enigmaGen(k, False)
    
