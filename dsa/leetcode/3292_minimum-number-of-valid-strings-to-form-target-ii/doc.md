# Minimum Number of Valid Strings to Form Target II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3292 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Binary Search, Dynamic Programming, Greedy, Segment Tree, Rolling Hash, String Matching, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-number-of-valid-strings-to-form-target-ii](https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/).

### Goal
Given a list of available strings and a target string, determine the minimum number of valid strings (prefixes of the provided words) required to concatenate and form the target string. If it is impossible to construct the target, return -1.

### Function Contract
**Inputs**

- `words`: A list of strings representing the available building blocks.
- `target`: The string that needs to be constructed.

**Return value**

- An integer representing the minimum number of concatenated prefixes needed, or -1 if construction is impossible.

### Examples
**Example 1**

- Input: `words = ["abc","aaaaa","bcfg"], target = "abcdabc"`
- Output: `3`

**Example 2**

- Input: `words = ["ab","abab"], target = "ababa"`
- Output: `2`

**Example 3**

- Input: `words = ["abcdef"], target = "xyz"`
- Output: `-1`

---

## Solution
### Approach
The problem is solved using a combination of a **Trie** (to store prefixes of `words`) and **Dynamic Programming** (to find the minimum count). To optimize the search for the longest prefix match at each position, we use the Trie to find the maximum length `k` such that `target[i:i+k]` is a prefix of some word in `words`. We then use a greedy approach with DP or a jump-table strategy to minimize the total segments.

### Complexity Analysis
- **Time Complexity**: `O(N * L + M * log(max_len))`, where `N` is the number of words, `L` is the average length of words, `M` is the length of the target, and `max_len` is the maximum length of a word.
- **Space Complexity**: `O(N * L)` to store the Trie structure.

### Reference Implementations
<details>
<summary>python</summary>

```python
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
```
</details>
