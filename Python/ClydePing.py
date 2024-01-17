import keyboard
import time

time_wait=0.05
input_string = input('Enter the user ID: ')

print('Starting in 5 seconds...')
time.sleep(5)

while True:
    keyboard.press_and_release("shift+<")
    time.sleep(time_wait)
    keyboard.press_and_release("shift+@")
    time.sleep(time_wait)
    for char in input_string:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(time_wait)
    keyboard.press_and_release("shift+>")
    time.sleep(time_wait)
    keyboard.press_and_release("enter")
    time.sleep(0.25)
