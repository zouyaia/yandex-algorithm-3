def evaluate(s):
    if len(s) == 0: return ""
    if s in ["!", "|", "&", "^"]: return s
    r = s.replace("|", " ").replace("^", " ").split()
    # print(r)
    ans, li = eval(r[0].replace("&", " and ").replace("!", " not ")), len(r[0])+1
    for i in range(1, len(r)):
        exp = eval(r[i].replace("&", " and ").replace("!", " not "))
        # print(s[li-1])
        if s[li-1] == '|':
            ans = ans or exp
        elif s[li-1] == '^':
            ans = ans ^ exp
        li += len(r[i])+1
    if ans: return "1"
    else: return "0"


s = input()
s = s.replace("()", "")
l = s.rfind("(")
while l != -1:
    r = s.find(")", l, len(s))
    # print(l, r, s[l+1:r])
    ans = evaluate(s[l+1:r]) # expression in brackets
    s = s[:l]+ans+s[r+1:]
    l = s.rfind("(")
print(evaluate(s))

# TESTS
# 1^0&!(0|1^1|!(0^(1|0)^0)&0&!1|0)
# 1
# ()