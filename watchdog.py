import pyautogui
import win32process
import win32gui
import time
from playsound import playsound
def alertNow():
    while (True):
        playsound('alert.mp3')
        print('Alert! Change your fucking class NOW!')

print('Scanning ...')
while (True):
    if 'FPT' in win32gui.GetWindowText(win32gui.GetForegroundWindow()):
        alertPoint = 0
        pyautogui.press('F5')
        for x in range(2):
            time.sleep(2)
            pos = pyautogui.locateOnScreen('noCourse.png', confidence=0.85)
            if (pos == None and ('FPT' in win32gui.GetWindowText(win32gui.GetForegroundWindow()))):
                alertPoint = alertPoint+1
        if (alertPoint >= 2):
            alertNow()
