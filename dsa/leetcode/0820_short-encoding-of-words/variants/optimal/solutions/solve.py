def solve(words: list[str]) -> int:
    root: dict[str, dict] = {}
    terminals: list[tuple[dict, int]] = []

    for word in set(words):
        node = root
        for character in reversed(word):
            node = node.setdefault(character, {})
        terminals.append((node, len(word)))

    return sum(length + 1 for node, length in terminals if not node)
