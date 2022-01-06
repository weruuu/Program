a = [1,3,-5]
b = [2,3,3]
# 对list a进行排序
for i in range(len(a) - 1):
    for j in range(len(a) - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
# 将list b中的元素插入排序后的list a中
for i in range(len(b)):
    for j in range(len(a)):
        if a[j]>=b[i]:
            a = a[:j]+[b[i]]+a[j:]
            break
        elif a[j]<b[i] and j==len(a)-1:
            a = a + [b[i]]
print(a)