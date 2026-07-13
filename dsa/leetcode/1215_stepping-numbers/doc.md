# Stepping Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1215 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Backtracking, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [stepping-numbers](https://leetcode.com/problems/stepping-numbers/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/stepping-numbers/).

### Goal
List all stepping numbers in the inclusive range `[low, high]`. A stepping number has adjacent decimal digits whose absolute difference is exactly 1.

### Function Contract
**Inputs**

- `low: int` - Lower bound of the range.
- `high: int` - Upper bound of the range.

**Return value**

`List[int]` - All stepping numbers in the range, in increasing order.

### Examples
**Example 1**

- Input: `low = 0, high = 21`
- Output: `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21]`

**Example 2**

- Input: `low = 10, high = 15`
- Output: `[10, 12]`

**Example 3**

- Input: `low = 90, high = 105`
- Output: `[98, 101]`

---

## Solution
### Approach
Generate candidates with BFS. Start from one-digit numbers `1` through `9`; from a number ending in digit `d`, append `d - 1` and/or `d + 1` when those digits are valid. Add candidates inside the range and stop expanding branches once they exceed `high`. Include `0` separately when it lies in the range, then sort the collected values.

### Complexity Analysis
- **Time Complexity**: `O(s log s)`, where `s` is the number of generated stepping numbers up to `high`; the log factor comes from sorting.
- **Space Complexity**: `O(s)` for the queue and answer.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
