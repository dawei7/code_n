from collections import Counter


def solve(nums: list[str], target: str) -> int:
    counts = Counter(nums)
    answer = 0

    for split in range(1, len(target)):
        left = target[:split]
        right = target[split:]
        if left == right:
            answer += counts[left] * (counts[left] - 1)
        else:
            answer += counts[left] * counts[right]

    return answer
