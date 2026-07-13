# Recover the Original Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2122 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, Sorting, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [recover-the-original-array](https://leetcode.com/problems/recover-the-original-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/recover-the-original-array/).

### Goal
Recover an array whose values generated the given even-length multiset. For one unknown positive integer `k`, each original value `x` contributed both `x - k` and `x + k` to `nums`. Any valid original array may be returned.

### Function Contract
**Inputs**

- `nums`: a shuffled array of `2n` integers known to admit at least one valid reconstruction.

**Return value**

One valid length-`n` original array.

### Examples
**Example 1**

- Input: `nums = [2, 10, 6, 4, 8, 12]`
- Output: `[3, 7, 11]`

**Example 2**

- Input: `nums = [1, 1, 3, 3]`
- Output: `[2, 2]`

**Example 3**

- Input: `nums = [5, 435]`
- Output: `[220]`

---

## Solution
### Approach
Sort `nums`. Its smallest value must be the lower member of some pair. Try pairing it with each larger value whose difference is positive and even; that difference determines `2k`. For each candidate, greedily consume the smallest unused value together with the required value `low + 2k` from a frequency map. Record `low + k` for each successful pair and return the first complete reconstruction.

### Complexity Analysis
- **Time Complexity**: `O(n^2)` in the worst case after sorting
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
