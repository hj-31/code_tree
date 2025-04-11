n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

arr.sort()

max_x2 = -999999999
not_crossing = []

for x1, x2 in arr:
    if x2 > max_x2:
        not_crossing.append(x2)
        max_x2 = x2
    else:
        while not_crossing:
            before_x2 = not_crossing.pop()
            if before_x2 < x2:
                not_crossing.append(before_x2)
                break

print(len(not_crossing))
