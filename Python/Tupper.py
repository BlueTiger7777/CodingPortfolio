import keyboard
import time

tupperName=input("Tupper bracket: ")

while True:
    input_string = input("Message: ")
    print("Message sending in 3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    for char in tupperName:
        keyboard.press_and_release(char)
    keyboard.press_and_release("shift+;")
    for char in input_string:
        keyboard.press_and_release(char)
    keyboard.press_and_release("enter")
