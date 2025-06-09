# Imports
from RPi import GPIO
from time import sleep

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
    return [l1out, l2out]

# Main
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
            update = False
        sleep(0.1)
    lcd_string((str(players)+" selected"), Line1)
    lcd_string("Press Enter", Line2)
    playerHP = []
    for i in range(players):
        playerHP.append(2)
    while not(GPIO.input(btnE)):
        sleep(0.1)
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
        if update:
            hpStr = buckshotHP(playerHP, selected)
            lcd_string(hpStr[0], Line1)
            lcd_string(hpStr[1], Line2)
            update = False
        sleep(0.1)
finally:
    GPIO.cleanup()
