test=[-1,-100,9,-100,8,-1,3]
sum,ans = 0,0
for x in test:
    sum += x
    ans = sum if sum > ans else ans
    if sum < 0: sum = 0
print(ans)