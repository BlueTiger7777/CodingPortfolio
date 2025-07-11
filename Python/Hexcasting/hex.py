# Imports
import numpy
import xml.etree.ElementTree as ET
from pyCosmicLib import tcolour as c

print(f'{c.BLINK}{c.RED}Test{c.ENDC}TEST')

# XML
tree = ET.parse("Patterns.xml")
root = tree.getroot()

x = input("> ").lower()
for child in root[0]:
    if x == child.attrib["name"].lower():
        print(child[4].text)
        break

# Vars
stack = [] # The iota stack, first in last out, [type, value]

# Funcs
# Gets iotas from the stack and checks if it is of the correct type called
def popStack(values):
    iotas = []
    for i in range(len(values)):
        iotas.append(stack[-1])
        stack.pop()
        if iotas[i][0] in values[len(values)-1-i] and type(values[len(values)-1-i]) is list or values[len(values)-1-i] == iotas[i][0] or values[len(values)-1-i] == "any":
            pass
        elif "list" in values[len(values)-1-i]:
            value = values[len(values)-1-i].replace("list ", "")
            for j in iotas[i][1]:
                if j[0] != value:
                    pushStack(iotas)
                    return "Type Missmatch"
        elif "many" in values[len(values)-1-i]:
            try:
                count = int(values[len(values)-1-i].replace("many ", ""))-1
                if count > len(stack):
                    pushStack(iotas)
                    return "Invalied Length"
                for j in range(count):
                    iotas.append(stack[-1])
                    stack.pop()
            except ValueError:
                for j in range(len(stack)):
                    iotas.append(stack[-1])
                    stack.pop()
        else:
            pushStack(iotas)
            return "Type Missmatch"
    return iotas

# Pushes iotas to the stack
def pushStack(iotas):
    for i in range(len(iotas)):
        stack.append(iotas[-1])
        iotas.pop()
        
# Patterns
# Base
def multiplicativeDistillation():
    iotas = popStack([["number", "vector"], ["number", "vector"]])
    if iotas == "Type Missmatch":
        return iotas
    elif iotas[0][0] == "number" and iotas[1][0] == "number":
        pushStack([["number", iotas[0][1]*iotas[1][1]]])
    elif iotas[0][0] == "vector" and iotas[1][0] == "vector":
        pushStack([["number", float(numpy.dot(iotas[0][1], iotas[1][1]))]])
    else:
        pushStack([["vector", numpy.ndarray.tolist(numpy.dot(iotas[0][1], iotas[1][1]))]])
        
def divisionDistillation():
    iotas = popStack([["number", "vector"], ["number", "vector"]])
    if iotas == "Type Missmatch":
        return iotas
    elif iotas[0][0] == "number" and iotas[1][0] == "number":
        pushStack([["number", iotas[1][1]/iotas[0][1]]])
    elif iotas[0][0] == "vector" and iotas[1][0] == "vector":
        pushStack([["vector", numpy.ndarray.tolist(numpy.cross(iotas[1][1], iotas[0][1]))]])
    elif iotas[0][0] == "number":
        pushStack([["vector", [round(iotas[1][1][0]/iotas[0][1], 2), round(iotas[1][1][1]/iotas[0][1], 2), round(iotas[1][1][2]/iotas[0][1], 2)]]])
    else:
        pushStack([["vector", [round(iotas[1][1]/iotas[0][1][0], 2), round(iotas[1][1]/iotas[0][1][1], 2), round(iotas[1][1]/iotas[0][1][2], 2)]]])

# Main
stack.append(["entity", "CosmicFire77"])
stack.append(["number", 0.0])
stack.append(["number", 1.0])
stack.append(["number", 2.0])
stack.append(["list", [["entity", "a"], ["number", 3.0], ["entity", "c"]]])
stack.append(["vector", [1.0, 2.0, 3.0]])
stack.append(["vector", [4.0, 5.0, 6.0]])
stack.append(["vector", [4.0, 5.0, 6.0]])
stack.append(["vector", [16.0, 32.0, 48.0]])
stack.append(["number", 8.0])


print(stack)
#print(popStack(["list entity", "any", "any", "vector"]))
multiplicativeDistillation()
#divisionDistillation()
print(stack)
