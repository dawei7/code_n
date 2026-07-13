MOD = 10**9 + 7


def solve(nums: list[int], k: int) -> int:
    nums.sort()
    n = len(nums)
    limit = min(k - 1, n - 1)

    comb_sums = [0] * n
    combinations = [0] * (limit + 1)
    combinations[0] = 1
    comb_sums[0] = 1

    for size in range(1, n):
        upper = min(size, limit)
        for choose in range(upper, 0, -1):
            combinations[choose] = (combinations[choose] + combinations[choose - 1]) % MOD
        comb_sums[size] = sum(combinations[: upper + 1]) % MOD

    answer = 0
    for index, value in enumerate(nums):
        answer = (answer + value * (comb_sums[index] + comb_sums[n - 1 - index])) % MOD
    return answer
