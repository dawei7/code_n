# Last Substring in Lexicographical Order

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1163 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [last-substring-in-lexicographical-order](https://leetcode.com/problems/last-substring-in-lexicographical-order/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/last-substring-in-lexicographical-order/).

### Goal
Return the lexicographically largest substring of the given string.

### Function Contract
**Inputs**

- `s`: Non-empty lowercase string.

**Return value**

The substring of `s` that is greatest in lexicographic order.

### Examples
**Example 1**

- Input: `s = "abab"`
- Output: `"bab"`

**Example 2**

- Input: `s = "leetcode"`
- Output: `"tcode"`

**Example 3**

- Input: `s = "zzzz"`
- Output: `"zzzz"`

---

## Solution
### Approach
The answer is one of the suffixes of `s`, because extending a chosen start to the end never makes the substring smaller while characters are still available.

Use two candidate start pointers `i` and `j` plus an offset `k`. Compare suffixes character by character; when one suffix loses, skip the losing start and all starts known to share the losing prefix. This is the same linear elimination idea used by Duval-style maximum suffix algorithms.

### Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(1)` beyond the returned substring.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
