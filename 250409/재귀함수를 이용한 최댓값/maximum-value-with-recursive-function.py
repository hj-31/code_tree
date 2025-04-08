n = int(input())
arr = list(map(int, input().split()))

def max_value(n, arr):
    if n == 0:
        return arr[n]
        
    return max(arr[n], max_value(n-1, arr))

print(max_value(n-1, arr))