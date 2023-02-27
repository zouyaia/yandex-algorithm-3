a = open("input.txt", 'r').read()
m = {}
for i in a:
    if i == ' ' or i == '\n':
        continue
    if i not in m.keys():
        m[i] = 1
    else:
        m[i] += 1
with open("output.txt", "a") as f:
    ans = ""
    mx = max(m.values())
    while mx > 0:
        for k in sorted(m.keys()):
            if m[k] >= mx:
                ans += '#'
            else:
                ans += ' '
        print(ans, file=f)
        ans = ""
        mx -= 1
    for k in sorted(m.keys()):
        ans += k
    print(ans, file=f)