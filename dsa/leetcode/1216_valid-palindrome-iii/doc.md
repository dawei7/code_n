# Valid Palindrome III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1216 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [valid-palindrome-iii](https://leetcode.com/problems/valid-palindrome-iii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/valid-palindrome-iii/).

### Goal
Check whether the string can become a palindrome after deleting at most `k` characters.

### Function Contract
**Inputs**

- `s: str` - Input string.
- `k: int` - Maximum number of deletions allowed.

**Return value**

`bool` - `True` if `s` is a `k`-palindrome, otherwise `False`.

### Examples
**Example 1**

- Input: `s = "abcdeca", k = 2`
- Output: `True`

**Example 2**

- Input: `s = "abbababa", k = 1`
- Output: `True`

**Example 3**

- Input: `s = "abc", k = 1`
- Output: `False`

---

## Solution
### Approach
The minimum deletions needed to form a palindrome equals `len(s) - LPS(s)`, where `LPS` is the longest palindromic subsequence length. Compute `LPS` as the longest common subsequence between `s` and `reversed(s)`, or with interval dynamic programming, and compare the required deletions with `k`.

### Complexity Analysis
- **Time Complexity**: `O(n^2)`, where `n = len(s)`.
- **Space Complexity**: `O(n)` with rolling LCS rows, or `O(n^2)` with a full DP table.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
