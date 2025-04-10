n, m = map(int, input().split())

# 아래, 오른쪽, 위, 왼쪽
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

arr = [[0] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

x, y = -1, 0
movedir = 0
for i in range(n * m):
    nx, ny = x + dx[movedir], y + dy[movedir]
    if not in_range(nx, ny) or arr[nx][ny] != 0:
        movedir = (movedir + 1) % 4
    x, y = x + dx[movedir], y + dy[movedir]
    arr[x][y] = i + 1

for a in arr:
    print(*a)