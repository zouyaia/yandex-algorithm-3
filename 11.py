N = int(input())
for i in range(N):
    cin = list(map(float, input().split()))
    n, z = int(cin[0]) + 1, 0
    a = [cin[i] for i in range(1, n)]
    a.sort()
    stack = []
    for j in range(1, n):
        if len(stack) > 0 and cin[j] <= stack[-1]:
            stack.append(cin[j])
        else:
            while len(stack) > 0 and cin[j] > stack[-1] and abs(stack[-1]-a[z]) <= 1e-7:
                stack.pop()
                z += 1
            stack.append(cin[j])
    while len(stack) > 0 and abs(stack[-1]-a[z]) <= 1e-7:
        stack.pop()
        z += 1
    if len(stack) == 0 and z == len(a):
        print(1)
    else:
        print(0)
