<<<<<<< HEAD
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
=======
<<<<<<< HEAD
from ctypes import *
print(windll.kernel32)
print(cdll.msvcrt)
libc = cdll.msvcrt
=======
from bs4 import BeautifulSoup
import requests
import pymysql
import datetime
import xlwt
>>>>>>> e503aa12f5133023491d968e7d827e2c2758a696

    def insetleft(self, value):
        self.left = TreeNode(value)
        self.left.parent = self
        return self.left

    def insertright(self, value):
        self.right = TreeNode(value)
        self.right.parent = self
        return self.right

<<<<<<< HEAD
    def show(self):
        print(self.data)
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:#递归边界
            return 0
        else:
            l=1+self.maxDepth(root.left)#递归
            r=1+self.maxDepth(root.right)
            return max(l,r)
solution = Solution()
root = TreeNode(3)
a = root.insertleft(9)
b = root.insertright(20)
c = a.insertleft(None)
d = a.insertright(None)
e = b.insertleft(15)
f = b.insertright(7)
print(solution.maxDepth(root))
=======
# for elem in result:
#     print(nowTime,elem[0],elem[1])
#     sql = "insert into mysql.nsh_money values('"+nowTime+"',"+str(elem[0])+","+str(elem[1])+")"
#     cursor.execute(sql)
#     connect.commit()
# print('写入完成')

sql = "select * from mysql.v_nsh"
cursor.execute(sql)
excel_set = []
for i in cursor:
    excel_set.append([i[0],i[1],str(i[2])])

# 关闭连接
cursor.close()
connect.close()

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('test')
for x in range(len(excel_set)):
    for y in range(len(excel_set[0])):
        worksheet.write(x, y, label=excel_set[x][y])
workbook.save('%s.xls' % ('nsh'))
>>>>>>> d6576d6120e9393ace7497fbe5605641758350f6
>>>>>>> e503aa12f5133023491d968e7d827e2c2758a696
