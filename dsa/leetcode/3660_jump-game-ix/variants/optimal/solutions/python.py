def solve(nums: list[int]) -> list[int]:
    n = len(nums)
    suffix_min = nums.copy()
    for i in range(n - 2, -1, -1):
        suffix_min[i] = min(nums[i], suffix_min[i + 1])

    answer = [0] * n
    start = 0
    segment_max = nums[0]

    for i in range(n - 1):
        segment_max = max(segment_max, nums[i])
        if segment_max <= suffix_min[i + 1]:
            for j in range(start, i + 1):
                answer[j] = segment_max
            start = i + 1
            segment_max = nums[start]

    segment_max = max(segment_max, nums[-1])
    for j in range(start, n):
        answer[j] = segment_max

    return answer
