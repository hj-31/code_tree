N = int(input())

def half_sum(n):
    if n <= 2:
        return n
    return n + half_sum(n-2)

print(half_sum(N))