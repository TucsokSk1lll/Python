from pyautogui import *
import pyautogui
import time
import win32api, win32con
from AppOpener import open
from AppOpener import open
import random

open("Google Chrome")
time.sleep(0.2)

#!= 255 or pyautogui.pixel(17,1007) [0] != 201 or pyautogui.pixel(17,1007) [1] != 100 or pyautogui.pixel(17,1007) [2] != 89

if pyautogui.pixel(1886,1000) [0] != 255 or pyautogui.pixel(1886,1000) [1] != 255 or pyautogui.pixel(1886,1000) [2]:
	pyautogui.keyDown('win')
	pyautogui.keyDown('up')
	time.sleep(0.1)
	pyautogui.keyUp('win')
	pyautogui.keyUp('up')
	sleep(0.1)
 
def press(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(0.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	time.sleep(0.5)
 
def type(text):
	for i in range(len(text)):
		pyautogui.keyDown(text[i])
		time.sleep(0.01)
		pyautogui.keyUp(text[i])

type('https://support.google.com/accounts/answer/27441?hl=en')

pyautogui.keyDown('Enter')
pyautogui.keyUp('Enter')
time.sleep(2)

press(250,580)

time.sleep(0.5)
type('Kalacskepu')

press(1100,666)

time.sleep(0.1)
press(820,540)

time.sleep(0.5)
type('1')

press(930,540)

press(930,570)

press(1100,550)

type('2000')

press(800,600)

press(800,666)

press(1100,700)

press(780,610)

win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
time.sleep(0.1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

type('Kalacskepu0001')

press(970,725)

type('Jelszo01')
pyautogui.keyDown('Enter')
pyautogui.keyUp('Enter')

type('Jelszo01')
pyautogui.keyDown('Enter')
pyautogui.keyUp('Enter')


