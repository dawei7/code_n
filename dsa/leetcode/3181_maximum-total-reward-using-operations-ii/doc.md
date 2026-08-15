# Maximum Total Reward Using Operations II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3181 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Bit Manipulation, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-total-reward-using-operations-ii/) |

## Problem Description

### Goal

You are given an integer array `rewardValues`, where every position is an available reward and all indices are initially unmarked. Your accumulated reward `x` begins at $0$.

You may repeat the following operation any number of times. Choose an unmarked index `i` only when `rewardValues[i]` is strictly greater than the current total $x$. Add that reward to $x$ and mark its index so it cannot be selected again. Return the largest total reward attainable by choosing a valid sequence optimally.

### Function Contract

**Inputs**

- `rewardValues`: The positive reward stored at each initially unmarked index.

Let $n=\lvert\texttt{rewardValues}\rvert$ and $V=\max(\texttt{rewardValues})$. The constraints are $1 \le n \le 5\cdot10^4$ and $1 \le \texttt{rewardValues[i]} \le 5\cdot10^4$.

**Return value**

Return the maximum final value of $x$ allowed by the strict-greater-than selection rule.

### Examples

#### Example 1

- **Input:** `rewardValues = [1, 1, 3, 3]`
- **Output:** `4`

Select a reward of $1$, then a reward of $3$. The resulting total is $4$, which is optimal.

#### Example 2

- **Input:** `rewardValues = [1, 6, 4, 3, 2]`
- **Output:** `11`

The rewards $1$, $4$, and $6$ can be chosen in that order, producing totals $1$, $5$, and $11$.
