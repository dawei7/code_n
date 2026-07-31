# Count Distinct Numbers on Board

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2549 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [count-distinct-numbers-on-board](https://leetcode.com/problems/count-distinct-numbers-on-board/) |

## Problem Description

### Goal

A positive integer `n` is initially the only value on a board. On each of $10^9$ days, consider every number `x` currently present. For every integer `i` satisfying $1 \le i \le n$ and `x % i == 1`, place `i` on the board as well.

Numbers are never removed, and adding a value already present does not create another distinct value. Return the number of distinct integers on the board after all $10^9$ days have elapsed.

### Function Contract

**Inputs**

- `n`: The positive initial board value and the inclusive upper bound for candidate values `i`.

The constraint is $1 \le n \le 100$.

**Return value**

Return the number of distinct board values after the daily process has run for $10^9$ days.

### Examples

**Example 1**

- Input: `n = 5`
- Output: `4`
- Explanation: The final board contains `2`, `3`, `4`, and `5`.

**Example 2**

- Input: `n = 3`
- Output: `2`
- Explanation: Since `3 % 2 == 1`, the final board contains `2` and `3`.
