n = int(input())
arr = list(map(int, input().split()))

def max_value(n, val):
    if n == -1:
        return val

    return max_value(n-1, arr[n] if arr[n] > val else val)

print(max_value(n-1, 0))