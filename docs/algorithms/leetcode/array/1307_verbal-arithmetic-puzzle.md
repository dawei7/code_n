# Verbal Arithmetic Puzzle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1307 |
| Difficulty | Hard |
| Topics | Array, Math, String, Backtracking |
| Official Link | [verbal-arithmetic-puzzle](https://leetcode.com/problems/verbal-arithmetic-puzzle/) |

## Problem Description & Examples
### Goal
Assign a distinct digit to every letter so that the sum of the word numbers equals the result number. No multi-letter number may start with zero.

### Function Contract
**Inputs**

- `words`: addend words.
- `result`: target sum word.

**Return value**

`true` if a valid digit assignment exists, otherwise `false`.

### Examples
**Example 1**

- Input: `words = ["SEND","MORE"]`, `result = "MONEY"`
- Output: `true`

**Example 2**

- Input: `words = ["SIX","SEVEN","SEVEN"]`, `result = "TWENTY"`
- Output: `true`

**Example 3**

- Input: `words = ["LEET","CODE"]`, `result = "POINT"`
- Output: `false`

---

## Underlying Base Algorithm(s)
Column-wise backtracking with carry propagation.

---

## Complexity Analysis
- **Time Complexity**: Exponential in the number of distinct letters, bounded by `10!` assignments.
- **Space Complexity**: `O(U)` for `U` unique letters plus recursion depth.
