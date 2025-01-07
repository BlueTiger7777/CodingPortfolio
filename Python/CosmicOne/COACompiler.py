# Vars
raw = [] # Uncompiled program
com = [] # Compiled binary file
addr = 1023 # Current address
jmpAddr = 0 # The address to jump to
labels = [] # [<labelName>,<addr>]
binOut = [] # List of byte ints

# Funcs
# Decimal to binary
def dtb(num, numBits=8):
    num = int(num)
    return f'{num:0{numBits}b}'.format(num)

# Register name to register addr
def reg(register):
    register = int(register[1:])
    return '{0:04b}'.format(register)

# Main
# Loads the uncompiled file
with open("program.coa", "r") as f:
    raw = f.readlines()
    f.close()
for i in range(len(raw)):
    raw[i] = raw[i][:-1]
raw = raw[::-1]

# Finds all program labels
addr = len(raw)-1
for i in raw:
    line = i.split()
    if line[0][0] == ".":
        labels.append([line[0][1:], addr])
    addr -= 1

# Compiles the program
for i in raw:
    line = i.split()
    if line[0][0] == ".":
        command = line[1:]
    else:
        command = line[0:]
    match command[0]:
        # Psuedo commands
        # Another way to do a NOP
        ##case "NOP":
        ##    out = "0010" + reg("r0") + reg("r0") + reg("r0")
        case "INC":
            out = "1001" + reg(command[1]) + dtb(1)
        case "DEC":
            out = "1001" + reg(command[1]) + dtb(255)
        case "CMP":
            out = "0011" + reg(command[1]) + reg(command[2]) + reg("r0")
        case "NOT":
            out = "0100" + reg(command[1]) + reg("r0") + reg(command[2])
        # Instruction set commands
        case "NOP":
             out = dtb(0, 16)
        case "HLT":
            out = "0001" + dtb(0, 12)
        case "ADD":
            out = "0010" + reg(command[1]) + reg(command[2]) + reg(command[3])
        case "SUB":
            out = "0011" + reg(command[1]) + reg(command[2]) + reg(command[3])
        case "NOR":
            out = "0100" + reg(command[1]) + reg(command[2]) + reg(command[3])
        case "AND":
            out = "0101" + reg(command[1]) + reg(command[2]) + reg(command[3])
        case "XOR":
            out = "0110" + reg(command[1]) + reg(command[2]) + reg(command[3])
        case "RSH":
            out = "0111" + reg(command[1]) + dtb(0, 4) + reg(command[2])
        case "LDI":
            out = "1000" + reg(command[1]) + dtb(command[2])
        case "ADI":
            out = "1001" + reg(command[1]) + dtb(command[2])
        case "JMP":
            if command[1][0] == ".":
                for label in labels:
                    if label[0] == command[1][1:]:
                        jmpAddr = label[1]
                        break
            else:
                jmpAddr = command[1]
            out = "1010" + dtb(0, 2) + dtb(jmpAddr, 10)
        case "BRH":
            if command[2][0] == ".":
                for label in labels:
                    if label[0] == command[2][1:]:
                        jmpAddr = label[1]
                        break
            else:
                jmpAddr = command[1]
            match command[1]:
                case "Z":
                    cond = "00"
                case "!Z":
                    cond = "01"
                case "C":
                    cond = "10"
                case "!C":
                    cond = "11"
            out = "1011" + cond + dtb(jmpAddr, 10)
        case "CAL":
            for label in labels:
                if label[0] == command[1][1:]:
                    jmpAddr = label[1]
                    break
            out = "1100" + dtb(0, 2) + dtb(jmpAddr, 10)
        case "RET":
            out = "1101" + dtb(0, 12)
    com.insert(0, out)

# Creates a list of byte ints
for i in com:
    print(i)
    binOut.append(int(i[0:8],2))
    binOut.append(int(i[8:],2))

# Compiled output
with open("program.bin", "wb") as f: 
    f.write(bytes(bytearray(binOut)))
    f.close()

print("\nProgram compiled, a copy of the terminal output is found in `program.bin`")
