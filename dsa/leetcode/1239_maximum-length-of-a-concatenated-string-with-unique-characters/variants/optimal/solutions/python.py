def solve(arr: list[str]) -> int:
    masks = [0]
    best = 0
    for word in arr:
        word_mask = 0
        for character in word:
            bit = 1 << (ord(character) - ord("a"))
            if word_mask & bit:
                word_mask = 0
                break
            word_mask |= bit
        if word_mask == 0:
            continue

        for existing in masks[:]:
            if existing & word_mask == 0:
                combined = existing | word_mask
                masks.append(combined)
                best = max(best, combined.bit_count())
    return best
