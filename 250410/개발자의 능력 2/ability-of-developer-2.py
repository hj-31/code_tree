nums = tuple(map(int, input().split()))
n = len(nums)
total = sum(nums)

min_diff = 9999999

for i in range(n):
    for j in range(i+1, n): # first team = i, j
        for k in range(n): # second team = k, l
            if k in (i, j):
                continue
            for l in range(n):
                if l in (i, j, k):
                    continue
                first = nums[i] + nums[j]
                second = nums[k] + nums[l]
                third = total - first - second

                biggest = max(first, second, third)
                smallest = min(first, second, third)

                min_diff = min(min_diff, biggest - smallest)

print(min_diff)