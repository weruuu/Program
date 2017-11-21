#循环写法
def triangles1(n):
    T = [1]
    while n>0:
        yield T
        T.append(0)
        T = [T[i]+T[i-1] for i in range(len(T))]
        n = n - 1
'''n = int(input('输入杨辉三角层数:\n'))
for t in triangles1(n):
    print(t)'''
#递归写法
def triangles2(i):
    if i == 0:
        return [1]
    return [ i+j for i,j in zip(triangles2(i-1)+[0],[0]+triangles2(i-1)) ]
'''for i in range(int(input('输入杨辉三角层数:\n'))):
    print(triangles2(i))'''