# Perfect Squares

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 279 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/perfect-squares/) |

## Problem Description
### Goal
Given a positive integer `n`, express it as a sum of perfect-square integers such as `1`, `4`, `9`, or `16`. The same square may be used more than once, and every term must be the square of an integer.

Return the minimum number of terms among all sums equaling `n` exactly. A perfect-square input requires one term, while other values may have several decompositions with different lengths. The function returns only the smallest count, not the chosen squares or their order, and may not use zero-valued terms to pad a representation.

### Function Contract
**Inputs**

- `n`: a positive integer

**Return value**

The smallest count of square terms summing to `n`.

### Examples
**Example 1**

- Input: `n = 12`
- Output: `3`

**Example 2**

- Input: `n = 13`
- Output: `2`

**Example 3**

- Input: `n = 1`
- Output: `1`
