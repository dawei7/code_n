# Find Unique Binary String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1980 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-unique-binary-string](https://leetcode.com/problems/find-unique-binary-string/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-unique-binary-string/).

### Goal
Given `n` distinct binary strings of length `n`, construct any binary string of length `n` that is not present in the list.

### Function Contract
**Inputs**

- `nums`: distinct binary strings, each of length `n`.

**Return value**

Return any missing binary string of length `n`.

### Examples
**Example 1**

- Input: `nums = ["01","10"]`
- Output: `"11"`

**Example 2**

- Input: `nums = ["00","01"]`
- Output: `"10"`

**Example 3**

- Input: `nums = ["111","011","001"]`
- Output: `"000"`

---

## Solution
### Approach
Cantor's diagonal idea gives a direct construction: for each index `i`, choose the opposite bit of `nums[i][i]`. The resulting string differs from every input string at least at its own diagonal position.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
