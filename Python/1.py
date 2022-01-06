





# class MaxSum(object):
#     def __init__(self, init_list):
#         self.l = init_list
#         self.subl = []
#     def max_sum(self):
#         sum = 0
#         ans = 0
#         if max(self.l) < 0:
#             return max(self.l)
#         for x in self.l:
#             sum += x
#             ans = sum if sum > ans else ans
#             if sum < 0: sum = 0
#         return ans
# if __name__ == '__main__':
#     test=[1,-100,9,-100,8,-1,3]
#     n = MaxSum(test)
#     print (n.max_sum())

# a= input()
# maxl = []
# max = 0
# for i in range(len(a)):
#     for j in range(i,len(a)):
#         flag = 0
#         for k in a[i:j+1]:
#             if k.isdigit() == False:
#                 flag += 1
#             if flag > 1:
#                 break
#         if flag == 1 and len(a[i:j+1])>max and len(a[i:j+1])!=1:
#             maxl = a[i:j+1]
#             max = len(a[i:j+1])
# print(maxl,max)

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
