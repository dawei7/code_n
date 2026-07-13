"""Optimal app-local solution for LeetCode 411."""


def solve(target: str, dictionary: list[str]) -> str:
    length = len(target)
    differences: list[int] = []

    for word in dictionary:
        if len(word) != length:
            continue
        difference = 0
        for index, (target_character, word_character) in enumerate(zip(target, word, strict=True)):
            if target_character != word_character:
                difference |= 1 << index
        differences.append(difference)

    if not differences:
        return str(length)

    def abbreviation_length(mask: int) -> int:
        tokens = 0
        index = 0
        while index < length:
            tokens += 1
            if mask & (1 << index):
                index += 1
            else:
                while index < length and not mask & (1 << index):
                    index += 1
        return tokens

    best_mask = (1 << length) - 1
    best_length = length
    seen: set[int] = set()

    def search(mask: int) -> None:
        nonlocal best_mask, best_length
        if mask in seen:
            return
        seen.add(mask)

        uncovered = [difference for difference in differences if mask & difference == 0]
        candidate_length = abbreviation_length(mask)
        if not uncovered:
            if candidate_length < best_length:
                best_mask = mask
                best_length = candidate_length
            return
        if candidate_length >= best_length:
            return

        difference = min(uncovered, key=int.bit_count)
        remaining = difference
        while remaining:
            bit = remaining & -remaining
            search(mask | bit)
            remaining -= bit

    search(0)

    parts: list[str] = []
    abbreviated = 0
    for index, character in enumerate(target):
        if best_mask & (1 << index):
            if abbreviated:
                parts.append(str(abbreviated))
                abbreviated = 0
            parts.append(character)
        else:
            abbreviated += 1
    if abbreviated:
        parts.append(str(abbreviated))
    return "".join(parts)
