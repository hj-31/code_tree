string = input()

move_dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
x, y, dir_idx = 0, 0, 0

is_start = False
t = 1

for s in string:
    if s == "L":
        dir_idx = (dir_idx - 1) % 4
    elif s == "R":
        dir_idx = (dir_idx + 1) % 4
    else:
        x, y = x + move_dir[dir_idx][0], y + move_dir[dir_idx][1]
        if (x, y) == (0, 0):
            is_start = True
            break
    t += 1

if is_start:
    print(t)
else:
    print(-1)
