# -*- coding: cp936 -*-
import win32api, win32gui, win32con  # ����win32api���ģ��
import win32gui
import time
hwnd_title = dict()
def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
win32gui.EnumWindows(get_all_hwnd, 0)
for h, t in hwnd_title.items():
    if t is not "":
        if t == 'ħ������' :
            hwnd = h
# send key
print(hwnd)
while (1) :
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x37, 0)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP,0x37, 0)
    time.sleep(0.1)
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x38, 0)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP,0x38, 0)
    time.sleep(0.3)
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x1B, 0)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP,0x1B, 0)
    time.sleep(0.3)