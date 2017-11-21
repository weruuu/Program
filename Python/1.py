#循环写法
def triangles1(n):
    T = [1]
    while n>0:
        yield T
        T.append(0)
        print(T)
        T = [T[i]+T[i-1] for i in range(len(T))]
        n = n - 1
n = int(input('输入杨辉三角层数:\n'))
for t in triangles1(n):
    print(t)