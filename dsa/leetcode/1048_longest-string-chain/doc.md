# Longest String Chain

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1048 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, String, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [longest-string-chain](https://leetcode.com/problems/longest-string-chain/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/longest-string-chain/).

### Goal
Given a list of words, find the longest chain where each next word can be formed by inserting exactly one character into the previous word.

### Function Contract
**Inputs**

- `words`: List[str]

**Return value**

int - maximum chain length

### Examples
**Example 1**

- Input: `words = ["a", "b", "ba", "bca", "bda", "bdca"]`
- Output: `4`

**Example 2**

- Input: `words = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]`
- Output: `5`

**Example 3**

- Input: `words = ["abcd", "dbqca"]`
- Output: `1`

---

## Solution
### Approach
Dynamic programming over words sorted by length.

### Complexity Analysis
- **Time Complexity**: `O(n * L^2)` where `L` is max word length
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1048: Longest String Chain."""


def solve(words: list[str]) -> int:
    dp: dict[str, int] = {}
    best = 1
    for word in sorted(words, key=len):
        longest = 1
        for i in range(len(word)):
            predecessor = word[:i] + word[i + 1 :]
            longest = max(longest, dp.get(predecessor, 0) + 1)
        dp[word] = longest
        best = max(best, longest)
    return best
```
</details>
