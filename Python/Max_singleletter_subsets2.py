#单循环
a= input()
index,flag = -1,0
anow,amax = [],[]
for i in a:
    if i.isdigit() == True:
        anow.append(i)
    elif i.isdigit() == False and index == -1:
        anow.append(i)
        index = anow.index(i)
        flag = 1
    else :
        anow.append(i)
        anow = anow[index+1:]
    if len(amax) < len(anow):
        amax = anow.copy()
    else :
        index = anow.index(i)
    if (len(amax) == 1 and amax[0].isdigit() == False) or flag == 0:
        amax = []
    if len(amax) > len(a[a.find(i):]):
        break
print(amax)