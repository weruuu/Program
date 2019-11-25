# -*- coding: utf-8 -*-
import os
from tkinter import *

class Application(Frame):
#初始化app
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.label1 = Label(self, text='视频地址')
        self.label1.pack()
        self.urlInputadd = Entry(self)
        self.urlInputadd.pack()
        self.alertButton = Button(self, text='Download', command=self.run)
        self.alertButton.pack()

    def geturl(self):
        url = self.urlInputadd.get()
        return url
    def run(self):
        os.system('you-get ' + self.geturl())

app = Application()
# 设置窗口标题:
app.master.title('B站视频下载')
# 主消息循环:
app.mainloop()