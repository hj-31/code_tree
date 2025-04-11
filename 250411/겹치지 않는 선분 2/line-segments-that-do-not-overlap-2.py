n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

not_crossing = 0
for i in range(n):
    is_crossing = False
    for j in range(n):
        if i == j:
            continue
        
        x1, x2 = arr[i]
        y1, y2 = arr[j]

        if (x1 <= y1 and x2 >= y2) or (x1 > y1 and x2 < y2):
            is_crossing = True
            break
    
    if not is_crossing:
        not_crossing += 1

print(not_crossing)

""" 방법 2
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
"""
