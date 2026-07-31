def solve(nums: list[int], queries: list[list[int]]) -> list[int]:
    prefix = [[0] * 101]
    for number in nums:
        counts = prefix[-1].copy()
        counts[number] += 1
        prefix.append(counts)

    answers = []
    for left, right in queries:
        previous = 0
        best = 101
        for value in range(1, 101):
            if prefix[right + 1][value] == prefix[left][value]:
                continue
            if previous:
                best = min(best, value - previous)
            previous = value
        answers.append(-1 if best == 101 else best)
    return answers
