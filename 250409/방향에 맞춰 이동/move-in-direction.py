N = int(input())

# N, S, W, E
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
direction_idx = {
    "N": 0, "S": 1, "W": 2, "E": 3
}

x, y = 0, 0
for _ in range(N):
    direction, distance = input().split()
    distance = int(distance)
    x, y = x + distance * dx[direction_idx[direction]], y + distance * dy[direction_idx[direction]]

print(x, y)