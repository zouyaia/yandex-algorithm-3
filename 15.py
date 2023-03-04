# author: @estle
# s = "<e><a><z></z></a></e>" * 50
# s = s[:-7] + '>' + s[-6:]
s = input()
alpha = ['<', '>', '/']
alpha += [chr(ord('a') + i) for i in range(26)]
# print(alpha)
for ch in alpha:
    flag = 0  # exit flag
    for k in range(len(s)):
        if 0 < k < len(s) - 1:
            if ch == '<' and (s[k - 1] != '>' or s[k + 1] == '>' or s[k + 1] == '<'):
                continue
            elif ch == '>' and (s[k + 1] != '<' or s[k - 1] == '>' or s[k - 1] == '<'):
                continue
            elif ch == '/' and (s[k - 1] != '<' or s[k + 1] == '>' or s[k + 1] == '<'):
                continue
        a = s[:k] + ch + s[k + 1:]  # new string, that may be correct
        # print(a)
        d = []
        l, flag2 = 0, 1
        while l < len(a) and flag2:
            r = l
            st = a[r]
            if st != '<':
                flag2 = 0
                continue
            r += 1
            ex = 0
            while r < len(a) and a[r] != '>' and a[r] != '<':
                if a[r] == '/' and ex == 0 and r - l == 1:
                    ex = 1
                    r += 1
                    continue
                elif a[r] == '/' and (ex or r - l != 1):
                    flag2 = 0
                    break
                st += a[r]
                r += 1
            if r < len(a): st += a[r]
            if st[0] == '<' and st[-1] == '>':
                if len(d) > 0 and ex and flag2 and len(d[-1]) == len(st) and d[-1] == st:
                    d.pop()
                elif ex == 0 and flag2:
                    d.append(st)
                else:
                    flag2 = 0
                    continue
            else:
                flag2 = 0
                continue
            l = r + 1
        if len(d) == 0 and flag2:
            print(a)
            flag = 1
            break
    if flag:
        break

# TEST 1
# <a></b>
# <b></b>
# TEST 2
# <a><aa>
# <a></a>
# TEST 3
# <a><>a>
# <a></a>
# TEST 4
# <a/</a>
# <a></a>
# TEST 5
# <a><b></b><c></a></a>
# <a><b></b><a></a></a>
# TEST 6
# <b><b></b><c></c>//b>
# <b><b></b><c></c></b>
# TEST 7
# <a<</a>
# <a></a>
# TEST 8
# <f><//><e></e>
# <f></f><e></e>

# NOTES
# '<' = 2k - 1
# '>' = 2k
# 'a-z' = 2m - 1
# '/' = k
# <<></a>
# <b><>b>
# подстановка одного символа в каждую позицию строки и проверка на корректность с помощью stack
# stack = [<a><b></b><c>] + </c>
