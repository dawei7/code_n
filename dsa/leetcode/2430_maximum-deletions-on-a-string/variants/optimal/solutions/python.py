def solve(s: str) -> int:
    n = len(s)
    best = [1] * n
    next_lcp = [0] * (n + 1)

    for start in range(n - 1, -1, -1):
        current_lcp = [0] * (n + 1)
        first = s[start]
        for other in range(n - 1, start, -1):
            if first == s[other]:
                current_lcp[other] = next_lcp[other + 1] + 1

        current = 1
        for length in range(1, (n - start) // 2 + 1):
            if current_lcp[start + length] >= length:
                current = max(current, 1 + best[start + length])
        best[start] = current
        next_lcp = current_lcp

    return best[0]
