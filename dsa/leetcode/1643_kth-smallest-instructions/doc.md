# Kth Smallest Instructions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1643 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/kth-smallest-instructions/) |

## Problem Description
### Goal
Starting at cell $(0,0)$, reach `destination = [row, column]` using only right and down moves. Encode a rightward horizontal move as `H` and a downward vertical move as `V`, so every valid instruction contains exactly `column` copies of `H` and `row` copies of `V`.

Sort all valid instruction strings lexicographically, with the usual character ordering in which `H` precedes `V`. Return the 1-indexed `k`th string in that ordering.

### Function Contract
**Inputs**

- `destination`: `[row, column]`, where $1 \le \texttt{row},\texttt{column} \le 15$.
- `k`: a 1-indexed rank satisfying

$$
1 \le k \le \binom{\texttt{row}+\texttt{column}}{\texttt{row}}.
$$

**Return value**

Return the `k`th lexicographically smallest instruction string that reaches the destination.

### Examples
**Example 1**

- Input: `destination = [2,3], k = 1`
- Output: `"HHHVV"`

**Example 2**

- Input: `destination = [2,3], k = 2`
- Output: `"HHVHV"`

**Example 3**

- Input: `destination = [2,3], k = 3`
- Output: `"HHVVH"`
