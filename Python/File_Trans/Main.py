# _*_ coding:utf-8 _*_
import tkinter
from tkinter import filedialog
import XML_XLS
import XLS_XML
file_name = ''
file_path = ''
def openfiles2():
	xlsfname = filedialog.askopenfilename(title='打开Excel文件', filetypes=[('Excel', '*.xlsx'), ('All Files', '*')])
	file_path = xlsfname
	file_name = file_path[file_path.rindex('/')+1:file_path.index('.xlsx')]
	XLS_XML.xls_xml(file_path.replace('/','\\'),file_name)
def openfilecgns():
	xmlfname = filedialog.askopenfilename(title='打开XML文件',filetypes=[('XML', '*.xml'), ('All Files', '*')] )
	file_path = xmlfname
	file_name = file_path[file_path.rindex('/')+1:file_path.index('.xml')]
	print(file_path,file_name)
	XML_XLS.xml_xls(file_path.replace('/','\\'),file_name)

root = tkinter.Tk()
#root.geometry('500x300+500+200')
btn1 = tkinter.Button(root, text='打开Excel文件',font =("宋体",20,'bold'),width=13,height=8, command=openfiles2)
btn2 = tkinter.Button(root, text='打开XML文件',font = ('宋体',20,'bold'),width=13,height=8, command=openfilecgns)

btn1.pack(side='left')
btn2.pack(side='left')
root.mainloop()

