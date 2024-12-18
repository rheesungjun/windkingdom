import pyautogui
import easyocr
import numpy as np
import cv2

# pyautogui.moveTo(1133,910,duration=1)
# pyautogui.moveTo(1284,928,duration=1)

x,y,w,h=1133,910,1284-1133,928-910

screenshot = pyautogui.screenshot('test.png',region=(x,y,w,h))
screenshot_np = np.array(screenshot)
reader = easyocr.Reader(['ko','en'])
results= reader.readtext(screenshot_np)
cv2.imwrite('test_cv4.png', screenshot_np)
# _,text,_=results[0]
# print(text)
print(results)