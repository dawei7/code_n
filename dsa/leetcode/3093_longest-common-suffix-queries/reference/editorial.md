### Approach: Trie

#### Intuition

For information about the Trie data structure, you can refer to the editorial for problem [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/description/?utm_source=chatgpt.com). Before attempting this problem, you should have a basic understanding of Tries.

For each query string, we need to find the string in $\textit{wordsContainer}$ that shares the longest common suffix with it, while also being the shortest and earliest appearing string among all valid candidates. We traverse $\textit{wordsContainer}$ from beginning to end, inserting each string into a trie in reverse order. When processing a query, we also traverse the query string in reverse order within the trie until we can no longer continue. The suffix represented by the last node reached corresponds to the longest common suffix.

However, this alone is not sufficient. We also need to determine which shortest string contains this suffix. Therefore, for each trie node, we record the index of the shortest inserted string that passes through that node. Since we process $\textit{wordsContainer}$ from front to back, ties are naturally resolved in favor of the earliest occurrence.

As a result, the index stored at the node where the traversal of the query string ends is exactly the required answer.

#### Implementation

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.min_len = float("inf")
        self.idx = float("inf")

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s: str, idx: int):
        node = self.root
        if len(s) < node.min_len:
            node.min_len = len(s)
            node.idx = idx

        for ch in s:
            c = ch
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

            if len(s) < node.min_len:
                node.min_len = len(s)
                node.idx = idx

    def query(self, s: str) -> int:
        node = self.root

        for ch in s:
            if ch in node.children:
                node = node.children[ch]
            else:
                break

        return node.idx

class Solution:
    def stringIndices(
        self, wordsContainer: List[str], wordsQuery: List[str]
    ) -> List[int]:
        trie = Trie()

        for i, word in enumerate(wordsContainer):
            reversed_word = word[::-1]
            trie.insert(reversed_word, i)

        res = []
        for query in wordsQuery:
            reversed_query = query[::-1]
            res.append(trie.query(reversed_query))

        return res
```

#### Complexity Analysis

Let $N$ be the sum of the lengths of all strings in $\textit{wordsContainer}$, and let $M$ be the sum of the lengths of all strings in $\textit{wordsQuery}$.

- Time complexity: $O(N + M)$.

- Space complexity: $O(N)$.

  In practice, each trie node stores $\textit{26}$ pointers to its child nodes. This factor affects the actual memory usage, but since it is constant, it is omitted from the asymptotic complexity analysis.

---