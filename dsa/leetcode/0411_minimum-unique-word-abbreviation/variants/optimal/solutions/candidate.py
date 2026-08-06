"""Inert review candidate for LeetCode 411: Minimum Unique Word Abbreviation."""


def solve(target: str, dictionary: list[str]) -> str:
    n = len(target)
    differences: list[int] = []

    for word in dictionary:
        if len(word) != n:
            continue
        difference = 0
        for i, (target_character, word_character) in enumerate(zip(target, word)):
            if target_character != word_character:
                difference |= 1 << i
        differences.append(difference)

    if not differences:
        return str(n)

    def abbreviation_length(mask: int) -> int:
        tokens = 0
        i = 0
        while i < n:
            tokens += 1
            if mask & (1 << i):
                i += 1
            else:
                while i < n and not mask & (1 << i):
                    i += 1
        return tokens

    best_mask = (1 << n) - 1
    best_length = n
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
    for i, character in enumerate(target):
        if best_mask & (1 << i):
            if abbreviated:
                parts.append(str(abbreviated))
                abbreviated = 0
            parts.append(character)
        else:
            abbreviated += 1
    if abbreviated:
        parts.append(str(abbreviated))
    return "".join(parts)
