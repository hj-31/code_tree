n, m = map(int, input().split())

string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
string_len = len(string)

arr = [[''] * m for _ in range(n)]

# right, down, left, up
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

x, y, move_dir = 0, 0, 0
for i in range(n * m):
    string_idx = i % string_len
    arr[x][y] = string[string_idx]

    nx, ny = x + dx[move_dir], y + dy[move_dir]
    if not in_range(nx, ny) or arr[nx][ny] != '':
        move_dir = (move_dir + 1) % 4
    x, y = x + dx[move_dir], y + dy[move_dir]

for a in arr:
    print(*a)