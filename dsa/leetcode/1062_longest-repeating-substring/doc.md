# Longest Repeating Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1062 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Binary Search, Dynamic Programming, Rolling Hash, Suffix Array, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [longest-repeating-substring](https://leetcode.com/problems/longest-repeating-substring/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/longest-repeating-substring/).

### Goal
Return the length of the longest non-empty substring that appears at least twice in `s`. The repeated occurrences may overlap.

### Function Contract
**Inputs**

- `s`: Lowercase English string.

**Return value**

Length of the longest repeated substring.

### Examples
**Example 1**

- Input: `s = "abcd"`
- Output: `0`

**Example 2**

- Input: `s = "abbaba"`
- Output: `2`

**Example 3**

- Input: `s = "aabcaabdaab"`
- Output: `3`

---

## Solution
### Approach
Binary search the answer length. To check a candidate length, slide a window across `s` and store each substring or rolling hash in a set. If a window repeats, a repeated substring of that length exists.

The binary search grows the length after a successful check and shrinks it after a failed check. The largest successful length is the answer.

### Complexity Analysis
- **Time Complexity**: `O(n log n)` expected with rolling hash checks.
- **Space Complexity**: `O(n)` for the set used in one check.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
