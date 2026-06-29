


def solve():
    class Trie:
        ALPHABET_SIZE = 26

        class TrieNode:
            def __init__(self):
                self.children = [None] * Trie.ALPHABET_SIZE
                self.isEndOfWord = False

        def __init__(self):
            self.root = self.TrieNode()

        def insert(self, word):
            current = self.root
            for ch in word:
                index = ord(ch) - ord('a')
                if current.children[index] is None:
                    current.children[index] = self.TrieNode()
                current = current.children[index]
            current.isEndOfWord = True


        def _node_has_no_children(self, node):
            return all(child is None for child in node.children) and not node.isEndOfWord

        def search(self, word):
            node = self._search_node(word)
            return node is not None and node.isEndOfWord

        def _search_node(self, word):
            current = self.root
            for ch in word:
                index = ord(ch) - ord('a')
                if current.children[index] is None:
                    return None  # Character not found in the trie
                current = current.children[index]
            return current



    if __name__ == "__main__":
        trie = Trie()
        n = int(input())
        for _ in range(n):
            trie.insert(input())
        m = int(input())
        for _ in range(m):
            if trie.search(input()):
                print("correct")
            else:
                print("incorrect")


if __name__ == "__main__":
    solve()
