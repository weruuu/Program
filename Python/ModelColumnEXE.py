from tkinter import *
import xml.etree.ElementTree as ET
import pyhdb
import xlwt
import tkinter.messagebox as messagebox

class Application(Frame):
    # 定义二维数组存放结果
    result = [[], [], [], []]
    result[0].append('输入节点')
    result[1].append('输出节点')
    result[2].append('输入字段')
    result[3].append('输出字段')

    #初始化app
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    #创建窗口
    def createWidgets(self):
        self.label1 = Label(self ,text = 'HANA Address')
        self.label1.pack()
        self.nameInputadd = Entry(self)
        self.nameInputadd.pack()
        self.label2 = Label(self, text='HANA Port')
        self.label2.pack()
        self.nameInputport = Entry(self)
        self.nameInputport.pack()
        self.label3 = Label(self, text='HANA User')
        self.label3.pack()
        self.nameInputuser = Entry(self)
        self.nameInputuser.pack()
        self.label4 = Label(self, text='User Password')
        self.label4.pack()
        self.nameInputpass = Entry(self)
        self.nameInputpass.pack()
        self.alertButton = Button(self, text='Test Connect', command=self.connect)
        self.alertButton.pack()
        self.label5 = Label(self, text='Package Name')
        self.label5.pack()
        self.nameInputpack = Entry(self)
        self.nameInputpack.pack()
        self.label6 = Label(self, text='Model Name')
        self.label6.pack()
        self.nameInputmodel = Entry(self)
        self.nameInputmodel.pack()
        self.alertButton = Button(self, text='Analytic', command=self.run)
        self.alertButton.pack()

    #定义连接
    def connect(self):
        try:
            self.connection = pyhdb.connect(
                host=self.nameInputadd.get(),
                port=self.nameInputport.get(),
                user=self.nameInputuser.get(),
                password=self.nameInputpass.get()
            )
        except TimeoutError as timeout:
            messagebox.showinfo('Message', '连接超时，请检查于服务器的通信连接是否正常')
        except pyhdb.exceptions.DatabaseError as connectionError:
            messagebox.showinfo('Message', '登陆失败，请检查用户名密码是否正确')
            raise
        messagebox.showinfo('Message', '连接成功!')
        self.connection.close()

    #用于返回连接变量
    def conn(self):
        self.connection = pyhdb.connect(
            host=self.nameInputadd.get(),
            port=self.nameInputport.get(),
            user=self.nameInputuser.get(),
            password=self.nameInputpass.get()
        )
        return self.connection

    #执行方法
    def run(self):
        cursor = self.conn().cursor()
        cursor.execute(
            'select cdata from _sys_repo.active_object where object_suffix like \'%view\' and package_id like \'%' + self.nameInputpack.get() + '%\' and object_name like \'' + self.nameInputmodel.get() + '\'')

        try:
            xmlfile = cursor.fetchone()[0].read(999999)
        except TypeError as NoResult:
            messagebox.showinfo('Message', '未获取到结果，请检查输入包路径和模型名称是否正确')
        fp = open("model.xml", "w", encoding='utf-8')  # 设置编码为utf-8避免windows系统出现乱码
        fp.write(xmlfile)
        fp.close()
        self.analytic()
        self.connection.close()

    # xml文件解析
    def analytic(self):
        tree = ET.parse('model.xml')
        root = tree.getiterator('calculationView')

        NodeList = []
        # 获取除顶层的下级节点清单
        for i in root:
            NodeList.append(i.attrib['id'])

        for NodeName in NodeList:
            # 检索DOM树id属性与节点清单匹配的节点
            for Element in root:
                if Element.attrib['id'] == NodeName:
                    InputNodes = Element.iter('input')
                    for InputNode in InputNodes:
                        # 获取符合条件的Mapping节点内容
                        mapping = InputNode.iter('mapping')
                        for maps in mapping:
                            if 'source' in maps.attrib:
                                self.result[0].append(InputNode.attrib['node'].replace('#', ''))
                                self.result[1].append(NodeName)
                                self.result[2].append(maps.attrib['source'])
                                self.result[3].append(maps.attrib['target'])

        # 获取顶层节点相关信息
        root = tree.getiterator('attribute')
        KeyMapping = tree.getiterator('keyMapping')
        InputNodeTop = tree.getiterator('logicalModel')[0].attrib['id']
        for TopNode, KeyMap in zip(root, KeyMapping):
            self.result[0].append(InputNodeTop)
            self.result[1].append('FinalNode')
            self.result[2].append(KeyMap.attrib['columnName'])
            self.result[3].append(TopNode.attrib['id'])

        # 将结果写入Excel
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet(self.nameInputmodel.get())
        for x in range(len(self.result)):
            for y in range(len(self.result[0])):
                worksheet.write(y, x, label=self.result[x][y])
        workbook.save('%s.xls' % (self.nameInputmodel.get()))
        messagebox.showinfo('Message', '执行成功，结果存放于同级目录下%s.xls文件中' % (self.nameInputmodel.get()))
app = Application()
# 设置窗口标题:
app.master.title('HANA Model Column Analytic')
# 主消息循环:
app.mainloop()