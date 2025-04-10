n, t = map(int, input().split())
string = input()

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

mid = n // 2
move_dir = 0 # north

# up, right, down, left : 90 rotate = +1, -90 rotate = -1
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

cur_x, cur_y = mid, mid
total = arr[cur_x][cur_y]

def change_dir(move_dir, order):
    rotate_num = 1 if order == "R" else -1
    return (move_dir + rotate_num) % 4


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


for order in string:
    if order in ("R", "L"):
        move_dir = change_dir(move_dir, order)
    else:
        nx, ny = cur_x + dx[move_dir], cur_y + dy[move_dir]
        if in_range(nx, ny):
            cur_x, cur_y = nx, ny
            total += arr[cur_x][cur_y]

print(total)
