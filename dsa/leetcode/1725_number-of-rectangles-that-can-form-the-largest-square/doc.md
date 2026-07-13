# Number Of Rectangles That Can Form The Largest Square

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1725 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-rectangles-that-can-form-the-largest-square](https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/).

### Goal
Each rectangle can form a square whose side length is the smaller of its two dimensions. Count how many rectangles can form the largest possible square side length.

### Function Contract
**Inputs**

- `rectangles`: a list of `[length, width]` pairs.

**Return value**

Return the number of rectangles whose maximum square side equals the largest side achievable by any rectangle.

### Examples
**Example 1**

- Input: `rectangles = [[5,8],[3,9],[5,12],[16,5]]`
- Output: `3`

**Example 2**

- Input: `rectangles = [[2,3],[3,7],[4,3],[3,7]]`
- Output: `3`

**Example 3**

- Input: `rectangles = [[1,1],[2,2],[3,1]]`
- Output: `1`

---

## Solution
### Approach
For each rectangle, compute `side = min(length, width)`. Track the largest side seen and how many rectangles achieve it. When a larger side appears, reset the count to one; when the side equals the current best, increment the count.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
