def solve(s: str) -> list[str]:
    seen: set[str] = set()
    repeated: set[str] = set()
    result: list[str] = []
    for start in range(len(s) - 9):
        sequence = s[start : start + 10]
        if sequence in seen:
            if sequence not in repeated:
                repeated.add(sequence)
                result.append(sequence)
        else:
            seen.add(sequence)
    return result
