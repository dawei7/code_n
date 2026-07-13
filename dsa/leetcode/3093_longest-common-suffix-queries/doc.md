# Longest Common Suffix Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3093 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [longest-common-suffix-queries](https://leetcode.com/problems/longest-common-suffix-queries/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/longest-common-suffix-queries/).

### Goal
Given two arrays of strings, `wordsContainer` and `wordsQuery`, determine the index of the string in `wordsContainer` that shares the longest common suffix with each string in `wordsQuery`. If multiple strings in `wordsContainer` share the same maximum suffix length, choose the one with the minimum length. If there is still a tie, choose the one with the smallest original index.

### Function Contract
**Inputs**

- `wordsContainer`: A list of strings representing the dictionary to search within.
- `wordsQuery`: A list of strings representing the queries to perform.

**Return value**

- A list of integers where each integer corresponds to the index of the best-matching string in `wordsContainer` for the respective query in `wordsQuery`.

### Examples
**Example 1**

- Input: `wordsContainer = ["abcd","bcd","xbcd"], wordsQuery = ["cd","bcd","xyz"]`
- Output: `[1,1,1]`

**Example 2**

- Input: `wordsContainer = ["abcdef","bcd","xyz"], wordsQuery = ["xyz","abc"]`
- Output: `[2,0]`

**Example 3**

- Input: `wordsContainer = ["a","b","c"], wordsQuery = ["d","e","f"]`
- Output: `[0,0,0]`

---

## Solution
### Approach
The problem is solved using a **Trie (Prefix Tree)**. Since we are matching suffixes, we insert the reversed strings of `wordsContainer` into the Trie. Each node in the Trie stores the index of the "best" string encountered so far that passes through that node (based on the criteria: longest suffix, shortest length, smallest index). During query time, we reverse the query string and traverse the Trie until we can no longer match characters, returning the index stored at the last reachable node.

### Complexity Analysis
- **Time Complexity**: $O(N \cdot L + M \cdot K)$, where $N$ is the number of words in `wordsContainer`, $L$ is the average length of these words, $M$ is the number of queries, and $K$ is the average length of query strings.
- **Space Complexity**: $O(N \cdot L \cdot \Sigma)$, where $\Sigma$ is the alphabet size (26), representing the space required to store the Trie nodes.

### Reference Implementations
<details>
<summary>python</summary>

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        # Stores (length_of_word, index_in_container)
        self.best = (float('inf'), float('inf'))

def solve(wordsContainer, wordsQuery):
    root = TrieNode()

    def insert(word, index):
        length = len(word)
        node = root
        # Update root if this word is better than current best
        if (length, index) < node.best:
            node.best = (length, index)

        # Insert reversed word
        for char in reversed(word):
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            if (length, index) < node.best:
                node.best = (length, index)

    # Build the Trie
    for i, word in enumerate(wordsContainer):
        insert(word, i)

    results = []
    for query in wordsQuery:
        node = root
        # Traverse Trie with reversed query
        for char in reversed(query):
            if char in node.children:
                node = node.children[char]
            else:
                break
        results.append(node.best[1])

    return results
```
</details>
