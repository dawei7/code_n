def solve(nums, n, left, right):
    mod = 1_000_000_007
    n = min(len(nums), max(0, int(n)))
    sums = []
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            sums.append(total)
    sums.sort()
    left = max(1, int(left))
    right = min(len(sums), int(right))
    return sum(sums[left - 1:right]) % mod
