n = int(input())
if n % 2 == 0:
    k = n//2
    print(k*(k+1)*(4*k+1)//2)
else:
    k = (n-1)//2
    print((k+1)*(4*k**2+7*k+2)//2)
