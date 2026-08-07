class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix_count = 0
        self.word_count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for character in word:
            node = node.children.setdefault(character, TrieNode())
            node.prefix_count += 1
        node.word_count += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for character in word:
            if character not in node.children:
                return 0
            node = node.children[character]
        return node.word_count

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for character in prefix:
            if character not in node.children:
                return 0
            node = node.children[character]
        return node.prefix_count

    def erase(self, word: str) -> None:
        node = self.root
        path = []
        for character in word:
            node = node.children[character]
            path.append(node)

        for path_node in path:
            path_node.prefix_count -= 1
        node.word_count -= 1
