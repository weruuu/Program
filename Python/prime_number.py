def pri_num():
    a=int(input('输入数字：\n'))
    b = [x for x in range(2,a) if a%x==0]
    if len(b)>0:
        return b
    else :
        return '是'
