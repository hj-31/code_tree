n = int(input())
arr = list(map(int, input().split()))

def max_value(n, val):
    if n == 0:
        return arr[0] if arr[0] > val else val

    return max_value(n-1, arr[n] if arr[n] > val else val)

print(max_value(n-1, 0))