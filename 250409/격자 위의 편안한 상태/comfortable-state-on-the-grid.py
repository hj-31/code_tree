n, m = tuple(map(int, input().split()))

arr = [[0] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def stable(x, y):
    cnt = 0
    for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr[nx][ny] == 1:
            cnt += 1
    return cnt


for _ in range(m):
    r, c = tuple(map(int, input().split()))
    arr[r-1][c-1] = 1
    print(1) if stable(r-1, c-1) == 3 else print(0)
