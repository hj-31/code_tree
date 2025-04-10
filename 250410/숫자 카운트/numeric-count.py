n = int(input())

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