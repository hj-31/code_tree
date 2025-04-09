N = int(input())

def f(n):
    if n == 1:
        return 0
    
    if n % 2 == 0:
        return 1 + f(n//2)
    else:
        return 1 + f(n*3+1)

print(f(N))