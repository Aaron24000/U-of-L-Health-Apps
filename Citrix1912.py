import os
import pyautogui
import time
import getpass
import tkinter
from tkinter import messagebox

os.startfile('C:\\Users\\Administrator\\Desktop\\Software\\new citrix LTSR 1912\\CitrixWorkspaceApp.exe')

time.sleep(10)

pyautogui.click(1087, 691)
pyautogui.click(740, 650)
pyautogui.click(1095, 691)
pyautogui.click(798, 526)
pyautogui.click(1091, 687)
time.sleep(60)
pyautogui.click(1161,690)
checkbox = messagebox.askyesno('Citrix 19.12', 'Would you like to restart now or later? Yes or no: ')

while True:
    no = False
    yes = True
    if checkbox == no:
        pyautogui.click(1105, 573)
        break
    elif checkbox == yes:
        pyautogui.click(1023, 576)
        break