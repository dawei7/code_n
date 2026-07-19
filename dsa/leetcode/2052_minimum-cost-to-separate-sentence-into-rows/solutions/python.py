def solve(sentence: str, k: int) -> int:
    words = sentence.split()
    word_count = len(words)
    best = [float("inf")] * (word_count + 1)
    best[0] = 0

    for start in range(word_count):
        row_length = 0
        for end in range(start, word_count):
            row_length += len(words[end])
            if end > start:
                row_length += 1
            if row_length > k:
                break

            row_cost = 0 if end == word_count - 1 else (k - row_length) ** 2
            best[end + 1] = min(best[end + 1], best[start] + row_cost)

    return int(best[word_count])
