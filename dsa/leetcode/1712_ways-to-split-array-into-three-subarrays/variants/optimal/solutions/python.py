def solve(nums: list[int]) -> int:
    modulo = 1_000_000_007
    prefix = [0]
    for value in nums:
        prefix.append(prefix[-1] + value)

    total = prefix[-1]
    ways = 0
    first_middle_end = 2
    first_too_large = 2

    for left_end in range(1, len(nums) - 1):
        first_middle_end = max(first_middle_end, left_end + 1)
        while (
            first_middle_end < len(nums)
            and prefix[first_middle_end] < 2 * prefix[left_end]
        ):
            first_middle_end += 1

        first_too_large = max(first_too_large, first_middle_end)
        while (
            first_too_large < len(nums)
            and 2 * prefix[first_too_large] <= total + prefix[left_end]
        ):
            first_too_large += 1

        ways += first_too_large - first_middle_end

    return ways % modulo
