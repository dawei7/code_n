from collections import Counter


def solve(chunks: list[str], queries: list[str]) -> list[int]:
    text = "".join(chunks)
    word_counts: Counter[str] = Counter()
    word_start = -1

    for index, character in enumerate(text):
        is_letter = "a" <= character <= "z"
        is_joiner = (
            character == "-"
            and index > 0
            and index + 1 < len(text)
            and "a" <= text[index - 1] <= "z"
            and "a" <= text[index + 1] <= "z"
        )

        if is_letter or is_joiner:
            if word_start == -1:
                word_start = index
        elif word_start != -1:
            word_counts[text[word_start:index]] += 1
            word_start = -1

    if word_start != -1:
        word_counts[text[word_start:]] += 1

    return [word_counts[query] for query in queries]
