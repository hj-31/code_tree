nums = list(map(int, input().split()))
n = 6

total = sum(nums)
min_diff = 3000000

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            part = nums[i] + nums[j] + nums[k]
            min_diff = min(min_diff, abs(total - 2 * part))

print(min_diff)