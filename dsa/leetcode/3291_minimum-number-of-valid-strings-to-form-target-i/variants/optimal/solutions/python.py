def solve(words: list[str], target: str) -> int:
    root: dict[str, dict] = {}
    for word in words:
        node = root
        for character in word:
            node = node.setdefault(character, {})

    length = len(target)
    infinity = length + 1
    best = [infinity] * (length + 1)
    best[0] = 0

    for start in range(length):
        if best[start] == infinity:
            continue
        node = root
        candidate = best[start] + 1
        for end in range(start, length):
            node = node.get(target[end])
            if node is None:
                break
            if candidate < best[end + 1]:
                best[end + 1] = candidate

    return -1 if best[length] == infinity else best[length]
