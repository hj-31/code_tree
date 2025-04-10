n = int(input())
dots = [tuple(map(int, input().split())) for _ in range(n)]

distance = 999999999

for i in range(n):
    for j in range(i+1, n):
        dxy = (dots[i][0] - dots[j][0]) ** 2 + (dots[i][1] - dots[j][1]) ** 2
        distance = min(distance, dxy)

print(distance)
