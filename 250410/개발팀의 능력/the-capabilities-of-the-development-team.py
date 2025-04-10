nums = tuple(map(int, input().split()))
n = len(nums)
total = sum(nums)

def diff_value(i, j, k):
    first = nums[i] + nums[j]
    second = total - first - nums[k]

    if first == second or first == nums[k] or second == nums[k]:
        return 999999999
    else:
        return max(first, second, nums[k]) - min(first, second, nums[k])


min_diff = 999999999
for i in range(n):
    for j in range(i+1, n):
        for k in range(n):
            if k in (i, j):
                continue
            diff = diff_value(i, j, k)
            min_diff = min(min_diff, diff)

print(min_diff)
