def longest_consec(strarr, k):
    strlen = len(strarr)
    if k <= 0 or strlen == 0 or k > strlen:
        return ''
    index = 0
    maxstr = ''
    while index+k<=strlen:
        if len(maxstr)<len(''.join(strarr[index:index+k])):
            maxstr = ''.join(strarr[index:index+k])
        index = index+1
    return maxstr

print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))


def longest_consec1(s, k):
    return max(["".join(s[i:i+k]) for i in range(len(s)-k+1)], key=len) if s and 0 < k <= len(s) else ""

print(longest_consec1(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))
