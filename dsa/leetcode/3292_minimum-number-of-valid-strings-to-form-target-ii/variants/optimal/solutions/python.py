class TrieNode:
    def __init__(self):
        self.children = {}

def solve(words: list[str], target: str) -> int:
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

    n = len(target)
    # max_match[i] stores the length of the longest prefix of any word
    # that matches target starting at index i
    max_match = [0] * n
    for i in range(n):
        node = root
        length = 0
        for j in range(i, n):
            if target[j] in node.children:
                node = node.children[target[j]]
                length += 1
            else:
                break
        max_match[i] = length

    count = 0
    farthest = 0
    current_end = 0
    i = 0

    while current_end < n:
        while i <= current_end and i < n:
            farthest = max(farthest, i + max_match[i])
            i += 1

        if farthest <= current_end:
            return -1

        count += 1
        current_end = farthest

    return count
