# Maximum Score from Performing Multiplication Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1770 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/) |

## Problem Description

### Goal

You are given 0-indexed integer arrays `nums` and `multipliers` of lengths $n$ and $m$, with $n\ge m$. Begin with score $0$ and perform exactly $m$ operations.

During operation `i`, remove either the first or the last remaining value `x` from `nums`, then add `multipliers[i] * x` to the score. Multipliers must be used in their given order, regardless of which ends are chosen.

Return the maximum score attainable after every multiplier has been used.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $1 \le m \le n \le 10^5$.
- `multipliers`: an integer array of length $m$, where $m \le 300$.
- Every value in both arrays lies between $-1000$ and $1000$, inclusive.

**Return value**

- Return the maximum total score after exactly $m$ end-removal operations, using `multipliers[i]` during operation `i`.

### Examples

**Example 1**

- Input: `nums = [1,2,3], multipliers = [3,2,1]`
- Output: `14`
- Explanation: Taking `3`, then `2`, then `1` from the right contributes $9+4+1$.

**Example 2**

- Input: `nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]`
- Output: `102`
- Explanation: One optimal sequence takes three values from the left, then two from the right, exploiting both negative and positive products.

**Example 3**

- Input: `nums = [5,1,4], multipliers = [2,3]`
- Output: `23`
- Explanation: Taking `4` from the right and then `5` from the left gives $8+15$.
