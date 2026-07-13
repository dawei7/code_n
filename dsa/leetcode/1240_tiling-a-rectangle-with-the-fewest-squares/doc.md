# Tiling a Rectangle with the Fewest Squares

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1240 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [tiling-a-rectangle-with-the-fewest-squares](https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/).

### Goal
Given rectangle dimensions `n x m`, cover the whole rectangle using the fewest axis-aligned integer-sided squares. Squares may have different sizes and may not overlap.

### Function Contract
**Inputs**

- `n`: int rectangle height
- `m`: int rectangle width

**Return value**

int - minimum number of squares required

### Examples
**Example 1**

- Input: `n = 2, m = 3`
- Output: `3`

**Example 2**

- Input: `n = 5, m = 8`
- Output: `5`

**Example 3**

- Input: `n = 11, m = 13`
- Output: `6`

---

## Solution
### Approach
Backtracking over the first uncovered cell with branch-and-bound pruning.

### Complexity Analysis
- **Time Complexity**: exponential in the rectangle area in the worst case
- **Space Complexity**: `O(n * m)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
