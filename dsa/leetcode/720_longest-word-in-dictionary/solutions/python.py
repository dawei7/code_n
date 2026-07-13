class _Node:
    def __init__(self):
        self.children = [None] * 26
        self.word = None


def solve(words: list[str]) -> str:
    root = _Node()

    for word in words:
        node = root
        for character in word:
            index = ord(character) - ord("a")
            if node.children[index] is None:
                node.children[index] = _Node()
            node = node.children[index]
        node.word = word

    best = ""
    stack = [root]

    while stack:
        node = stack.pop()
        if node.word is not None and (
            len(node.word) > len(best)
            or (len(node.word) == len(best) and node.word < best)
        ):
            best = node.word

        for child in node.children:
            if child is not None and child.word is not None:
                stack.append(child)

    return best
