n = int(input())
dots = [tuple(map(int, input().split())) for _ in range(n)]

min_area = 40000 * 40000
for i in range(n):
    max_x, max_y, min_x, min_y = 1, 1, 40000, 40000
    for j in range(n):
        if i == j:
            continue
        
        x, y = dots[j]
        max_x, max_y = max(max_x, x), max(max_y, y)
        min_x, min_y = min(min_x, x), min(min_y, y)

    area = (max_x - min_x) * (max_y - min_y)
    min_area = min(min_area, area)

print(min_area)
