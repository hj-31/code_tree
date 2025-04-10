nums = tuple(map(int, input().split()))
n = len(nums)
total = sum(nums)

min_diff = 9999999

def diff_value(i, j, k, l):
    first = nums[i] + nums[j]
    second = nums[k] + nums[l]
    third = total - first - second

    biggest = max(first, second, third)
    smallest = min(first, second, third)
    
    return biggest - smallest


# first team = i, j
for i in range(n):
    for j in range(i+1, n):
        # second team = k, l
        for k in range(n):
            for l in range(k+1, n):
                if k in (i, j) or l in (i, j):
                    continue
                min_diff = min(min_diff, diff_value(i, j, k, l))
                
print(min_diff)
