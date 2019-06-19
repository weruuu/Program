from ctypes import *
print(windll.kernel32)
print(cdll.msvcrt)
libc = cdll.msvcrt