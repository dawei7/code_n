def solve(words: list[str]) -> int:
    def minimal_rotation(text: str) -> str:
        if not text:
            return ""

        doubled = text + text
        length = len(text)
        first = 0
        second = 1
        offset = 0
        while first < length and second < length and offset < length:
            first_char = doubled[first + offset]
            second_char = doubled[second + offset]
            if first_char == second_char:
                offset += 1
                continue

            if first_char > second_char:
                first = first + offset + 1
                if first == second:
                    first += 1
            else:
                second = second + offset + 1
                if first == second:
                    second += 1
            offset = 0

        start = min(first, second)
        return doubled[start : start + length]

    signatures = set()
    for word in words:
        signatures.add(
            (
                minimal_rotation(word[::2]),
                minimal_rotation(word[1::2]),
            )
        )

    return len(signatures)
