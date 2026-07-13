def solve(s: str, word_dict: list[str]) -> bool:
    words = set(word_dict)
    reachable = [False] * (len(s) + 1)
    reachable[0] = True
    for end in range(1, len(s) + 1):
        for start in range(end):
            if reachable[start] and s[start:end] in words:
                reachable[end] = True
                break
    return reachable[-1]
