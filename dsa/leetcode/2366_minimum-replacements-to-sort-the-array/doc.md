# Minimum Replacements to Sort the Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2366 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-replacements-to-sort-the-array](https://leetcode.com/problems/minimum-replacements-to-sort-the-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-replacements-to-sort-the-array/).

### Goal
Given a positive integer array, you may replace any single value `x` with several positive integers whose sum is `x`. Find the minimum number of such replacement operations needed so the final flattened array can be read from left to right in nondecreasing order.

### Function Contract
**Inputs**

- `nums`: List[int] of positive values

**Return value**

int - the minimum number of replacement operations

### Examples
**Example 1**

- Input: `nums = [3, 9, 3]`
- Output: `2`

**Example 2**

- Input: `nums = [1, 2, 3, 4]`
- Output: `0`

**Example 3**

- Input: `nums = [12, 7, 6]`
- Output: `4`

---

## Solution
### Approach
Greedy right-to-left splitting with integer ceiling division.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
