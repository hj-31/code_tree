n = int(input())

arr = [[0] * n for _ in range(n)]
cur_x, cur_y = n//2, n//2

# right, up, left, down
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
move_dir, move_num = 0, 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


# 마지막 직선 이동은 전 방향 진행 수와 같아서 +1 하면 경계 밖 됨
def end():
    return not in_range(cur_x, cur_y)


def move():
    global cur_x, cur_y

    cur_x += dx[move_dir]
    cur_y += dy[move_dir]


cnt = 1
while not end():
    for _ in range(move_num):
        arr[cur_x][cur_y] = cnt
        cnt += 1

        move()
        if end():
            break
    
    move_dir = (move_dir + 1) % 4
    if move_dir in (0, 2):
        move_num += 1

for a in arr:
    print(*a)



""" 방법2
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
"""