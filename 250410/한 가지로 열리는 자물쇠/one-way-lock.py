n = int(input())
a, b, c = map(int, input().split())

def under2(x):
    return -2 <= x <= 2

cnt = 0
for i in range(1, n+1):
    da = a - i
    if under2(da):
        cnt += n*n
        continue
    
    for j in range(1, n+1):
        db = b - j
        if under2(db):
            cnt += n
            continue

        for k in range(1, n+1):
            dc = c - k
            if under2(dc):
                cnt += 1

print(cnt)

