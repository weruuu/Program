# #单循环
# a= '12as67865o254'#input()
# index,flag,stridx = -1,0,0
# anow,amax = [],[]
# for i in a:
#     if i.isdigit() == True:
#         anow.append(i)
#     elif i.isdigit() == False and index == -1:
#         anow.append(i)
#         index = anow.index(i)
#         stridx = a.index(i)
#         flag = 1
#     else :
#         anow.append(i)
#         anow = anow[stridx+1:]
#         stridx = 0
#     if len(amax) <= len(anow):
#         amax = anow.copy()
#     else :
#         index = anow.index(i)
#     if (len(amax) == 1 and amax[0].isdigit() == False) or flag == 0:
#         amax = []
# print(amax)


#单循环
a= '11a11a211a1115a5a4a'
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
        index = anow.index(i)
    if len(amax) < len(anow):
        amax = anow.copy()
    #else :
        #index = anow.index(i)
    if (len(amax) == 1 and amax[0].isdigit() == False) or flag == 0:
        amax = []
print(amax)