def _generate_abbreviations(word: str) -> list[str]:
    length = len(word)
    result: list[str] = []

    for mask in range(1 << length):
        pieces: list[str] = []
        abbreviated = 0
        for index, letter in enumerate(word):
            if mask & (1 << index):
                abbreviated += 1
                continue
            if abbreviated:
                pieces.append(str(abbreviated))
                abbreviated = 0
            pieces.append(letter)
        if abbreviated:
            pieces.append(str(abbreviated))
        result.append("".join(pieces))

    return result


def solve(word: str) -> list[str]:
    return _generate_abbreviations(word)
