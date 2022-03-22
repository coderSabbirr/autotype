import pyautogui
import time
message = 50
# while True:
#     time.sleep(3)
#     pyautogui.typewrite('i miss you.')
#     time.sleep(2)
#     pyautogui.press('enter')

while message > 0:
    time.sleep(0.3)
    pyautogui.typewrite('i need you')
    pyautogui.press('enter')
    message = message - 1