def solve(nums: list[int], k: int) -> int:
    adjusted: list[int] = []
    for index, value in enumerate(nums):
        if value == 1:
            adjusted.append(index - len(adjusted))

    prefix = [0]
    for position in adjusted:
        prefix.append(prefix[-1] + position)

    answer = float("inf")
    for left in range(len(adjusted) - k + 1):
        right = left + k
        middle = left + k // 2
        median = adjusted[middle]
        left_cost = median * (middle - left) - (prefix[middle] - prefix[left])
        right_cost = (prefix[right] - prefix[middle + 1]) - median * (right - middle - 1)
        answer = min(answer, left_cost + right_cost)

    return int(answer)
