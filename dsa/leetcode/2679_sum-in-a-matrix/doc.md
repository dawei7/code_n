# Sum in a Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2679 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting, Heap (Priority Queue), Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/sum-in-a-matrix/) |

## Problem Description

### Goal

Start with score zero and a 0-indexed rectangular integer matrix `nums`. Repeatedly remove one value from every row until the matrix is empty. During each round, the removed value from a row must be one of that row's current largest values; ties may be resolved arbitrarily. Add the largest value removed across all rows in that round to the score.

Return the score after every value has been removed.

### Function Contract

**Inputs**

- `nums`: A matrix with 1 through 300 rows and 1 through 500 columns per row. Every entry is an integer from 0 through $10^3$.

**Return value**

Return the sum of the largest row-removal value from every round.

### Examples

#### Example 1

- **Input:** `nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]`
- **Output:** `15`
- **Explanation:** The round maxima added to the score are 7, 5, and 3.

#### Example 2

- **Input:** `nums = [[1]]`
- **Output:** `1`
