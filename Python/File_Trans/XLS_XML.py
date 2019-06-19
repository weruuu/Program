import tkinter.messagebox as messagebox
import xlrd

from xml.etree import ElementTree as ET
from xml.dom.minidom import parse

def xls_xml(file_path,file_name):
    def read(file):
        try:
            data = xlrd.open_workbook(file)
            return data
        except IndentationError:
            print("读取失败")
    def writexml(data):

        index = 0
        names = locals()
        nrowsName = locals()
        Block = ET.Element("std_no")
        Block.text= file_name

        xx=0
        for block in data.sheet_names():
            nameB = block
            sheet = data.sheet_by_index(index)
            index =index +1
            names['block%d ' %index] = ET.SubElement(Block ,nameB)
            if xx==0:
                e1=ET.SubElement(Block,"text_table")
                e1.text = ""
                e=e1
            elif xx==1:
                e2=ET.SubElement(Block,"compute_table")
                e2.text = ""
                e=e2
            else:
                e3=ET.SubElement(Block,"byte_table")
                e3.text = ""
                e=e3
                pass
            xx+=1



            nrows = sheet.nrows
            nclos = sheet.ncols
            flag = 0

            for i in range(nrows):

                if flag!=0 and flag!=1:
                    if xx == 1:
                        nrowsName["nrow%d".format(i)] = ET.SubElement(e ,'text_block')
                    elif xx == 2:
                        nrowsName["nrow%d".format(i)] = ET.SubElement(e ,'func_block')
                    elif xx == 3:
                        nrowsName["nrow%d".format(i)] = ET.SubElement(e ,'byte_block')
                    index1 = 0


                    for j in range(nclos):
                        nn= ET.SubElement(nrowsName["nrow%d".format(i)], str(sheet.cell(1, j).value))
                        str0=str(sheet.cell(i, j).value)

                        if str0 is "":
                            str0 = "null"

                        if str(str0[-2:]) == '.0':
                            str0 = str(str0[:-2])
                        else:
                            str0 = str(str0)
                        # if index1==0 or index1==1:
                        #     try:
                        #         str0 = str(int(float(str0)))
                        #     except:
                        #
                        #         str0=str0
                        #         pass



                        index1 += 1
                        nn.text = str0

                flag+=1


        tree = ET.ElementTree(Block)

        tree.write("xx01.xml", encoding="utf-8")


    def build_sitemap():
        urlset = ET.Element("牛皮")  # 设置一个根节点，标签为urlset
        url = ET.SubElement(urlset, "牛")  # 在根节点urlset下建立子节点
        loc = ET.SubElement(url, '二牛')
        loc.text = "百度"
        lastmod = ET.SubElement(url, "三牛")
        lastmod.text = "2017-10-10"
        changefreq = ET.SubElement(url, "死牛")
        changefreq.text = "daily"
        priority = ET.SubElement(url, "五牛")
        priority.text = "1.0"
        tree = ET.ElementTree(urlset)
        tree.write("sitemap.xml", encoding="utf-8")

        pass


    def prettyXml(element, indent, newline, level=0):  # elemnt为传进来的Elment类，参数indent用于缩进，newline用于换行
        if element:  # 判断element是否有子元素
            if element.text == None or element.text.isspace():  # 如果element的text没有内容
                element.text = newline + indent * (level + 1)
            else:
                element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
        # else:  # 此处两行如果把注释去掉，Element的text也会另起一行
        # element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * level
        temp = list(element)  # 将elemnt转成list
        for subelement in temp:
            if temp.index(subelement) < (len(temp) - 1):  # 如果不是list的最后一个元素，说明下一个行是同级别元素的起始，缩进应一致
                subelement.tail = newline + indent * (level + 1)
            else:  # 如果是list的最后一个元素， 说明下一行是母元素的结束，缩进应该少一个
                subelement.tail = newline + indent * level
            prettyXml(subelement, indent, newline, level=level + 1)  # 对子元素进行递归操作


    # X.xlsx表名字
    data = read(file_path)
    # print(len(data.sheet_names()))
    #

    #
    # sheet1 = data.sheet_by_index(1)
    #
    # nrows = sheet1.nrows
    # ncols = sheet1.ncols
    # for i in range(0,nrows):
    #     for j in range(0,ncols):
    #         sheet1R = sheet1.cell(0,j).value
    #         print(sheet1R)
    writexml(data)

    tree = ET.parse("xx01.xml")
    root = tree.getroot()
    for delete_node in root.findall('文字表'):
        print(delete_node)
        root.remove(delete_node)
    for delete_node in root.findall('计算表'):
        root.remove(delete_node)
    for delete_node in root.findall('标记示例表'):
        root.remove(delete_node)
    tree.write("xx01.xml",encoding='utf-8')
    doc = parse("xx01.xml")
    f = open(file_name+'.xml', 'w' ,encoding='utf-8')
    doc.writexml(f, addindent='  ', newl='\n', encoding='utf-8')
    f.close()
    messagebox.showinfo('Message', '完成')