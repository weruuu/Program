def pal_num():
    a=input('输入数字：\n')
    if a!=a[::-1]:
        return '不是回文数'
    else:
        return '是回文数'