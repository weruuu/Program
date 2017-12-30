s=[[1,2,3,4],[2,3,4,5],[4,5,6,7],[5,6,7,8]]
def check_row():
    for x in range(len(s)):
        for y in range(len(s)):
            val = s[x][y]
            for z in range(y+1,len(s)):
                if val == s[x][z]:
                    return False
    return True
def check_col():
    for y in range(len(s)):
        for x in range(len(s)):
            val = s[x][y]
            for z in range(x+1,len(s)):
                if val == s[z][y]:
                    return False
    return True
print(check_row(),check_col())
