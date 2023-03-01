from queue import Queue

K = int(input())
s = input()
ans = 0
for x in range(0, 26):
    c = chr(ord('a')+x)
    cur, k = 0, K
    R, L = 0, 0
    while R < len(s):
        while R < len(s) and (s[R] == c or k > 0):
            if s[R] != c:
                k -= 1
            R += 1
            cur += 1
        ans = max(ans, cur)
        if K == 0:
            cur = 0
            R += 1
        else:
            while L < len(s) and s[L] == c:
                L += 1
                cur -= 1
            if L < len(s):
                R += 1
                L += 1
print(ans)
