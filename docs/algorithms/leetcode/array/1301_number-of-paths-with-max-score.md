# Number of Paths with Max Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1301 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [number-of-paths-with-max-score](https://leetcode.com/problems/number-of-paths-with-max-score/) |

## Problem Description & Examples
### Goal
On a square board, move from `S` at the bottom-right to `E` at the top-left using up, left, or diagonal up-left moves. Avoid obstacles and maximize the sum of digit cells visited. Return the maximum score and the number of maximum-score paths.

### Function Contract
**Inputs**

- `board`: list of strings containing digits, `S`, `E`, and obstacles `X`.

**Return value**

`[maxScore, pathCount]`, modulo `1_000_000_007` for the path count. Return `[0,0]` if no path exists.

### Examples
**Example 1**

- Input: `board = ["E23","2X2","12S"]`
- Output: `[7,1]`

**Example 2**

- Input: `board = ["E12","1X1","21S"]`
- Output: `[4,2]`

**Example 3**

- Input: `board = ["E11","XXX","11S"]`
- Output: `[0,0]`

---

## Underlying Base Algorithm(s)
Grid dynamic programming with score/count pairs.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n^2)`
