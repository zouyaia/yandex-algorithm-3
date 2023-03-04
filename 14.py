cin = [i for i in map(int, input().split())]
n = cin[0]+1
stack = [[cin[1], 1]]
rside = [0]*n # правый меньший элемент
lside = [0]*n # левый меньший элемент
for i in range(2, n):
    while len(stack) > 0 and stack[-1][0] > cin[i]:
        rside[stack[-1][1]] = i-1
        stack.pop()
    stack.append([cin[i], i])
while len(stack) > 0:
    rside[stack[-1][1]] = n-1
    stack.pop()
# print(len(rside))
# print(rside)
stack = [[cin[n-1], n-1]]
for i in range(n-2, 0, -1):
    while len(stack) > 0 and stack[-1][0] > cin[i]:
        lside[stack[-1][1]] = i+1
        stack.pop()
    stack.append([cin[i], i])
while len(stack) > 0:
    lside[stack[-1][1]] = 1
    stack.pop()
# print(len(lside))
# print(lside)
ans = 0
for i in range(1, n):
    s = cin[i]*(rside[i]-lside[i]+1)
    ans = max(ans, s)
print(ans)

# TEST
# 6 5 4 7 3 10 2
# 15