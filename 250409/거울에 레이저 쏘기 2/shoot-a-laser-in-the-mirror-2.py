n = int(input())

mirrors = []
for i in range(n):
    mirrors.append(list(input()))

# down, left, up, right : rotate 90
move_dir = [(1, 0), (0, -1), (-1, 0), (0, 1)]

k_dict = {}
x, y = -1, -1
idx, dir_idx = 3, 0
for k in range(4*n):
    dx, dy = move_dir[idx]
    x, y = x + dx, y + dy
    k_dict[k+1] = (x, y, dir_idx)

    if k % n == n - 1:
        x, y = x + dx, y + dy
        idx = (idx + 1) % 4
        dir_idx += 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


# 방향 전환하기
def change_direction(mirror, dir_idx):
    # / : down <-> left, up <-> right  &  \ : down <-> right, up <-> left
    to_slash =  [1, 0, 3, 2]
    to_backslash = [3, 2, 1, 0]

    if mirror == "/":
        return to_slash[dir_idx]
    else:
        return to_backslash[dir_idx]


k = int(input())

# 시작 위치
start_x, start_y, start_idx = k_dict[k]
# 격자 안에 시작 위치
x, y, idx = start_x + move_dir[start_idx][0], start_y + move_dir[start_idx][1], start_idx

cnt = 0
# 좌표가 범위 밖이면 끝
while in_range(x, y):
    # 좌표가 범위 안이니까 거울에 또 튕길 거
    cnt += 1
    # 거울에 튕겨 바뀐 방향 구하기
    idx = change_direction(mirrors[x][y], idx)
    # 다음 칸 좌표 구하기
    x, y = x + move_dir[idx][0], y + move_dir[idx][1]

print(cnt)