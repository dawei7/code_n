"""Optimal solution for LeetCode 1032: Stream of Characters."""


def solve(words: list[str], queries: list[str]) -> list[bool]:
    trie: dict[str, dict] = {}
    max_len = 0
    for word in words:
        max_len = max(max_len, len(word))
        node = trie
        for char in reversed(word):
            node = node.setdefault(char, {})
        node["$"] = {}

    stream: list[str] = []
    answer: list[bool] = []
    for char in queries:
        stream.append(char)
        if len(stream) > max_len:
            stream.pop(0)
        node = trie
        found = False
        for current in reversed(stream):
            if current not in node:
                break
            node = node[current]
            if "$" in node:
                found = True
                break
        answer.append(found)
    return answer
