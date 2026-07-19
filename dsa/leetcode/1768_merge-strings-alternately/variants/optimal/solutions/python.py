def solve(word1: str, word2: str) -> str:
    merged: list[str] = []
    shared = min(len(word1), len(word2))

    for index in range(shared):
        merged.append(word1[index])
        merged.append(word2[index])

    merged.append(word1[shared:])
    merged.append(word2[shared:])
    return "".join(merged)
