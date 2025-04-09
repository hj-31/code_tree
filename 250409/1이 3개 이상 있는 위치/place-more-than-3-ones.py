N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

dxy = list(zip([1, -1, 0, 0], [0, 0, 1, -1]))

cnt = 0
for i in range(N):
    for j in range(N):
        in_cnt = 0
        for dx, dy in dxy:
            nx, ny = i + dx, j + dy
            if in_range(nx, ny) and arr[nx][ny] == 1:
                in_cnt += 1
        if in_cnt >= 3:
            cnt += 1

print(cnt)

