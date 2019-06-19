import xml.etree.ElementTree as ET
import xlwt
import tkinter.messagebox as messagebox

def xml_xls(file_path,file_name):
    tree = ET.parse(file_path)
    root = tree.getroot()

    workbook = xlwt.Workbook(encoding = 'utf-8')
    for i in root:
        if i.tag == 'text_table':
            worksheet = workbook.add_sheet('文字表')
        elif i.tag == 'compute_table':
            worksheet = workbook.add_sheet('计算表')
        elif i.tag == 'byte_table' :
            worksheet = workbook.add_sheet('标记示例表')
        else :
            pass
        if i.tag == 'text_table':
            worksheet.write(0, 0, label='标识')
            worksheet.write(0, 1, label='父级标识')
            worksheet.write(0, 2, label='章节号')
            worksheet.write(0, 3, label='名称')
            worksheet.write(0, 4, label='内容')
            worksheet.write(0, 5, label='标准号')
            worksheet.write(0, 6, label='链接编号')
            worksheet.write(1, 0, label='id')
            worksheet.write(1, 1, label='father_id')
            worksheet.write(1, 2, label='chapter')
            worksheet.write(1, 3, label='tag')
            worksheet.write(1, 4, label='value')
            worksheet.write(1, 5, label='std_no')
            worksheet.write(1, 6, label='link_no')
        elif i.tag == 'compute_table':
            worksheet.write(0, 0, label='标识')
            worksheet.write(0, 1, label='分类号')
            worksheet.write(0, 2, label='子分类号')
            worksheet.write(0, 3, label='输出字段')
            worksheet.write(0, 4, label='输入字段')
            worksheet.write(0, 5, label='输入值')
            worksheet.write(0, 6, label='输出值')
            worksheet.write(0, 7, label='标准号')
            worksheet.write(0, 8, label='链接编号')
            worksheet.write(0, 9, label='输出字段上标')
            worksheet.write(0, 10, label='输出字段下标')
            worksheet.write(0, 11, label='输入字段上标')
            worksheet.write(0, 12, label='输入字段下标')
            worksheet.write(0, 13, label='公差')
            worksheet.write(0, 14, label='输入字段单位')
            worksheet.write(0, 15, label='输出字段单位')
            worksheet.write(1, 0, label='id')
            worksheet.write(1, 1, label='sort_no')
            worksheet.write(1, 2, label='sub_sort_no')
            worksheet.write(1, 3, label='out_tag')
            worksheet.write(1, 4, label='in_tag')
            worksheet.write(1, 5, label='in_value')
            worksheet.write(1, 6, label='out_value')
            worksheet.write(1, 7, label='std_no')
            worksheet.write(1, 8, label='link_no')
            worksheet.write(1, 9, label='out_tag_upper')
            worksheet.write(1, 10, label='out_tag_lower')
            worksheet.write(1, 11, label='in_tag_upper')
            worksheet.write(1, 12, label='in_tag_lower')
            worksheet.write(1, 13, label='tolerance')
            worksheet.write(1, 14, label='in_tag_unit')
            worksheet.write(1, 15, label='out_tag_unit')
        elif i.tag == 'byte_table' :
            worksheet.write(0, 0, label='标识')
            worksheet.write(0, 1, label='父级标识')
            worksheet.write(0, 2, label='标记示例')
            worksheet.write(0, 3, label='字段数量')
            worksheet.write(0, 4, label='字段名称')
            worksheet.write(0, 5, label='字段值')
            worksheet.write(1, 0, label='id')
            worksheet.write(1, 1, label='father_id')
            worksheet.write(1, 2, label='tag_eg')
            worksheet.write(1, 3, label='tag_num')
            worksheet.write(1, 4, label='tag')
            worksheet.write(1, 5, label='value')
        else :
            pass
        index = 1
        for j in i:
            index+=1
            index1=0
            for ii in j:
                pass
                if 1:
                        if str(ii.text[-2:]) == '.0':
                            label = str(ii.text[:-2])
                        else:
                            label = str(ii.text)
                else:
                    label=ii.text
                if label == "null":
                    label=""
                worksheet.write(index, index1, label=label)
                index1+=1
        workbook.save(file_name+'.xls')
    messagebox.showinfo('Message', '完成')
