n, m = list(map(int, input().split()))

arr = [[0] * m for _ in range(n)]

# N, E, S, W
move_dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir_idx = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

x, y, srt = 0, 0, 1
for _ in range(n*m):
    arr[x][y] = srt
    srt += 1

    nx, ny = x + move_dir[dir_idx][0], y + move_dir[dir_idx][1]
    if not in_range(nx, ny) or arr[nx][ny] != 0:
        dir_idx = (dir_idx + 1) % 4
    
    x += move_dir[dir_idx][0]
    y += move_dir[dir_idx][1]

for row in arr:
    print(*row)