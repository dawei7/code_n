from bisect import bisect_left


def solve(intervals):
    ordered = sorted(
        (right, left, weight, index)
        for index, (left, right, weight) in enumerate(intervals)
    )
    ends = [item[0] for item in ordered]
    n = len(ordered)
    impossible = (-1, ())
    dp = [[(0, ())] * (n + 1)] + [
        [impossible] * (n + 1) for _ in range(4)
    ]

    for chosen in range(1, 5):
        for i in range(1, n + 1):
            best = dp[chosen][i - 1]
            _, left, weight, original_index = ordered[i - 1]
            previous = bisect_left(ends, left, 0, i - 1)
            score, indices = dp[chosen - 1][previous]

            if score >= 0:
                candidate = (
                    score + weight,
                    tuple(sorted((*indices, original_index))),
                )
                if candidate[0] > best[0] or (
                    candidate[0] == best[0] and candidate[1] < best[1]
                ):
                    best = candidate

            dp[chosen][i] = best

    answer = (0, ())
    for chosen in range(1, 5):
        candidate = dp[chosen][n]
        if candidate[0] > answer[0] or (
            candidate[0] == answer[0] and candidate[1] < answer[1]
        ):
            answer = candidate

    return list(answer[1])
