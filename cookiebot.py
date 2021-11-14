#!/usr/bin/python

import time
import threading
import pynput
import sys

from pynput import mouse,keyboard
from pynput.mouse import Controller, Button

time.sleep(1)
print("Starting in 5")
time.sleep(1)
print("Starting in 4")
time.sleep(1)
print("Starting in 3")
time.sleep(1)
print("Starting in 2")
time.sleep(1)
print("Starting in 1")
time.sleep(1)
print("Click Click Click Click Click...")
time.sleep(1)
print("Press ESC to exit")

a=False

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    global a
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        a=True
        return False

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
def listen():
    listener.join()

threading.Thread(target=listen).start()

mouse = Controller()

def func1():
    while True:
        if a:
            break
        mouse.click(Button.left)
        time.sleep(0.0007)

func1()
