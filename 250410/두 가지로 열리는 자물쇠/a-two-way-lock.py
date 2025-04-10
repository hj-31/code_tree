n = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

possible_set = {}
for i in range(1, 10):
    lst = [(i+j)%9 if (i+j)%9 != 0 else 9 for j in range(-2, 3)]
    possible_set[i] = lst

def is_possible(x, y):
    return x in possible_set[y]


def count_possible(a, b, c):
    cnt = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if is_possible(i, a) and is_possible(j, b) and is_possible(k, c):
                    cnt += 1

    return cnt


def duplicate(a, b, c, x, y, z):
    first = set(possible_set[a]) & set(possible_set[x])
    second = set(possible_set[b]) & set(possible_set[y])

total_cnt = count_possible(a1, b1, c1) + count_possible(a2, b2, c2) - 1
print(total_cnt)