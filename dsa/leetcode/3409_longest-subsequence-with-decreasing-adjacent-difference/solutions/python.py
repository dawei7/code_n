def solve(nums: list[int]) -> int:
    max_value = 300
    dp = [[0] * (max_value + 1) for _ in range(max_value + 1)]
    suffix_best = [[0] * (max_value + 2) for _ in range(max_value + 1)]
    seen = [False] * (max_value + 1)
    answer = 1

    for value in nums:
        updates = [0] * (max_value + 1)
        for previous in range(1, max_value + 1):
            if not seen[previous]:
                continue
            difference = abs(value - previous)
            updates[difference] = max(
                updates[difference],
                max(2, suffix_best[previous][difference] + 1),
            )

        for difference, length in enumerate(updates):
            if length > dp[value][difference]:
                dp[value][difference] = length
                answer = max(answer, length)

        running = 0
        for difference in range(max_value, -1, -1):
            running = max(running, dp[value][difference])
            suffix_best[value][difference] = running
        seen[value] = True

    return answer
