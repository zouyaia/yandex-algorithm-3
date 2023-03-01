from bisect import bisect_left as lb # equals c++ lower_bound()

M = int(input())
N = int(input())
stack = []
for i in range(N):
    p = list(map(int, input().split()))
    ix = lb(stack, p)
    stack.insert(ix, p)
    if len(stack) != 0:
        while ix+1 < len(stack) and stack[ix+1][0] <= p[1]:
            stack.pop(ix+1)
        while ix-1 >= 0 and stack[ix-1][1] >= p[0]:
            stack.pop(ix-1)
            ix -= 1
    # print(stack)
print(len(stack))