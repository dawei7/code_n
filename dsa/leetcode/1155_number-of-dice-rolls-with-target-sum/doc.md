# Number of Dice Rolls With Target Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1155 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/) |

## Problem Description

### Goal

You have $n$ dice. Every die has $k$ faces numbered from $1$ through $k$, and one face-up number is produced by each roll.

Among the $k^n$ possible ordered roll outcomes, count how many have face-up numbers whose sum is exactly `target`. Outcomes that assign different values to individual dice are different ways, even when their totals agree. Because the count can be very large, return it modulo $10^9 + 7$.

### Function Contract

**Inputs**

- `n`: The number of dice, with $1 \le n \le 30$.
- `k`: The number of faces on every die, with $1 \le k \le 30$; the available values are the integers from $1$ through $k$.
- `target`: The required sum, with $1 \le \texttt{target} \le 1000$.

**Return value**

- The number of ordered roll outcomes whose sum is exactly `target`, reduced modulo $10^9 + 7$.

### Examples

**Example 1**

- Input: `n = 1`, `k = 6`, `target = 3`
- Output: `1`

**Example 2**

- Input: `n = 2`, `k = 6`, `target = 7`
- Output: `6`

The six ordered outcomes are `(1, 6)`, `(2, 5)`, `(3, 4)`, `(4, 3)`, `(5, 2)`, and `(6, 1)`.

**Example 3**

- Input: `n = 30`, `k = 30`, `target = 500`
- Output: `222616187`
