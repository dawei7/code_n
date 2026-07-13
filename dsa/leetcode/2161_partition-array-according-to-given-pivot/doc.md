# Partition Array According to Given Pivot

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2161 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [partition-array-according-to-given-pivot](https://leetcode.com/problems/partition-array-according-to-given-pivot/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/partition-array-according-to-given-pivot/).

### Goal
Stably partition an array around a pivot: values smaller than the pivot come first, values equal to it come next, and values greater than it come last. Preserve relative order within the smaller and greater groups.

### Function Contract
**Inputs**

- `nums`: an integer array.
- `pivot`: a value known to occur in `nums`.

**Return value**

The stably partitioned array.

### Examples
**Example 1**

- Input: `nums = [9, 12, 5, 10, 14, 3, 10]`, `pivot = 10`
- Output: `[9, 5, 3, 10, 10, 12, 14]`

**Example 2**

- Input: `nums = [-3, 4, 3, 2]`, `pivot = 2`
- Output: `[-3, 2, 4, 3]`

**Example 3**

- Input: `nums = [1, 1, 1]`, `pivot = 1`
- Output: `[1, 1, 1]`

---

## Solution
### Approach
Scan the input three times, appending values less than, equal to, and greater than the pivot respectively. Appending in encounter order guarantees stability. The three passes remain linear.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` for the returned array

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
