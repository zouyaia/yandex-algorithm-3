from collections import deque

def equalize(d1, d2):
    while len(d1) < len(d2):
        d1.append(d2.popleft())

n = int(input())
d1, d2 = deque(), deque()
for i in range(n):
    s = input().split()
    if s[0] == '+':
        x = int(s[1])
        d2.append(x) # to the end
        equalize(d1, d2)
    elif s[0] == '*':
        x = int(s[1])
        d2.appendleft(x) # to the center
        equalize(d1, d2)
    elif s[0] == '-':
        print(d1.popleft())
        equalize(d1, d2)
    # print("queue:", *d1, *d2)