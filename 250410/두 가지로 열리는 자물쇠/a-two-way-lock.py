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
    a_list = set(filter(lambda i: 1 <= i <= n, possible_set[a]))
    b_list = set(filter(lambda i: 1 <= i <= n, possible_set[b]))
    c_list = set(filter(lambda i: 1 <= i <= n, possible_set[c]))
    
    x_list = set(filter(lambda i: 1 <= i <= n, possible_set[x]))
    y_list = set(filter(lambda i: 1 <= i <= n, possible_set[y]))
    z_list = set(filter(lambda i: 1 <= i <= n, possible_set[z]))

    i, j, k = a_list & x_list, b_list & y_list, c_list & z_list
    return len(i) * len(j) * len(k)


cnt1 = count_possible(a1, b1, c1)
cnt2 = count_possible(a2, b2, c2)
duplicate_cnt = duplicate(a1, b1, c1, a2, b2, c2)

print(cnt1 + cnt2 - duplicate_cnt)