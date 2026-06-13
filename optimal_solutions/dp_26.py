"""Optimal solution for dp_26: Optimal Binary Search Tree.

opt[i][j] = min cost over BSTs containing keys[i..j].
Recurrence: try k in [i, j] as the root. Cost of putting
a subtree at depth+1 adds the total probability.
"""


def solve(keys, probs, n):
    if n == 0:
        return 0
    INF = float("inf")
    prefix = [0.0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + probs[i]
    opt = [[0.0] * n for _ in range(n)]
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            best = INF
            for k in range(i, j + 1):
                left = opt[i][k - 1] if k > i else 0
                right = opt[k + 1][j] if k < j else 0
                c = left + right + prefix[j + 1] - prefix[i]
                if c < best:
                    best = c
            opt[i][j] = best
    return opt[0][n - 1]
