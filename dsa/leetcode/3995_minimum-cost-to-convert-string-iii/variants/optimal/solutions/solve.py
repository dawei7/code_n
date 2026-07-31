def solve(
    source: str,
    target: str,
    rules: list[list[str]],
    costs: list[int],
) -> int:
    n = len(source)
    infinity = 10**30
    dp = [infinity] * (n + 1)
    dp[0] = 0
    prepared = [(pattern, replacement, cost + pattern.count("*")) for (pattern, replacement), cost in zip(rules, costs)]

    for index in range(n):
        if dp[index] == infinity:
            continue
        if source[index] == target[index]:
            dp[index + 1] = min(dp[index + 1], dp[index])

        for pattern, replacement, total_cost in prepared:
            end = index + len(pattern)
            if end > n or not target.startswith(replacement, index):
                continue
            if all(
                pattern[offset] == "*" or pattern[offset] == source[index + offset] for offset in range(len(pattern))
            ):
                dp[end] = min(dp[end], dp[index] + total_cost)

    return -1 if dp[n] == infinity else dp[n]
