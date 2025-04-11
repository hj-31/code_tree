from collections import defaultdict

n, m, d, s = map(int, input().split())
# 몇 번째 사람 p, 몇 번째 치즈 m, 언제 먹었는지 t (1~N)
arr_eat = [tuple(map(int, input().split())) for _ in range(d)]
# 몇 번째 사람 p, 언제 아팠는지 t (상한거 먹고 1초 지나야 아픔, 다른 아픈 사람 존재 가능성 있음)
arr_sick = [tuple(map(int, input().split())) for _ in range(s)]

unfresh = set([i for i in range(1, m+1)])
cheese = defaultdict(set)

for p, t in arr_sick:
    unfresh_p = set()
    for pi, mi, ti in arr_eat:
        cheese[mi].add(pi)
        if p != pi:
            continue
        if ti < t:
            unfresh_p.add(mi)
    unfresh.intersection_update(unfresh_p)

patient = set()
for unfresh_cheese in unfresh:
    patient.update(cheese[unfresh_cheese])

print(len(patient))
