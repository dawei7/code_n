# Minimum Array Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3366 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-array-sum/) |

## Problem Description

### Goal

Given a non-negative integer array `nums`, a subtraction amount `k`, and two operation budgets, reduce the array's total as much as possible. Operation 1 replaces one selected value $x$ by $\lceil x/2\rceil$ and may be used at most `op1` times. Operation 2 replaces $x$ by $x-k$, but only while the current value is at least `k`, and may be used at most `op2` times.

Each operation may affect a particular index no more than once. Both operations may affect the same index, and their order matters because the eligibility and result of the second operation are evaluated after the first transformation. Operations are optional; return the minimum total sum obtainable without exceeding either global budget.

### Function Contract

**Inputs**

- `nums`: The non-negative values that may be reduced independently.
- `k`: The fixed amount removed by operation 2 when its current-value condition holds.
- `op1`: The maximum number of indices on which the ceiling-halving operation may be used.
- `op2`: The maximum number of indices on which the subtraction operation may be used.

Let $n=\lvert\texttt{nums}\rvert$. The constraints are $1\le n\le100$, $0\le\texttt{nums[i]}\le10^5$, $0\le k\le10^5$, and $0\le\texttt{op1},\texttt{op2}\le n$.

**Return value**

- The minimum possible sum of all array elements after any legal selection and ordering of operations.

### Examples

**Example 1**

- Input: `nums = [2, 8, 3, 19, 3]`, `k = 3`, `op1 = 1`, `op2 = 1`
- Output: `23`
- Explanation: Subtract 3 from 8 and halve 19 with upward rounding, producing `[2, 5, 3, 10, 3]`.

**Example 2**

- Input: `nums = [2, 4, 3]`, `k = 3`, `op1 = 2`, `op2 = 1`
- Output: `3`
- Explanation: Halve 2 and 4, then subtract 3 from the final element to obtain `[1, 2, 0]`.
