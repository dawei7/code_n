# Profitable Schemes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 879 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/profitable-schemes/) |

## Problem Description
### Goal
A group has `n` members and a list of possible crimes. Crime $i$ produces `profit[i]` profit and requires `group[i]` members. A member who participates in one selected crime cannot participate in another, so a chosen subset cannot require more than `n` members in total.

A profitable scheme is any subset of crimes whose combined profit is at least `minProfit` and whose combined member requirement is at most `n`. Count the distinct qualifying crime subsets and return the result modulo $10^9+7$.

### Function Contract
**Inputs**

- `n`: the available member count, where $1 \leq n \leq 100$.
- `minProfit`: the required profit threshold $P$, where $0 \leq P \leq 100$.
- `group`: an array of $m$ positive member requirements, where $1 \leq m \leq 100$ and $1 \leq \texttt{group[i]} \leq 100$.
- `profit`: an array of the same length, where $0 \leq \texttt{profit[i]} \leq 100$ gives the corresponding crime's profit.

**Return value**

Return the number of subsets whose total members are at most `n` and whose total profit is at least $P$, modulo $10^9+7$.

### Examples
**Example 1**

- Input: `n = 5, minProfit = 3, group = [2,2], profit = [2,3]`
- Output: `2`

Crime `1` alone and the subset containing both crimes qualify.

**Example 2**

- Input: `n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]`
- Output: `7`

Every nonempty subset fits and reaches the profit threshold.

**Example 3**

- Input: `n = 1, minProfit = 0, group = [1], profit = [0]`
- Output: `2`

Both the empty subset and the subset containing the crime meet a zero threshold.
