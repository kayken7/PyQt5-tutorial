import pyautogui
import time
import subprocess

subprocess.Popen(['notepad'])
time.sleep(1)
pyautogui.typewrite('Hello my friend!\n',0.1)
pyautogui.typewrite('This is an automated writing program.\n',0.1)
pyautogui.typewrite('I can do a lot of things, for instance\n',0.1)
pyautogui.typewrite('ctrl + a',0.1)
pyautogui.keyDown('ctrl');
pyautogui.press('a');
time.sleep(1)
pyautogui.keyUp('ctrl');
pyautogui.keyDown('ctrl');
pyautogui.press('x');
time.sleep(1)
pyautogui.keyUp('ctrl');
pyautogui.keyDown('ctrl');
pyautogui.press('v');
time.sleep(1)
pyautogui.keyUp('ctrl');
pyautogui.typewrite('\n\n That\'s it. Things like that.',0.1)

time.sleep(2)
pyautogui.click()
pyautogui.rightClick()
