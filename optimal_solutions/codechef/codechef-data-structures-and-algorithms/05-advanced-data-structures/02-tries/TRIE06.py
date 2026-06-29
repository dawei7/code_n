


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

        def delete_word(self, word):
            self._delete_word_recursive(self.root, word, 0)

        def _delete_word_recursive(self, node, word, depth):
            if node is None:
                return False

            if depth == len(word):
                if not node.isEndOfWord:
                    return False  # Word not present in the trie

                node.isEndOfWord = False

                # If the node has no children, it can be safely removed
                return self._node_has_no_children(node)

            index = ord(word[depth]) - ord('a')
            if self._delete_word_recursive(node.children[index], word, depth + 1):
                # Delete the child node if it can be deleted
                node.children[index] = None

                # Check if the current node has no children and is not an end-of-word node
                return self._node_has_no_children(node)

            return False

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


    if __name__ == "__main__":
        trie = Trie()
        n = int(input().strip())

        for _ in range(n):
            command = list(map(str, input().split()))

            if command[0] == "insert":
                word = command[1]
                trie.insert(word)
            elif command[0] == "words":
                trie.print_all_words()
            elif command[0] == "search":
                word = command[1]
                if trie.search(word):
                    print("present")
                else:
                    print("not present")
            elif command[0] == "delete":
                word = command[1]
                trie.delete_word(word)


if __name__ == "__main__":
    solve()
