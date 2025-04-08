N = int(input())

def count_execution(n):
    if n == 1:
        return 0
    
    if n % 2 == 0:
        return 1 + count_execution(n//2)
    else:
        return 1 + count_execution(n//3)

print(count_execution(N))