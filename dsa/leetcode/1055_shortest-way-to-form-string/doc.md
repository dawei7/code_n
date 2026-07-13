# Shortest Way to Form String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1055 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, String, Binary Search, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [shortest-way-to-form-string](https://leetcode.com/problems/shortest-way-to-form-string/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/shortest-way-to-form-string/).

### Goal
Find the minimum number of subsequences of `source` that must be concatenated to form `target`. If any character in `target` cannot be taken from `source`, return `-1`.

### Function Contract
**Inputs**

- `source`: Source string whose subsequences may be reused.
- `target`: Target string to form.

**Return value**

Minimum number of source subsequences needed, or `-1` if impossible.

### Examples
**Example 1**

- Input: `source = "abc", target = "abcbc"`
- Output: `2`

**Example 2**

- Input: `source = "abc", target = "acdbc"`
- Output: `-1`

**Example 3**

- Input: `source = "xyz", target = "xzyxz"`
- Output: `3`

---

## Solution
### Approach
Preprocess `source` into sorted position lists for each character. Walk through `target` while tracking the current position inside the active copy of `source`. For each target character, binary search its next occurrence after the current position.

If no such occurrence exists, start a new subsequence copy and take the first occurrence of that character. If the character does not exist in `source` at all, the target is impossible.

### Complexity Analysis
- **Time Complexity**: `O(m + n log m)`, where `m = len(source)` and `n = len(target)`.
- **Space Complexity**: `O(m)` for the source position lists.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
