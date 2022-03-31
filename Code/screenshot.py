import pyautogui
import time
import webbrowser
# import pytesseract
import cv2
import glob
from matplotlib import pyplot as plt
import numpy as np


def openscreen(url):
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
    time.sleep(5)
    pyautogui.press('f')
    time.sleep(5)


def screenshot():
    im1 = pyautogui.screenshot(region=(0, 0, 966, 1070))
    im1.save("pictures/screenshot.png")
    cv2.waitKey(0)
