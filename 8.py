k = int(input())
x, y = [], []
for i in range(k):
    xi, yi = map(int, input().split())
    x += [xi]
    y += [yi]
print(min(x), min(y), max(x), max(y))