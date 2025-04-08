N = int(input())

def factorial(n):
    if n == 1 or n == 0:
        return n
    
    return n * factorial(n-1)

print(factorial(N))