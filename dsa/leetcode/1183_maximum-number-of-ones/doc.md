# Maximum Number of Ones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1183 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Greedy, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-number-of-ones](https://leetcode.com/problems/maximum-number-of-ones/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-number-of-ones/).

### Goal
Fill a `height x width` binary matrix to maximize the number of `1` values while ensuring every `sideLength x sideLength` submatrix contains at most `maxOnes` ones.

### Function Contract
**Inputs**

- `width`: Number of columns.
- `height`: Number of rows.
- `sideLength`: Side length of the constrained square.
- `maxOnes`: Maximum ones allowed inside any such square.

**Return value**

Maximum total number of ones in the full matrix.

### Examples
**Example 1**

- Input: `width = 3`, `height = 3`, `sideLength = 2`, `maxOnes = 1`
- Output: `4`

**Example 2**

- Input: `width = 3`, `height = 3`, `sideLength = 2`, `maxOnes = 2`
- Output: `6`

**Example 3**

- Input: `width = 1`, `height = 1`, `sideLength = 1`, `maxOnes = 1`
- Output: `1`

---

## Solution
### Approach
The optimal matrix repeats a pattern modulo `sideLength` in both dimensions. Each cell of that pattern contributes to several positions in the full matrix; some pattern cells appear more often than others.

For every residue pair `(row % sideLength, col % sideLength)`, count how many full-matrix cells share it. Choose the `maxOnes` largest frequencies and sum them.

### Complexity Analysis
- **Time Complexity**: `O(sideLength^2 log(sideLength^2))`.
- **Space Complexity**: `O(sideLength^2)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
