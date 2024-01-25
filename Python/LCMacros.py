#Imports
import pyautogui
import keyboard

'''Misc macro stuff
#Coursor Pos
#print(pyautogui.position())

#Click
#pyautogui.click(x,y)

#Type
#pyautogui.typewrite("view monitor")
'''

print("Macros Running:\n-\tView Monitor\n=\tSwitch")
while True:
    if keyboard.read_key()=="-":
        pyautogui.press("backspace")
        pyautogui.typewrite("view monitor")
        pyautogui.press("enter")
        print("View Monitor")
        
    elif keyboard.read_key()=="=":
        pyautogui.press("backspace")
        pyautogui.typewrite("switch")
        pyautogui.press("enter")
        print("Switch")
