n = int(input())
arr = list(map(int, input().split()))

def max_value(n, arr):
    if n == 0:
        return arr[n]
    val = max_value(n-1, arr)
    return arr[n] if arr[n] >= val else val

print(max_value(n-1, arr))