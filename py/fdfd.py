a = ''
b = input('输入字符串')
n = len(b)
for c in range(n):
    print(c)
    a = a +b[n-1-c]
print(a)