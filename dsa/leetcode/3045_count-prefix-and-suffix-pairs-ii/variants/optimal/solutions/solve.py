def solve(words: list[str]) -> int:
    root = {}
    pairs = 0

    for word in words:
        node = root

        for index in range(len(word)):
            character_pair = (word[index], word[-1 - index])
            node = node.setdefault(character_pair, {})
            pairs += node.get(None, 0)

        node[None] = node.get(None, 0) + 1

    return pairs
