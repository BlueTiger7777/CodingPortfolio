import keyboard
import datetime
t=datetime.datetime.now()
print(str(t)[:-7])
while str(t)[:-7] != "2025-01-01 00:00:00":
    t=datetime.datetime.now()
    print(t)
keyboard.press_and_release("shift+h")
keyboard.press_and_release("a")
keyboard.press_and_release("p")
keyboard.press_and_release("p")
keyboard.press_and_release("y")

keyboard.press_and_release("space")

keyboard.press_and_release("shift+n")
keyboard.press_and_release("e")
keyboard.press_and_release("w")

keyboard.press_and_release("space")

keyboard.press_and_release("shift+y")
keyboard.press_and_release("e")
keyboard.press_and_release("a")
keyboard.press_and_release("r")

keyboard.press_and_release("space")

keyboard.press_and_release("shift+@")
keyboard.press_and_release("e")
keyboard.press_and_release("v")
keyboard.press_and_release("e")
keyboard.press_and_release("r")
keyboard.press_and_release("y")
keyboard.press_and_release("o")
keyboard.press_and_release("n")
keyboard.press_and_release("e")

keyboard.press_and_release("enter")
keyboard.press_and_release("enter")
