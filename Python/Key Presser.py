import keyboard
import time

while True:
    key=input("What key: ")
    presses=int(input("How many presses: "))
    print("Pressing in 3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    for i in range(presses):
        keyboard.press_and_release(key)
        time.sleep(0.1)
        
