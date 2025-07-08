# Custom lib of functions and classes]
# Documentation on https://github/BlueTiger7777/CodingPortfolio/Python/pyCosmicLib
# Required imports
import os
import sys

# Classes
# Terminal Colours, names bassed off Win11 PowerShell (08/07/2025 18:44)
class tcolour:
    # Special
    ENDC = '\33[0m'
    GREY = '\33[2m'
    BLINK = '\33[5m'
    BLINK2 = '\33[6m'
    SELECTED = '\33[7m'
    TERM = '\33[8m'
    # Standard
    BOLD = '\33[1m'
    ITAL = '\33[3m'
    UNDERLINE = '\33[4m'
    UNDERLINE2 = '\33[21m'
    STRIKE = '\33[9m'
    # Text Colour (Dark)
    BLACK = '\33[30m'
    RED = '\33[31m'
    GREEN = '\33[32m'
    YELLOW = '\33[33m'
    BLUE = '\33[34m'
    PURPLE = '\33[35m'
    CYAN = '\33[36m'
    WHITE = '\33[37m'
    # Text Colour (Bright)
    BBLACK = '\33[90m'
    BRED = '\33[91m'
    BGREEN = '\33[92m'
    BYELLOW = '\33[93m'
    BBLUE = '\33[94m'
    BPURPLE = '\33[95m'
    BCYAN = '\33[96m'
    BWHITE = '\33[97m'
    # Background Colour (Dark)
    BLACKBG = '\33[40m'
    REDBG = '\33[41m'
    GREENBG = '\33[42m'
    YELLOWBG = '\33[43m'
    BLUEBG = '\33[44m'
    PURPLEBG = '\33[45m'
    CYANBG = '\33[46m'
    WHITEBG = '\33[47m'
    # Background Colour (Bright)
    BBLACKBG = '\33[100m'
    BREDBG = '\33[101m'
    BGREENBG = '\33[102m'
    BYELLOWBG = '\33[103m'
    BBLUEBG = '\33[104m'
    BPURPLEBG = '\33[105m'
    BCYANBG = '\33[106m'
    BWHITEBG = '\33[107m'

# Returns the position of verious points in the terminal (08/07/2025 18:53)
try:
    class anchor:
        TL = [0, 0]
        TC = [os.get_terminal_size()[0]/2, 0]
        TR = [os.get_terminal_size()[0], 0]
        CL = [0, os.get_terminal_size()[1]/2]
        CC = [os.get_terminal_size()[0]/2, os.get_terminal_size()[1]/2]
        CR = [os.get_terminal_size()[0], os.get_terminal_size()[1]/2]
        BL = [0, os.get_terminal_size()[1]]
        BC = [os.get_terminal_size()[0]/2, os.get_terminal_size()[1]]
        BR = [os.get_terminal_size()[0], os.get_terminal_size()[1]]
except:
    print("pyCosmicLib: Program did not run in the terminal, anchor class is unavaliable for this session")

# Misc funcs
# Finds all files with a file type and lets the user select one (08/07/2025 18:00)
def fileLoad(dirPath, fileFormat, createNew=False):
    files = []
    for file in os.listdir(dirPath): # Finds files in the location
        if file.endswith(fileFormat): # Filters thme for the wanted format
            print(file[:-len(fileFormat)])
            files.append(file) # Adds the file to the list
    while True:
        fileName = input("File to load: ") # Asks for the file to load
        if fileName + fileFormat in files: # Checks if it exists
            return ["exists", dirPath + fileName + fileFormat] # Returns its path and existance
        else:
            print("That was not an option")
            if createNew: # if createNew set asks if the file should be created
                option = input("Do you want to create a file with that name? y/n: ").lower()
                if option == "y":
                    return ["new", dirPath + fileName + fileFormat] # Returns the path and the inexistance of the file
                
# CLI Graphics funcs
# Prints to a location in the terminal (08/07/2025 18:11)
def termPrint(x, y, text, reset=True):
    sys.stdout.write("\x1b8")
    if reset:
        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (y, x, text)) # First arg is vertical second is horizontal
        sys.stdout.flush()
    else:
        sys.stdout.write("\x1b7\x1b[%d;%df%s" % (y, x, text))

# Sends lines in a text file to be printed to the screen (08/07/2025 19:06)
def printAsciiArt(filePath, x, y, txtFormat=''):
    with open(filePath, "r") as f:
        art = f.readlines()
        f.close()
    for i in range(len(art)):
        termPrint(i+y, x, f'{txtFormat}{art[i]}{tcolour.ENDC}')
