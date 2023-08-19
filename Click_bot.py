import random 
from pyautogui import *
import pyautogui
import time
import win32api, win32con
from AppOpener import open
from AppOpener import open

#pyautogui.keyDown('shift')



while True:
	pyautogui.keyDown('shift')
	win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
	time.sleep(0.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
	pyautogui.keyUp('shift')
	time.sleep(0.1)
	