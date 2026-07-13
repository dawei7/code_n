# Missing Number In Arithmetic Progression

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1228 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [missing-number-in-arithmetic-progression](https://leetcode.com/problems/missing-number-in-arithmetic-progression/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/missing-number-in-arithmetic-progression/).

### Goal
Given an arithmetic progression with exactly one interior value removed, return the missing value.

### Function Contract
**Inputs**

- `arr: List[int]` - The remaining values of the arithmetic progression in order.

**Return value**

`int` - The removed value.

### Examples
**Example 1**

- Input: `arr = [5, 7, 11, 13]`
- Output: `9`

**Example 2**

- Input: `arr = [15, 13, 12]`
- Output: `14`

**Example 3**

- Input: `arr = [1, 4, 7, 13]`
- Output: `10`

---

## Solution
### Approach
The original progression has one more element than `arr`, so the common difference is `(arr[-1] - arr[0]) / len(arr)`. Scan adjacent pairs until the difference is not the expected difference; the missing value is the previous element plus the expected difference.

A binary search variant can compare each value with its expected value at that index to find the first shifted position.

### Complexity Analysis
- **Time Complexity**: `O(n)` for the direct scan, or `O(log n)` with the binary search variant.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
