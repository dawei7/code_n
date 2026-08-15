# Buy Two Chocolates

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2706 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/buy-two-chocolates/) |

## Problem Description

### Goal

The integer array `prices` lists the prices of individual chocolates in a store, and `money` is the amount available before shopping. You must buy exactly two distinct chocolates while keeping the remaining balance non-negative.

Choose the affordable pair with the smallest total price and return the money left after buying it. If even the two cheapest chocolates cost more than `money`, no valid purchase exists; in that case, return the original amount unchanged. A zero balance is permitted because the leftover need only be non-negative.

### Function Contract

**Inputs**

- `prices`: An integer array of length $n$, where $2 \le n \le 50$ and $1 \le \texttt{prices[i]} \le 100$.
- `money`: The initial amount, where $1 \le \texttt{money} \le 100$.

**Return value**

Return `money` minus the sum of the two cheapest prices when that sum is affordable; otherwise return `money`.

### Examples

#### Example 1

- **Input:** `prices = [1,2,2]`, `money = 3`
- **Output:** `0`
- **Explanation:** Prices $1$ and $2$ form the cheapest pair and use all available money.

#### Example 2

- **Input:** `prices = [3,2,3]`, `money = 3`
- **Output:** `3`
- **Explanation:** The cheapest pair costs $5$, so buying two chocolates would create debt.

#### Example 3

- **Input:** `prices = [6,4,1,2]`, `money = 10`
- **Output:** `7`
- **Explanation:** Buying the chocolates priced $1$ and $2$ leaves $10-3=7$.
