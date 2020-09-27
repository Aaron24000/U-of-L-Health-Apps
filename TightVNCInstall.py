import os
import pyautogui
import getpass
from tkinter import messagebox

os.startfile("C:\\Users\\Administrator\\Desktop\\Software\\TightVNC (Win7)\\tightvnc-2.0.2-setup.exe")
pyautogui.moveTo((1065, 689), duration=2)
pyautogui.click()
pyautogui.click()
pyautogui.click()
pyautogui.click()
pyautogui.click()
checkbox = messagebox.askyesno('TightVNC', 'Is the set passwords box checked? yes or no:')

while True:
    no = False
    yes = True
    if checkbox == no:
        pyautogui.moveTo((749, 562), duration=2)
        pyautogui.click()
        pyautogui.moveTo(1073, 691)
        break
    elif checkbox == yes:
        print('Onto the passwords then!')
        pyautogui.click()
        pyautogui.moveTo(1073, 691)
        break

pyautogui.click()
pyautogui.moveTo((900, 457), duration=2)
pyautogui.click()
pyautogui.typewrite('helpme')
pyautogui.moveTo((900, 484), duration=2)
pyautogui.click()
pyautogui.typewrite('helpme')
pyautogui.moveTo((970, 548), duration=2)
pyautogui.click()
pyautogui.typewrite('helpme')
pyautogui.moveTo((970, 574), duration=2)
pyautogui.click()
pyautogui.typewrite('helpme')
pyautogui.moveTo((1072, 685), duration= 2)
pyautogui.click()
pyautogui.click(duration=20)
pyautogui.click()
pyautogui.click()
