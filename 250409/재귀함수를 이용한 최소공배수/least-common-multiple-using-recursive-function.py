N = int(input())
arr = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    
    return gcd(b, a%b)

def lcm(a, b):
    if b > a:
        a, b = b, a
    
    return a * b // gcd(a, b)

ans = arr[0]
for a in arr[1:]:
    ans = lcm(ans, a)

print(ans)