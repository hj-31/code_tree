n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or k == i:
                continue

                is_success = True
                for num, cnt1, cnt2 in arr:
                    x, y, z = num // 100, num // 10 % 10, num % 10
                    strike, ball = 0, 0
                    
                    if i == x:
                        strike += 1
                    if j == y:
                        strike += 1
                    if k == z:
                        strike += 1
                    if i in (y, z):
                        ball += 1
                    if j in (x, z):
                        ball += 1
                    if k in (x, y):
                        ball += 1

                    if strike != cnt1 or ball != cnt2:
                        is_success = False
                        break
            
                if is_success:
                    cnt += 1

print(cnt)


""" 방법 2
arr_set = set()
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i != j and j != k and k != i:
                arr_set.add((i, j, k))

def count(abc, cnt1, cnt2):
    new_set = set()
    for xyz in arr_set:
        strike = len(list(filter(lambda i: abc[i] == xyz[i], [0, 1, 2])))
        ball = len(set(abc) & set(xyz)) - strike
        
        if strike == cnt1 and ball == cnt2:
            new_set.add(xyz)

    return new_set



for _ in range(n):
    num, cnt1, cnt2 = input().split()
    abc= tuple(map(int, list(num)))
    cnt1, cnt2 = int(cnt1), int(cnt2)
    arr_set = count(abc, cnt1, cnt2)
    
print(len(arr_set))
"""