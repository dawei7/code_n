def solve(nums: list[int]) -> int:
    prefix_counts = {0: 1}
    prefix_xor = 0
    answer = 0

    for value in nums:
        prefix_xor ^= value
        answer += prefix_counts.get(prefix_xor, 0)
        prefix_counts[prefix_xor] = prefix_counts.get(prefix_xor, 0) + 1

    return answer
