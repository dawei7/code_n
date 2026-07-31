def solve(nums: list[int]) -> int:
    bit_count = 30
    last_with_bit = [-1] * bit_count
    left_blocker = [-1] * len(nums)

    for index, value in enumerate(nums):
        blocker = -1
        for bit in range(bit_count):
            if value & (1 << bit) == 0:
                blocker = max(blocker, last_with_bit[bit])
            else:
                last_with_bit[bit] = index
        left_blocker[index] = blocker

    next_with_bit = [len(nums)] * bit_count
    next_equal: dict[int, int] = {}
    answer = 0

    for index in range(len(nums) - 1, -1, -1):
        value = nums[index]
        blocker = len(nums)

        for bit in range(bit_count):
            if value & (1 << bit) == 0:
                blocker = min(blocker, next_with_bit[bit])
            else:
                next_with_bit[bit] = index

        right_limit = min(blocker, next_equal.get(value, len(nums)))
        answer += (index - left_blocker[index]) * (right_limit - index)
        next_equal[value] = index

    return answer
