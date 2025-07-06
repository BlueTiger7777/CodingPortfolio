# Imports
from RPi import GPIO
from time import sleep
import sys
import os

# Setup
os.system("clear")

# Chars 8x16
tw, th = os.get_terminal_size()
titleCen = (tw-100)/2+10

# Pins
btnL = 22
btnR = 27
btnE = 17

rs = 21
e = 20

d4 = 26
d5 = 19
d6 = 13
d7 = 6

# GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(btnL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btnR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btnE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(rs, GPIO.OUT)
GPIO.setup(e, GPIO.OUT)

GPIO.setup(d4, GPIO.OUT)
GPIO.setup(d5, GPIO.OUT)
GPIO.setup(d6, GPIO.OUT)
GPIO.setup(d7, GPIO.OUT)

# Classes
# Text and Background Colours
class tcolours:
    BLIN = '\33[5m'
    TRED = '\33[91m'
    TYEL = '\33[93m'
    BYEL = '\33[103m'
    ENDC = '\33[0m'

# Functions
# Display inisalisation
def lcd_int():
    lcd_byte(0x33, LCDCMD) # 110011 Int
    lcd_byte(0x32, LCDCMD) # 110010 Int
    lcd_byte(0x06, LCDCMD) # 000110 Cursor Move Direction
    lcd_byte(0x0c, LCDCMD) # 001100 Display On, Cursor Off, Blink Off
    lcd_byte(0x28, LCDCMD) # 101000 Data Length, Number of Lines, Font Size
    lcd_byte(0x01, LCDCMD) # 000001 Clear Display
    sleep(E_PULSEDELAY)

# Sends Byte to Data Pins
def lcd_byte(bits, mode): # Bits = Data, Mode = True for character, False for Command
    GPIO.output(rs, mode)
    # High Bits
    GPIO.output(d4, False)
    GPIO.output(d5, False)
    GPIO.output(d6, False)
    GPIO.output(d7, False)
    if bits&0x10==0x10:
        GPIO.output(d4, True)
    if bits&0x20==0x20:
        GPIO.output(d5, True)
    if bits&0x40==0x40:
        GPIO.output(d6, True)
    if bits&0x80==0x80:
        GPIO.output(d7, True)
    lcd_toggle_enable()
    # Low Bits
    GPIO.output(d4, False)
    GPIO.output(d5, False)
    GPIO.output(d6, False)
    GPIO.output(d7, False)
    if bits&0x01==0x01:
        GPIO.output(d4, True)
    if bits&0x02==0x02:
        GPIO.output(d5, True)
    if bits&0x04==0x04:
        GPIO.output(d6, True)
    if bits&0x08==0x08:
        GPIO.output(d7, True)
    lcd_toggle_enable()

# Toggle Enable
def lcd_toggle_enable():
    sleep(E_PULSEDELAY)
    GPIO.output(e, True)
    sleep(E_PULSEDELAY)
    GPIO.output(e, False)
    sleep(E_PULSEDELAY)

# Send String Data
def lcd_string(msg, line):
    msg = msg.ljust(LCDWidth," ")
    lcd_byte(line, LCDCMD)
    for i in range(LCDWidth):
        if msg[i] == "█":
            lcd_byte(255,LCDCHR)
        elif msg[i] == "→":
            lcd_byte(126,LCDCHR)
        elif msg[i] == "←":
            lcd_byte(127,LCDCHR)
        else:
            lcd_byte(ord(msg[i]),LCDCHR)

# Displays the HP of Players
def buckshotHP(hpList, turn):
    l1out = ""
    l2out = ""
    for i in range(len(hpList)):
        if hpList[i] == 2:
            hp = "██"
        elif hpList[i] == 1:
            hp = "█-"
        else:
            hp = "--"
        if i < 2:
            if turn == i:
                l1out += hp+"←"
            else:
                l1out += hp+" "
        elif i == 2:
            if turn == i:
                l1out += "→"+hp+"←"
            else:
                l1out += " "+hp+" "
        elif i > 2 and i < 5:
            if turn == i:
                l1out += "→"+hp
            else:
                l1out += " "+hp
        elif i > 4 and i < 7:
            if turn == i:
                l2out += hp+"←"
            else:
                l2out += hp+" "
        elif i == 7:
            if turn == i:
                l2out += "→"+hp+"←"
            else:
                l2out += " "+hp+" "
        else:
            if turn == i:
                l2out += "→"+hp
            else:
                l2out += " "+hp
        printHP(i, hpList[i], turn)
    return [l1out, l2out]

# Prints at a specified character position x = vertical, y = horizontal
def termPrint(x, y, text, reset=True):
    sys.stdout.write("\x1b8")
    if reset:
        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
        sys.stdout.flush()
    else:
        sys.stdout.write("\x1b7\x1b[%d;%df%s" % (x, y, text))

