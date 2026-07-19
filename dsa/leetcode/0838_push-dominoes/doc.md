# Push Dominoes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 838 |
| Difficulty | Medium |
| Topics | Two Pointers, String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/push-dominoes/) |

## Problem Description
### Goal
A line contains `n` upright dominoes. Initially, some are pushed left and some are pushed right at the same time. After each second, every domino falling left pushes its adjacent upright neighbor on the left, and every domino falling right similarly pushes the adjacent upright neighbor on the right.

If an upright domino receives equal falling forces from both sides, it stays upright. A falling domino exerts no additional force on a domino that is already falling or has fallen. The input string uses `L` for an initial left push, `R` for an initial right push, and `.` for no push. Return the final state after all effects finish.

### Function Contract
**Inputs**

- `dominoes`: a string of length $n$ containing only `L`, `R`, and `.`, where $1 \leq n \leq 10^5$.

**Return value**

Return a string of the same length describing every domino's final left-fallen, right-fallen, or upright state.

### Examples
**Example 1**

- Input: `dominoes = "RR.L"`
- Output: `"RR.L"`

The rightward force has no additional effect on a domino already falling right, and the middle upright domino is balanced.

**Example 2**

- Input: `dominoes = ".L.R...LR..L.."`
- Output: `"LL.RR.LLRRLL.."`

**Example 3**

- Input: `dominoes = "R...L"`
- Output: `"RR.LL"`
