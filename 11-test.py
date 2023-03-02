from random import randint, random

f = open("output11.txt", "w")
N = randint(50, 100)
print(N, file=f)
for j in range(N):
    K = randint(1, 10)
    x = [random()*100+1 for i in range(K)]
    print(K, *x, file=f)