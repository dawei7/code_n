def solve(lcp: list[list[int]]) -> str:
    n = len(lcp)

    labels = [-1] * n
    next_label = 0
    for i in range(n):
        if labels[i] != -1:
            continue
        if next_label == 26:
            return ""
        for j in range(i, n):
            if lcp[i][j] > 0:
                labels[j] = next_label
        next_label += 1

    produced = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        if lcp[i][i] != n - i:
            return ""
        for j in range(n - 1, -1, -1):
            if labels[i] == labels[j]:
                produced[i][j] = produced[i + 1][j + 1] + 1
            if produced[i][j] != lcp[i][j]:
                return ""

    return "".join(chr(ord("a") + label) for label in labels)
