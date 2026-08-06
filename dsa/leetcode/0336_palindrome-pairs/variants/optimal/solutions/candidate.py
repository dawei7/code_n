class _TrieNode:
    def __init__(self):
        self.children: dict[str, "_TrieNode"] = {}
        self.terminal = -1
        self.palindrome_remainders: list[int] = []


def _palindrome_boundaries(word: str) -> tuple[list[bool], list[bool]]:
    n = len(word)
    prefix = [False] * (n + 1)
    suffix = [False] * (n + 1)
    prefix[0] = True
    suffix[n] = True

    text = "|" + "|".join(word) + "|"
    radii = [0] * len(text)
    center = 0
    right = -1
    for i in range(len(text)):
        k = 0 if i > right else min(radii[2 * center - i], right - i)
        while i - k - 1 >= 0 and i + k + 1 < len(text) and text[i - k - 1] == text[i + k + 1]:
            k += 1
        radii[i] = k
        l = i - k
        r = i + k
        if l == 0:
            prefix[(r + 1) // 2] = True
        if r == len(text) - 1:
            suffix[l // 2] = True
        if r > right:
            center = i
            right = r

    return prefix, suffix


def solve(words: list[str]) -> list[list[int]]:
    boundaries = [_palindrome_boundaries(word) for word in words]
    root = _TrieNode()

    for i, word in enumerate(words):
        prefix, _ = boundaries[i]
        node = root
        for j in range(len(word) - 1, -1, -1):
            if prefix[j + 1]:
                node.palindrome_remainders.append(i)
            child = node.children.get(word[j])
            if child is None:
                child = _TrieNode()
                node.children[word[j]] = child
            node = child
        node.terminal = i
        node.palindrome_remainders.append(i)

    pairs = []
    for i, word in enumerate(words):
        _, suffix = boundaries[i]
        node = root
        for j, character in enumerate(word):
            if node.terminal >= 0 and node.terminal != i and suffix[j]:
                pairs.append([i, node.terminal])
            node = node.children.get(character)
            if node is None:
                break
        else:
            for partner in node.palindrome_remainders:
                if partner != i:
                    pairs.append([i, partner])
    return pairs
