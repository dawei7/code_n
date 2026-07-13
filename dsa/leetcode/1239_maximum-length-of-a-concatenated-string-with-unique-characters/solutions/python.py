def solve(arr):
    masks = [0]
    best = 0
    for word in arr:
        mask = 0
        for ch in word:
            bit = 1 << (ord(ch) - ord("a"))
            if mask & bit:
                mask = 0
                break
            mask |= bit
        if mask == 0:
            continue
        for existing in masks[:]:
            if existing & mask == 0:
                combined = existing | mask
                masks.append(combined)
                best = max(best, combined.bit_count())
    return best
