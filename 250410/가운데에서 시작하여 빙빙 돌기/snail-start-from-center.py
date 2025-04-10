n = int(input())

def in_range(x, y, small_n, mid):
    return mid - small_n <= x <= mid + small_n and mid - small_n <= y <= mid + small_n

arr = [[0] * n for _ in range(n)]

# rihgt, up, left, down
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
move_dir = 0

# 중앙 좌표, 중앙부터의 거리
mid, small_n = n // 2, 0
x, y = mid, mid
cnt = 1
while small_n <= n//2:
    arr[x][y] = cnt

    cnt += 1
    if (2*small_n+1) ** 2 < cnt:
        small_n += 1

    nx, ny = x + dx[move_dir], y + dy[move_dir]
    if not in_range(nx, ny, small_n, mid):
        move_dir = (move_dir + 1) % 4
    x, y = x + dx[move_dir], y + dy[move_dir]

for a in arr:
    print(*a)
