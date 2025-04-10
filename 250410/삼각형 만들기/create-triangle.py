n = int(input())
dots = [tuple(map(int, input().split())) for _ in range(n)]

def right_triangle(dot1, dot2, dot3):
    x1, y1 = dot1
    x2, y2 = dot2
    x3, y3 = dot3

    dx12, dx23, dx31 = x1 - x2, x2 - x3, x3 - x1
    dy12, dy23, dy31 = y1 - y2, y2 - y3, y3 - y1

    if dx12 == 0:
        if dy23 == 0:
            return dy12 * dx23
        elif dy31 == 0:
            return dy12 * dx31
    elif dx23 == 0:
        if dy12 == 0:
            return dy23 * dx12
        elif dy31 == 0:
            return dy23 * dx31
    elif dx31 == 0:
        if dy12 == 0:
            return dy31 * dx12
        elif dy23 == 0:
            return dy31 * dx23

    return 0


area = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            area = max(area, abs(right_triangle(dots[i], dots[j], dots[k])))

print(area)
