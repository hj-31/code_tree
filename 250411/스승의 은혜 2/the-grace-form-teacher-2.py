n, b = map(int, input().split())
p = [int(input()) for _ in range(n)]
p.sort()

max_cnt = 0
# i번째 학생에게 반값 쿠폰 써주기
for i in range(n):
    price = p[i]//2
    if price > b:
        continue
    else:
        cnt = 1

    for j in range(n):
        if i == j:
            continue

        price += p[j]
        if price <= b:
            cnt += 1
        else:
            break
            
    max_cnt = max(max_cnt, cnt)

print(max_cnt)
