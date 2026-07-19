"""Optimal app-local solution for LeetCode 837."""


def solve(n, k, maxPts):
    if k == 0 or n >= k - 1 + maxPts:
        return 1.0

    probability = [0.0] * (n + 1)
    probability[0] = 1.0
    drawable_window = 1.0
    answer = 0.0

    for score in range(1, n + 1):
        probability[score] = drawable_window / maxPts
        if score < k:
            drawable_window += probability[score]
        else:
            answer += probability[score]

        outgoing = score - maxPts
        if 0 <= outgoing < k:
            drawable_window -= probability[outgoing]

    return answer
