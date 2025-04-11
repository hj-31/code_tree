n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
# (x1, 0), (x2, 1) -> (x1, x2)

arr.sort()

max_x1, max_x2 = -1000001, -1000001
cnt = 0 # 교차 선분

is_crossing = False
crossing = 1

for x1, x2 in arr:
    if x2 < max_x2:
        is_crossing = True
        crossing += 1
    else:
        if is_crossing:
            is_crossing = False
            cnt += crossing
            crossing = 1
        max_x2 = x2

if is_crossing:
    cnt += crossing

print(n - cnt)
