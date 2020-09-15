from pynput.keyboard import Key, Controller
keyboard = Controller()

for i in range(0,1000):
    keyboard.press(Key.space)
    keyboard.release(Key.space)
