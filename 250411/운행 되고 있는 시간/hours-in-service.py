n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(n):
    work = set()
    for j in range(n):
        if i == j:
            continue

        for k in range(arr[j][0], arr[j][1]):
            work.add(k)
    cnt = max(cnt, len(work))

print(cnt)