# Prints the buckshot title
def printTitle():
    with open("titleBuckshot.txt", "r") as f:
        lines = f.readlines()
        f.close()
    for i in range(len(lines)):
        termPrint(i+2, titleCen, f'\33[33m{lines[i]}{tcolours.ENDC}')

# Prints hp
def printHP(player, hp, turn):
    with open("hpBuckshot.txt", "r") as f:
        lines = f.readlines()
        f.close()
    with open("arrowLBuckshot.txt", "r") as f:
        arrowL = f.readlines()
        f.close()
    with open("arrowRBuckshot.txt", "r") as f:
        arrowR = f.readlines()
        f.close()
    # Line to begin on
    if player < 5:
        x = 2
    else:
        x = 22
    # Where on said line
    match player % 5:
        case 0:
            y = 2
        case 1:
            y = 29
        case 2:
            y = 56
        case 3:
            y = 83
        case 4:
            y = 110
    if turn == player:
        match player % 5:
            case 0:
                aly = 21
                ary = None
            case 1:
                aly = 48
                ary = 21
            case 2:
                aly = 75
                ary = 48
            case 3:
                aly = 102
                ary = 75
            case 4:
                aly = None
                ary = 102
        if aly != None:
            for i in range(len(arrowL)):
                termPrint(i+x, aly, f'{tcolours.BLIN}{arrowL[i]}{tcolours.ENDC}')
        if ary != None:
            for i in range(len(arrowR)):
                termPrint(i+x, ary, f'{tcolours.BLIN}{arrowR[i]}{tcolours.ENDC}')
    if hp >= 1:
        for i in range(len(lines)):
            termPrint(i+x, y, f'{tcolours.TYEL}{lines[i]}{tcolours.ENDC}')
    else:
        for i in range(len(lines)):
            if i == 7:
                termPrint(i+x, y, f'{tcolours.TRED}########{tcolours.ENDC}')
            else:
                termPrint(i+x, y, "        ")
    if hp == 2:
        for i in range(len(lines)):
            termPrint(i+x, y+10, f'{tcolours.TYEL}{lines[i]}{tcolours.ENDC}')
    else:
        for i in range(len(lines)):
            if i == 7:
                termPrint(i+x, y+10, f'{tcolours.TRED}########{tcolours.ENDC}')
            else:
                termPrint(i+x, y+10, "        ")

# Main
printTitle()
termPrint(30, 55, "Please Press Enter")

LCDWidth = 16
LCDCHR = True
LCDCMD = False
Line1 = 0x80
Line2 = 0xc0
E_PULSEDELAY = 0.0005

lcd_int()

lcd_string("Welcome to", Line1)
lcd_string("Buckshot IRL", Line2)

players = 2
update = False
selected = 0

try:
    while not(GPIO.input(btnE)):
        sleep(0.1)
    termPrint(30, 55, "  > Players:  2   ")
    lcd_string("Players: 2-10", Line1)
    lcd_string(str(players), Line2)
    while not(GPIO.input(btnE)):
        if GPIO.input(btnL):
            players -= 1
            update = True
        elif GPIO.input(btnR):
            players += 1
            update = True
        if players > 10:
            players = 10
        elif players < 2:
            players = 2
        if update:
            lcd_string(str(players), Line2)
            termPrint(30, 69, str(players)+" ")
            update = False
        sleep(0.1)
    lcd_string((str(players)+" selected"), Line1)
    lcd_string("Press Enter", Line2)
    termPrint(30, 54, " "+str(players)+" players selected")
    termPrint(31, 55, "Please Press Enter")
    playerHP = []
    for i in range(players):
        playerHP.append(2)
    while not(GPIO.input(btnE)):
        sleep(0.1)
    os.system("clear")
    hpStr = buckshotHP(playerHP, selected)
    lcd_string(hpStr[0], Line1)
    lcd_string(hpStr[1], Line2)
    while True:
        if GPIO.input(btnL):
            playerHP[selected] += 1
            if playerHP[selected] > 2:
                playerHP[selected] = 2
            else:
                update = True
        if GPIO.input(btnR):
            playerHP[selected] -= 1
            if playerHP[selected] < 0:
                playerHP[selected] = 0
            else:
                update = True
        if GPIO.input(btnE):
            selected += 1
            if selected == players:
                selected = 0
            update = True
            os.system("clear")
        if update:
            hpStr = buckshotHP(playerHP, selected)
            lcd_string(hpStr[0], Line1)
            lcd_string(hpStr[1], Line2)
            update = False
        sleep(0.1)
finally:
    GPIO.cleanup()
