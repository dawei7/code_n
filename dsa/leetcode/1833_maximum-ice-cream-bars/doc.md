# Maximum Ice Cream Bars

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-ice-cream-bars/) |
| Frontend ID | 1833 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting, Counting Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A store has $n$ ice cream bars. Entry `costs[i]` gives the positive number of coins required to buy the $i$th bar, and a buyer has exactly `coins` coins available. Each bar can be bought at most once, but the bars may be selected in any order.

Return the greatest number of bars that can be purchased without spending more than the available budget. Solve the problem using counting sort rather than a comparison sort.

### Function Contract

**Inputs**

- `costs`: an array of $n$ positive prices, where $1 \le n \le 10^5$ and $1 \le \texttt{costs[i]} \le 10^5$.
- `coins`: the available budget, where $1 \le \texttt{coins} \le 10^8$.
- Let $M = \max(\texttt{costs})$.

**Return value**

- Return the maximum number of distinct bars whose total price is at most `coins`.

### Examples

**Example 1**

- Input: `costs = [1,3,2,4,1], coins = 7`
- Output: `4`

Buying bars priced 1, 1, 2, and 3 uses all 7 coins.

**Example 2**

- Input: `costs = [10,6,8,7,7,8], coins = 5`
- Output: `0`

Even the least expensive bar costs more than the budget.

**Example 3**

- Input: `costs = [1,6,3,1,2,5], coins = 20`
- Output: `6`

All six bars cost 18 coins in total.
