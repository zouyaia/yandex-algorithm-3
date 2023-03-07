import heapq

k, n = map(int, input().split())
s = [i for i in range(1, k+1)]
heapq.heapify(s) # now heap structure
ans = [0]*n
flag = 1
ti = []
for i in range(n):
    a, b = map(int, input().split())
    ti.append([a, -1, i])
    ti.append([b, 1, i])
ti.sort()
for i in range(len(ti)):
    if ti[i][1] == -1:
        if len(s) == 0:
            print(0, ti[i][2]+1)
            flag = 0
            break
        mi = heapq.heappop(s) # min element in garage
        ans[ti[i][2]] = mi
    else:
        heapq.heappush(s, ans[ti[i][2]]) # garage is free again
if flag:
    for i in ans:
        print(i)