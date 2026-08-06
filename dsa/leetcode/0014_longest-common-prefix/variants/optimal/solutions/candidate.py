def solve(strs: list[str]) -> str:
    first = strs[0]
    for i, c in enumerate(first):
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != c:
                return first[:i]
    return first
