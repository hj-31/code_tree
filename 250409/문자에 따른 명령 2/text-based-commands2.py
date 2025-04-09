order_list = list(input().strip())

x, y = 0, 0

# E, S, W, N
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
move_dir = [0, 1, 2, 3]

d = move_dir[3]
for order in order_list:
    if order == "L":
        d = move_dir[(d-1)%4]
    elif order == "R":
        d = move_dir[(d+1)%4]
    else:
        x += dx[d]
        y += dy[d]

print(x, y)
