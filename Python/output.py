import path_length
import brackets_check
import palindrome_number
import prime_number
import yanghui_tran
select_type = int(input('选择一个功能：\n1.括号检查\n2.判断质数\n3.判断回文数\n4.杨辉三角\n5.矩阵路径长\n'))
if select_type == 1:
    print(brackets_check.brackets())
elif select_type == 2:
    print(prime_number.pri_num())
elif select_type == 3:
    print(palindrome_number.pal_num())
elif select_type == 4:
    for i in range(int(input('输入杨辉三角层数:\n'))):
        print(yanghui_tran.triangles2(i))
elif select_type == 5:
    print(path_length.path_length(eval(input('输入一个矩阵:\n'))))