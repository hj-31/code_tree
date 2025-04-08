n = int(input())
arr = list(map(int, input().split()))

def max_value(n, val):
    if arr[n] > val:
        val = arr[n]

    if n == 0:
        return val

    return max_value(n-1, val)

print(max_value(n-1, 0))