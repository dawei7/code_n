# Get Equal Substrings Within Budget

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1208 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Binary Search, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [get-equal-substrings-within-budget](https://leetcode.com/problems/get-equal-substrings-within-budget/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/get-equal-substrings-within-budget/).

### Goal
Given two equal-length strings, find the longest substring that can be changed from `s` to `t` with total character conversion cost at most `maxCost`. Converting one character costs the absolute difference of its character codes.

### Function Contract
**Inputs**

- `s`: Source string.
- `t`: Target string.
- `maxCost`: Maximum allowed total conversion cost.

**Return value**

Maximum valid substring length.

### Examples
**Example 1**

- Input: `s = "abcd"`, `t = "bcdf"`, `maxCost = 3`
- Output: `3`

**Example 2**

- Input: `s = "abcd"`, `t = "cdef"`, `maxCost = 3`
- Output: `1`

**Example 3**

- Input: `s = "abcd"`, `t = "acde"`, `maxCost = 0`
- Output: `1`

---

## Solution
### Approach
Compute each index's conversion cost. Use a sliding window whose sum stays within `maxCost`: expand the right side, and while the sum is too high, remove costs from the left side. Track the largest window length seen.

### Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
