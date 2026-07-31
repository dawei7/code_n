def solve(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    frequencies: dict[int, int] = {}
    answer = [0] * n

    for i in range(n - 1, -1, -1):
        exposed = i + k + 1
        if exposed < n:
            value = nums[exposed]
            frequencies[value] = frequencies.get(value, 0) + 1
        answer[i] = frequencies.get(nums[i], 0)

    return answer
