# Maximum Total Reward Using Operations I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3180 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Bit Manipulation, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-total-reward-using-operations-i/) |

## Problem Description
### Goal
You are given an integer array `rewardValues`. Its positions represent available rewards, and every index begins unmarked. Your total reward `x` starts at $0$.

You may perform the following operation any number of times: choose an unmarked index `i` whose value `rewardValues[i]` is strictly greater than the current total $x$, add that value to $x$, and mark the chosen index. A marked index cannot be selected again. Return the maximum total reward obtainable by choosing the operations optimally.

### Function Contract
**Inputs**

- `rewardValues`: The positive reward at every initially unmarked index.

Let $n=\lvert\texttt{rewardValues}\rvert$ and $V=\max(\texttt{rewardValues})$. The constraints are $1 \le n \le 2000$ and $1 \le \texttt{rewardValues[i]} \le 2000$.

**Return value**

Return the greatest total reward achievable under the strict-greater-than selection rule.

### Examples
**Example 1**

- Input: `rewardValues = [1, 1, 3, 3]`
- Output: `4`

Choose a reward of $1$ and then a reward of $3$. Their total is $4$, and no other valid sequence produces more.

**Example 2**

- Input: `rewardValues = [1, 6, 4, 3, 2]`
- Output: `11`

Choosing rewards $1$, $4$, and $6$ in that order produces totals $1$, $5$, and $11$.
