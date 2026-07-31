def solve(s: str, dictionary: list[str]) -> int:
    trie: dict[str, dict] = {}
    for word in dictionary:
        node = trie
        for character in reversed(word):
            node = node.setdefault(character, {})
        node["#"] = True

    minimum_extra = [0] + [len(s)] * len(s)

    for end in range(1, len(s) + 1):
        minimum_extra[end] = minimum_extra[end - 1] + 1
        node = trie

        for start in range(end - 1, -1, -1):
            character = s[start]
            if character not in node:
                break
            node = node[character]
            if "#" in node:
                minimum_extra[end] = min(
                    minimum_extra[end], minimum_extra[start]
                )

    return minimum_extra[len(s)]
