n = int(input())

move_dir = {
    "W": (0, -1), "E": (0, 1),
    "N": (-1, 0), "S": (1, 0)
}

x, y, t = 0, 0, 0
is_move = True
for _ in range(n):
    d, dn = input().split()
    dn = int(dn)

    dx, dy = move_dir[d]

    for _ in range(dn):
        x, y = x + dx, y + dy
        t += 1
        if (x, y) == (0, 0):
            is_move = False
            break
    
    if not is_move:
        break

print(-1) if is_move else print(t)


