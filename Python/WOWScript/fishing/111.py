import logging
import cv2
import pyscreenshot as ImageGrab
import numpy as np
import autopy
import pyautogui
from matplotlib import pyplot as plt

import pyaudio
import wave
import audioop
from collections import deque
import os
import time
import math
import psutil
# img = ImageGrab.grab(bbox =(0, 0, 1920, 1200))
# img.save('./1.png')
print(pyautogui.onScreen(1057, 379))
pyautogui.moveTo(1057, 379)
# cv2.imread('./var/1.png')
# for pid in psutil.pids():
#     p = psutil.Process(pid)
#     print(p.name())


# img_rgb = cv2.imread('./var/fishing_session.png')
# img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# template = cv2.imread('./var/fishing_float_0.png', 0)
# h, w = template.shape[:2]
#
# res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
# threshold = 0.9
# # 取匹配程度大于%80的坐标
# loc = np.where(res >= threshold)
# print(loc[::-1])
# # np.where返回的坐标值(x,y)是(h,w)，注意h,w的顺序
# for pt in zip(*loc[::-1]):
#     bottom_right = (pt[0] + w, pt[1] + h)
#     # print(bottom_right)
#     cv2.rectangle(img_rgb, pt, bottom_right, (0, 0, 255), 2)
#     # print(cv2.rectangle(img_rgb, pt, bottom_right, (0, 0, 255), 2))