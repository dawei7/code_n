def solve(nums: list[int]) -> float:
    ordered = sorted(nums)
    answer = float("inf")

    for left in range(len(ordered) // 2):
        right = len(ordered) - 1 - left
        answer = min(answer, (ordered[left] + ordered[right]) / 2)

    return answer
