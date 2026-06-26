# Maximum Students Taking Exam

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1349 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Bit Manipulation, Matrix, Bitmask |
| Official Link | [maximum-students-taking-exam](https://leetcode.com/problems/maximum-students-taking-exam/) |

## Problem Description & Examples
### Goal
Seat as many students as possible in a classroom grid. Broken seats cannot be used, and no student may sit directly left/right of another student or diagonally behind another student in the previous row.

### Function Contract
**Inputs**

- `seats`: grid of `"."` usable seats and `"#"` broken seats.

**Return value**

The maximum number of students who can take the exam.

### Examples
**Example 1**

- Input: `seats = [["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]]`
- Output: `4`

**Example 2**

- Input: `seats = [[".","#"],["#","#"],["#","."],["#","#"],[".","#"]]`
- Output: `3`

**Example 3**

- Input: `seats = [["#",".",".",".","#"],[".","#",".","#","."],[".",".","#",".","."],[".","#",".","#","."],["#",".",".",".","#"]]`
- Output: `10`

---

## Underlying Base Algorithm(s)
Bitmask dynamic programming by row.

---

## Complexity Analysis
- **Time Complexity**: `O(rows * states^2)` where `states <= 2^cols`.
- **Space Complexity**: `O(states)`
