import heapq

n = int(input())
a = [i for i in map(int, input().split())]
heapq.heapify(a)
ans = 0.0
while len(a) > 1:
    x = heapq.heappop(a) + heapq.heappop(a)
    ans += x*0.05
    heapq.heappush(a, x)
print(f'{ans:.2f}')