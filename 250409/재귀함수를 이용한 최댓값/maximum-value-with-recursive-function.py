n = int(input())
arr = list(map(int, input().split()))

def max_value(i, n, arr):
    if i == n-1:
        return arr[-1]
        
    return max(arr[i], max_value(i+1, n, arr))

print(max_value(0, n, arr))