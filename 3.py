n = int(input())
a = map(int, input().split())
k = int(input())
p = map(int, input().split())
a = sorted(set(a))
for x in p:
    l, r = 0, len(a)-1
    while l+1 < r:
        mid = (l+r)//2
        if a[mid] >= x:
            r = mid-1
        else:
            l = mid
    if x > a[r]:
        print(r+1)
    elif x > a[l]:
        print(l+1)
    else:
        print(l)