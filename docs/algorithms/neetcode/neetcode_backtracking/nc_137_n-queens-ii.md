## Problem Description & Examples
### Goal
The n-queens puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other. Given an integer `n`, return the number of distinct solutions to the n-queens puzzle.

### Function Contract
**Inputs**

- `n`: int

**Return value**

int - number of distinct solutions

### Examples
**Example 1**

- Input: `n = 4`
- Output: `2`

**Example 2**

- Input: `n = 4`
- Output: `2`

**Example 3**

- Input: `n = 2`
- Output: `0`

---

## Underlying Base Algorithm(s)
- [Permutations](backtrack_02_permutations.md)
- [Combination sum](backtrack_03_combination-sum.md)
- [Word break decision](backtrack_04_word-break-decision.md)

---

## Complexity Analysis
- **Time Complexity**: `O(2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
