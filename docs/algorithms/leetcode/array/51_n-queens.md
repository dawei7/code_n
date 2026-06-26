# N-Queens

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_136` |
| Frontend ID | 51 |
| Difficulty | Hard |
| Topics | Array, Backtracking |
| Official Link | [n-queens](https://leetcode.com/problems/n-queens/) |

## Problem Description & Examples
### Goal
The n-queens puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other. Given an integer `n`, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration where `'Q'` and `'.'` indicate a queen and an empty space, respectively.

### Function Contract
**Inputs**

- `n`: int

**Return value**

List[List[str]] - all board solutions

### Examples
**Example 1**

- Input: `n = 4`
- Output: `[[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]`

**Example 2**

- Input: `n = 4`
- Output: `[['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]`

**Example 3**

- Input: `n = 1`
- Output: `[['Q']]`

---

## Underlying Base Algorithm(s)
- [Permutations](backtrack_02_permutations.md)
- [Combination sum](backtrack_03_combination-sum.md)
- [Word break decision](backtrack_04_word-break-decision.md)

---

## Complexity Analysis
- **Time Complexity**: `O(2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
