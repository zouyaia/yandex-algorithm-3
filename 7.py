from math import ceil, floor

A = list(map(int, input().split(':')))
B = list(map(int, input().split(':')))
C = list(map(int, input().split(':')))
if C[0] >= A[0]:
    t = ((C[0] - A[0]) * 3600 + (C[1] - A[1]) * 60 + C[2] - A[2]) / 2
else:
    t = ((C[0] - A[0] + 24) * 3600 + (C[1] - A[1]) * 60 + C[2] - A[2]) / 2
if t * 10 % 10 == 5:
    t = ceil(t)
else:
    t = floor(t)
T = B[0]*3600 + B[1]*60 + B[2] + t
h, m, s = T // 3600 % 24, T // 60 % 60, T % 60
print(f'{h:02d}:{m:02d}:{s:02d}')