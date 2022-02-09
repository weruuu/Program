# a = '()()[][}'
# def func(a):
#     x = []
#     if len(a)%2 == 1:
#         return 'false'
#     for i in a:
#         if i in ('(','[','{') :
#             x.append(i)
#         elif i in (')',']','}') and len(x) == 0:
#             return 'false'
#         elif (i==')' and x[-1] == '(') or (i==']' and x[-1] == '[') or (i=='}' and x[-1] == '{') :
#             x.pop(-1)
#         else :
#             return 'false'
#     if len(x) == 0:
#         return 'true'
#     else :
#         return 'false'
# print(func(a))


a = ['a',1,3,'b']
print(a.index('b'))