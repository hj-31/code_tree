n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]

# Up, Down, Right, Left

def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= n

move_dir = { "U": 0, "D": 3, "R": 2, "L": 1}
direction = move_dir[d]

while t > 0:
    nx, ny = r + dx[direction], c + dy[direction]
    
    if not in_range(nx, ny):
        direction = 3 - direction
    else:
        r, c = nx, ny

    t -= 1

print(r, c)