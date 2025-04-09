N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def part_cnt(x, y):
    cnt = 0
    for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr[nx][ny] == 1:
            cnt += 1
    return cnt


cnt = 0
for i in range(N):
    for j in range(N):
        if part_cnt(i, j) >= 3:
            cnt += 1

print(cnt)

