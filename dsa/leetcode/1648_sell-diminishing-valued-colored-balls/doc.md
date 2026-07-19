# Sell Diminishing-Valued Colored Balls

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1648 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Binary Search, Greedy, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sell-diminishing-valued-colored-balls/) |

## Problem Description
### Goal
You manage an inventory of colored balls. The value of a ball is not fixed: at the moment it is sold, its value equals the number of balls of the same color that remain, including that ball. Selling one ball therefore decreases the value of every later ball of that color by one.

Given the starting quantity for every color and the exact number of customer orders, choose which color supplies each order so that the total profit is as large as possible. There are enough balls to fill all orders. Return the maximum profit modulo $10^9 + 7$.

### Function Contract
**Inputs**

- `inventory`: a list of $n$ positive integers, where `inventory[i]` is the initial number of balls of color `i`, $1 \le n \le 10^5$, and $1 \le \texttt{inventory[i]} \le 10^9$.
- `orders`: the exact number of balls to sell, where $1 \le \texttt{orders} \le \min\!\left(\sum_i \texttt{inventory[i]}, 10^9\right)$.

**Return value**

Return the greatest obtainable profit modulo $1{,}000{,}000{,}007$.

### Examples
**Example 1**

- Input: `inventory = [2, 5], orders = 4`
- Output: `14`

Selling from current values 5, 4, 3, and 2 earns $14$.

**Example 2**

- Input: `inventory = [3, 5], orders = 6`
- Output: `19`

**Example 3**

- Input: `inventory = [2, 8, 4, 10, 6], orders = 20`
- Output: `110`
