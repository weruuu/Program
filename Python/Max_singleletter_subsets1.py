#子集遍历
a= input()
maxl,max = '',0
for i in range(len(a)):
    for j in range(i,len(a)):
        flag = 0
        for k in a[i:j+1]:
            if k.isdigit() == False:
                flag += 1
            if flag > 1:
                break
        if flag == 1 and len(a[i:j+1])>max and len(a[i:j+1])!=1:
            maxl = a[i:j+1]
            max = len(a[i:j+1])
print(maxl,max)

