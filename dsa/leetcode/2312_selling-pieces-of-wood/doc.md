# Selling Pieces of Wood

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2312 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Memoization |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [selling-pieces-of-wood](https://leetcode.com/problems/selling-pieces-of-wood/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/selling-pieces-of-wood/).

### Goal
Sell an `m x n` wood board for maximum revenue. A listed dimension may be sold whole at its price, or a board may be cut fully across horizontally or vertically any number of times. Pieces cannot be rotated unless their rotated dimension is separately priced.

### Function Contract
**Inputs**

- `m`, `n`: board dimensions.
- `prices`: triples `[height, width, price]` for directly sellable pieces.

**Return value**

The maximum total revenue obtainable.

### Examples
**Example 1**

- Input: `m = 3`, `n = 5`, `prices = [[1, 4, 2], [2, 2, 7], [2, 1, 3]]`
- Output: `19`

**Example 2**

- Input: `m = 4`, `n = 6`, `prices = [[3, 2, 10], [1, 4, 2], [4, 1, 3]]`
- Output: `32`

**Example 3**

- Input: `m = 1`, `n = 1`, `prices = [[1, 1, 5]]`
- Output: `5`

---

## Solution
### Approach
Use two-dimensional dynamic programming. Initialize `dp[h][w]` with any direct sale price. For every board size, try each horizontal split `x + (h - x)` and vertical split `y + (w - y)`, taking the maximum of direct sale and the sums of the two resulting optimal subboards.

### Complexity Analysis
- **Time Complexity**: `O(mn(m + n))`
- **Space Complexity**: `O(mn)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
