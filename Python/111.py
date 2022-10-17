import psutil

for pid in psutil.pids():
    p = psutil.Process(pid)
    print(p.name())