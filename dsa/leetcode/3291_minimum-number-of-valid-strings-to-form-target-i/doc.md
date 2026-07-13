# Minimum Number of Valid Strings to Form Target I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3291 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Binary Search, Dynamic Programming, Greedy, Trie, Segment Tree, Rolling Hash, String Matching, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-number-of-valid-strings-to-form-target-i](https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/).

### Goal
Given a list of available strings and a target string, determine the minimum number of concatenated substrings (each taken from the available list) required to construct the target string exactly. If it is impossible to form the target, return -1.

### Function Contract
**Inputs**

- `words`: A list of strings representing the available building blocks.
- `target`: The string that needs to be constructed.

**Return value**

- An integer representing the minimum number of concatenated substrings needed, or -1 if the target cannot be formed.

### Examples
**Example 1**

- Input: `words = ["abc","aaaaa","bcfg"], target = "abcdabc"`
- Output: `3`

**Example 2**

- Input: `words = ["ab","abab"], target = "ababa"`
- Output: `2`

**Example 3**

- Input: `words = ["ax","ay","bx","by"], target = "axby"`
- Output: `2`

---

## Solution
### Approach
The problem is solved using a Trie (Prefix Tree) to store all available words, combined with Dynamic Programming. The DP state `dp[i]` represents the minimum number of substrings needed to form the prefix of `target` of length `i`. For each position `i`, we traverse the Trie to find the longest prefix of `target[i:]` that exists as a substring in any of the `words`.

### Complexity Analysis
- **Time Complexity**: `O(N * L + M * L)`, where `N` is the number of words, `L` is the average length of words, and `M` is the length of the target. We build the Trie in `O(N * L)` and perform DP with Trie traversal in `O(M * L)`.
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
    # dp[i] is the min strings to form target[0:i]
    # Initialize with infinity
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(n):
        if dp[i] == float('inf'):
            continue

        # From index i, find all possible valid substrings starting at target[i]
        node = root
        for j in range(i, n):
            if target[j] in node.children:
                node = node.children[target[j]]
                dp[j + 1] = min(dp[j + 1], dp[i] + 1)
            else:
                break

    return dp[n] if dp[n] != float('inf') else -1
```
</details>
