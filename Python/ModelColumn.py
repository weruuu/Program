import GetHanaXML
import xml.etree.ElementTree as ET

PackageName = input('输入模型包路径(非必输)：\n')
ModelName = input('输入模型名称：\n')
GetHanaXML.writefile(PackageName,ModelName)
ls_sourse = []
ls_result = []
ls_node = []
#获取DOM树
tree = ET.parse('model.xml')
root = tree.getroot()

#属性视图
def att_view():
    # 查找DOM中名称为attribute的tag
    for sourse in root.iter('attribute'):
        #查找的结果为dict类型，通过索引输出结果
        ls_sourse.append(sourse.attrib['id'])

    for result in root.iter('keyMapping'):
        ls_result.append(result.attrib['columnName'])

    for a,b in zip(ls_sourse,ls_result):
        print('%30s %30s' % (a,b))

#计算视图
def cal_view():
    root = tree.getiterator('calculationView')
    NodeList = []
    #获取除顶层的下级节点清单
    for i in root :
        NodeList.append(i.attrib['id'])

    for NodeName in NodeList:
        #检索DOM树id属性与节点清单匹配的节点
        for Element in root:
            if Element.attrib['id'] == NodeName:
                InputNodes = Element.iter('input')
                for InputNode in InputNodes:
                    #获取符合条件的Mapping节点内容
                    mapping = InputNode.iter('mapping')
                    for maps in mapping:
                        if 'source' in maps.attrib:
                            print('%30s %30s %30s %30s' % (InputNode.attrib['node'].replace('#',''),NodeName,maps.attrib['source'],maps.attrib['target']))

    #获取顶层节点相关信息
    root = tree.getiterator('attribute')
    KeyMapping = tree.getiterator('keyMapping')
    InputNodeTop = tree.getiterator('logicalModel')[0].attrib['id']
    for TopNode,KeyMap in zip(root,KeyMapping):
        print('%30s %30s %30s %30s' % (InputNodeTop,'FinalNode',KeyMap.attrib['columnName'],TopNode.attrib['id']))

cal_view()