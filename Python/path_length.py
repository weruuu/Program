def path_length(list1):
    if len(list1)<2:
        return list1
    for i in range(1,len(list1)):
        list1[0][i]=list1[0][i-1]+list1[0][i]
        list1[i][0]=list1[i-1][0]+list1[i][0]
    for i in range(1,len(list1)):
        for j in range(1,len(list1)):
            sum1=list1[i][j-1]+list1[i][j]
            sum2=list1[i-1][j]+list1[i][j]
            list1[i][j]=sum1 if sum1<sum2 else sum2
    return list1[len(list1)-1][len(list1)-1]