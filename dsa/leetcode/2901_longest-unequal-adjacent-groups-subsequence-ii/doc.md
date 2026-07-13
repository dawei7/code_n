# Longest Unequal Adjacent Groups Subsequence II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2901 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [longest-unequal-adjacent-groups-subsequence-ii](https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/).

### Goal
Given two arrays of strings and integers, find the longest subsequence such that no two adjacent elements in the subsequence belong to different groups (as defined by the integer array) and satisfy a specific similarity condition: the strings must have the same length and differ by exactly one character (Hamming distance of 1).

### Function Contract
**Inputs**

- `words`: A list of strings representing the available elements.
- `groups`: A list of integers where `groups[i]` is the group ID of `words[i]`.

**Return value**

- A list of strings representing the longest valid subsequence found.

### Examples
**Example 1**

- Input: `words = ["e","a","b"], groups = [0,0,1]`
- Output: `["e","b"]`

**Example 2**

- Input: `words = ["bab","dab","cab"], groups = [1,2,2]`
- Output: `["bab","cab"]`

**Example 3**

- Input: `words = ["a","b","c","d"], groups = [1,2,3,4]`
- Output: `["a","b","c","d"]`

---

## Solution
### Approach
The problem is solved using Dynamic Programming. We maintain a `dp` array where `dp[i]` stores the length of the longest valid subsequence ending at index `i`. To reconstruct the path, we store a `parent` array. The transition condition checks if `groups[i] != groups[j]` and if `words[i]` and `words[j]` have the same length and a Hamming distance of exactly 1.

### Complexity Analysis
- **Time Complexity**: O(n² * L), where n is the number of words and L is the maximum length of a word, due to the nested loops and the string comparison.
- **Space Complexity**: O(n) to store the DP table and the parent pointers.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(words: list[str], groups: list[int]) -> list[str]:
    n = len(words)
    dp = [1] * n
    parent = [-1] * n

    def is_valid(s1, s2):
        if len(s1) != len(s2):
            return False
        diff = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                diff += 1
            if diff > 1:
                return False
        return diff == 1

    for i in range(n):
        for j in range(i):
            if groups[i] != groups[j] and is_valid(words[i], words[j]):
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j

    max_len = 0
    curr = -1
    for i in range(n):
        if dp[i] > max_len:
            max_len = dp[i]
            curr = i

    result = []
    while curr != -1:
        result.append(words[curr])
        curr = parent[curr]

    return result[::-1]
```
</details>
