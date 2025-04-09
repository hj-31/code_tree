n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Up, Left, Right, Down
dxy = list(zip([-1, 0, 0, 1], [0, -1, 1, 0]))
move_dir = {"U": 0, "L": 1, "R": 2, "D": 3}

def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= n

direction = move_dir[d]
for _ in range(t):
    dx, dy = dxy[direction]
    nx, ny = r + dx, c + dy
    
    if not in_range(nx, ny):
        direction = 3 - direction
    else:
        r, c = nx, ny

print(r, c)