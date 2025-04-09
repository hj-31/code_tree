n = int(input())

mirrors = []
for i in range(n):
    mirrors.append(list(input()))

# down, left, up, right : rotate 90
move_dir = [(1, 0), (0, -1), (-1, 0), (0, 1)]

k_dict = {}
x, y = 0, -1
for k in range(4*n):
    pos = (k//3 -1)%4
    x, y = x + move_dir[pos][0], y + move_dir[pos][1]
    k_dict[k+1] = (x, y, k//3)
    # k: (x, y, direction)

k = int(input())

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 시작 위치
x, y, idx = k_dict[k]
# 격자 안에 시작 위치
x, y = x + move_dir[idx][0], y + move_dir[idx][1]
cnt = 0

# 방향 전환하기
def change_direction(mirror, dir_idx):
    # / : down <-> left, up <-> right  &  \ : down <-> right, up <-> left
    to_slash_idx = [1, 0, 3, 2]
    to_backslash_idx = [3, 2, 1, 0]

    return to_slash_idx[dir_idx] if mirror == "/" else to_backslash_idx[dir_idx]


# 좌표가 범위 밖이면 끝
while in_range(x, y):
    # 좌표가 범위 안이니까 거울에 또 튕길 거
    cnt += 1
    # 거울에 튕겨 바뀐 방향 구하기
    idx = change_direction(mirrors[x][y], idx)
    # 다음 칸 좌표 구하기
    x, y = x + move_dir[idx][0], y + move_dir[idx][1]
    # 진입 방향 바꾸기 : d <-> u, l <-> r
    idx = (idx + 2) % 4

print(cnt)