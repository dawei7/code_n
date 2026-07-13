# Defuse the Bomb

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1652 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [defuse-the-bomb](https://leetcode.com/problems/defuse-the-bomb/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/defuse-the-bomb/).

### Goal
Replace each circular-array value with the sum of the next `k` values when
`k > 0`, the previous `|k|` values when `k < 0`, or zero when `k == 0`.

### Function Contract
**Inputs**

- `code`: the circular integer array.
- `k`: the direction and count of values to sum.

**Return value**

The transformed array.

### Examples
**Example 1**

- Input: `code = [5, 7, 1, 4], k = 3`
- Output: `[12, 10, 16, 13]`

**Example 2**

- Input: `code = [1, 2, 3, 4], k = 0`
- Output: `[0, 0, 0, 0]`

**Example 3**

- Input: `code = [2, 4, 9, 3], k = -2`
- Output: `[12, 5, 6, 13]`

---

## Solution
### Approach
Use a circular sliding window. For positive `k`, initialize the sum of the next
`k` positions for index `0`, then slide one step at a time. For negative `k`,
do the same over previous positions. A doubled array or modular indexing keeps
wraparound simple.

### Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(1)` extra space besides the result.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
