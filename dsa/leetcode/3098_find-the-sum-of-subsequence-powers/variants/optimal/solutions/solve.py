def solve(nums: list[int], k: int) -> int:
    MOD = 1_000_000_007
    nums.sort()
    n = len(nums)

    differences = sorted({nums[j] - nums[i] for i in range(n) for j in range(i + 1, n) if nums[j] > nums[i]})

    def count_with_minimum_gap(gap: int) -> int:
        previous = [1] * n

        for _ in range(2, k + 1):
            current = [0] * n
            prefix = 0
            left = 0

            for right in range(n):
                while left < right and nums[right] - nums[left] >= gap:
                    prefix = (prefix + previous[left]) % MOD
                    left += 1
                current[right] = prefix

            previous = current

        return sum(previous) % MOD

    answer = 0
    previous_gap = 0

    for gap in differences:
        count = count_with_minimum_gap(gap)
        answer = (answer + (gap - previous_gap) * count) % MOD
        previous_gap = gap

    return answer
