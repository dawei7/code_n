"""Signature-grouped prefix tries for LeetCode 527."""


class _TrieNode:
    __slots__ = ("children", "count")

    def __init__(self) -> None:
        self.children: dict[str, _TrieNode] = {}
        self.count = 0


def _abbreviate(word: str, prefix_length: int) -> str:
    omitted = len(word) - prefix_length - 1
    if omitted <= 1:
        return word
    return f"{word[:prefix_length]}{omitted}{word[-1]}"


def solve(words: list[str]) -> list[str]:
    roots: dict[tuple[int, str, str], _TrieNode] = {}
    for word in words:
        signature = (len(word), word[0], word[-1])
        node = roots.setdefault(signature, _TrieNode())
        for character in word:
            node = node.children.setdefault(character, _TrieNode())
            node.count += 1

    answer: list[str] = []
    for word in words:
        node = roots[(len(word), word[0], word[-1])]
        prefix_length = 0
        for character in word:
            node = node.children[character]
            prefix_length += 1
            if node.count == 1:
                break
        answer.append(_abbreviate(word, prefix_length))
    return answer
