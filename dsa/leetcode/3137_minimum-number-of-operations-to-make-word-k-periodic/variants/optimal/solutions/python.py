def solve(word: str, k: int) -> int:
    frequencies: dict[str, int] = {}

    for start in range(0, len(word), k):
        block = word[start : start + k]
        frequencies[block] = frequencies.get(block, 0) + 1

    block_count = len(word) // k
    return block_count - max(frequencies.values())
