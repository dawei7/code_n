def solve(nums: list[int], l: int, r: int) -> int:
    answer = 10**18

    for length in range(l, r + 1):
        window_sum = sum(nums[:length])
        if 0 < window_sum < answer:
            answer = window_sum

        for end in range(length, len(nums)):
            window_sum += nums[end] - nums[end - length]
            if 0 < window_sum < answer:
                answer = window_sum

    return -1 if answer == 10**18 else answer
