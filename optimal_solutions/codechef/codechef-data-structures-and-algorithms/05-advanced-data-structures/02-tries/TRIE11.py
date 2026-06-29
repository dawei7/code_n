


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

        def print_all_words(self):
            current_word = []
            self._print_words_recursive(self.root, current_word)

        def _print_words_recursive(self, node, current_word):
            if node is None:
                return

            if node.isEndOfWord:
                print(''.join(current_word))

            for i in range(self.ALPHABET_SIZE):
                if node.children[i] is not None:
                    current_word.append(chr(ord('a') + i))
                    self._print_words_recursive(node.children[i], current_word)
                    current_word.pop()

        def autocomplete(self, s):
            current = self.root
            for ch in s:
                index = ord(ch) - ord('a')
                if current.children[index] is None:
                    return
                current = current.children[index]
            current_word = list(s)
            self._print_words_recursive(current, current_word)



    if __name__ == "__main__":
        trie = Trie()
        n, s = (input().split())
        n = int(n)
        for i in range(n):
            word = input().strip()
            trie.insert(word)

        trie.autocomplete(s)


if __name__ == "__main__":
    solve()
