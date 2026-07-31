def solve(nums: list[int], queries: list[list[int]]) -> list[int]:
    length = len(nums)
    best = [[0] * length for _ in range(length)]

    for index, value in enumerate(nums):
        best[index][index] = value

    scores = nums[:]
    for width in range(2, length + 1):
        next_scores = [scores[start] ^ scores[start + 1] for start in range(length - width + 1)]

        for start, score in enumerate(next_scores):
            end = start + width - 1
            best[start][end] = max(
                score,
                best[start][end - 1],
                best[start + 1][end],
            )

        scores = next_scores

    return [best[left][right] for left, right in queries]
