def solve(s: str) -> str:
    ordered = [""] * 9
    word_count = 0

    for token in s.split():
        position = int(token[-1]) - 1
        ordered[position] = token[:-1]
        word_count += 1

    return " ".join(ordered[:word_count])
