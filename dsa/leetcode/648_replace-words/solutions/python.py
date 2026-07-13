TERMINAL = "#"


def solve(dictionary: list[str], sentence: str) -> str:
    trie: dict = {}
    for root in dictionary:
        node = trie
        for character in root:
            node = node.setdefault(character, {})
        node[TERMINAL] = True

    def replacement(word: str) -> str:
        node = trie
        for index, character in enumerate(word):
            if character not in node:
                return word
            node = node[character]
            if TERMINAL in node:
                return word[: index + 1]
        return word

    return " ".join(replacement(word) for word in sentence.split())
