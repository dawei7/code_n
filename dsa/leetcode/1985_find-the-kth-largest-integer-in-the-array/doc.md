# Find the Kth Largest Integer in the Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1985 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-kth-largest-integer-in-the-array](https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/).

### Goal
The array contains non-negative integers written as strings, possibly very long. Find the `k`th largest numeric value.

### Function Contract
**Inputs**

- `nums`: integer strings.
- `k`: one-based rank from largest to smallest.

**Return value**

Return the string representation of the `k`th largest integer.

### Examples
**Example 1**

- Input: `nums = ["3","6","7","10"], k = 4`
- Output: `"3"`

**Example 2**

- Input: `nums = ["2","21","12","1"], k = 3`
- Output: `"2"`

**Example 3**

- Input: `nums = ["0","0"], k = 2`
- Output: `"0"`

---

## Solution
### Approach
Compare numeric strings by length first and lexicographic order second. Sort with that key, or keep a min-heap of size `k`, then select the desired rank.

### Complexity Analysis
- **Time Complexity**: `O(n log n * L)` with sorting, where `L` is max string length.
- **Space Complexity**: `O(n)` for sorting keys/order.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
