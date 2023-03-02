s = input()
a = {}
n = len(s)
for i in s:
    a[i] = 0
d = [0]*n
d[0] = n
a[s[0]] += d[0]
for i in range(1, n):
    c = s[i]
    d[i] = d[i-1] - i + n - i
    a[c] += d[i]
a = dict(sorted(a.items()))
for k, v in a.items():
    print(f'{k}: {v}')