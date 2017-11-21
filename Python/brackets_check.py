def brackets():
    a = list(input('请输入英文括号序列\n'))
    b = []
    i = 0
    l = []
    while len(a) > 0 :
        if str(a[0]) == '(' or str(a[0]) == '[' or str(a[0]) == '{' :
            b.append(str(a[0]))
            a.pop(0)
            i = i + 1
            l.append(i)
        elif (a[0] == ')' or a[0] == ']' or a[0] == '}') and len(b)==0:
            print('第',i+1,'个位置的括号未找到起始括号')
            exit()
        elif a[0] == ')' and b[-1] == '(' and len(b)>0 :
            b.pop(-1)
            a.pop(0)
            i = i + 1
            l.pop(-1)
        elif a[0] == ']' and b[-1] == '[' and len(b)>0 :
            b.pop(-1)
            a.pop(0)
            i = i + 1
            l.pop(-1)
        elif a[0] == '}' and b[-1] == '{' and len(b)>0 :
            b.pop(-1)
            a.pop(0)
            i = i + 1
            l.pop(-1)
        else :
            return '第',i,'个位置的括号未正确结束'
    if len(b) > 0 :
        return '第',l[-1],'个位置的括号未正确结束'
    return "所有括号正确匹配"