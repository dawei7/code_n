# Maximum Students Taking Exam

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1349 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Matrix, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/maximum-students-taking-exam/) |

## Problem Description

### Goal

A classroom is represented by a rectangular grid `seats`. A `"."` marks a usable seat, while a `"#"` marks a broken seat where nobody can sit.

Students can see answers from another student seated immediately to their left or right in the same row, or diagonally to the upper-left or upper-right in the previous row. They cannot see directly in front of or behind themselves. Choose usable seats so that no seated student can cheat under these rules, and return the maximum number of students who can take the exam.

### Function Contract

**Inputs**

- `seats`: a nonempty $m \times n$ grid containing only `"."` and `"#"`.
- $m$ is the number of rows and $n$ is the number of columns.

**Return value**

- Return the largest number of usable seats that can be occupied without any horizontal or upper-diagonal conflict.

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
