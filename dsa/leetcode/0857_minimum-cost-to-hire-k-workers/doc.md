# Minimum Cost to Hire K Workers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 857 |
| Difficulty | Hard |
| Topics | Array, Greedy, Sorting, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/) |

## Problem Description
### Goal
There are $n$ workers. Worker `i` has quality `quality[i]` and will accept no less than `wage[i]`. Hire exactly $k$ workers and assign their pay subject to two rules: every hired worker receives at least their minimum wage, and all hired workers are paid directly proportionally to their quality.

Find the least total amount that can satisfy both rules for some group of exactly $k$ workers. A result within $10^{-5}$ of the exact minimum is accepted.

### Function Contract
**Inputs**

- `quality`: an array of $n$ positive worker qualities.
- `wage`: an equally long array of positive minimum wages, paired by index with `quality`.
- `k`: the required group size, where $1 \leq k \leq n \leq 10^4$ and $1 \leq \texttt{quality[i]}, \texttt{wage[i]} \leq 10^4$.

**Return value**

Return the minimum total cost as a floating-point number, within absolute error $10^{-5}$.

### Examples
**Example 1**

- Input: `quality = [10,20,5], wage = [70,50,30], k = 2`
- Output: `105.0`

Paying at a rate of $7$ per unit of quality gives the selected workers payments $70$ and $35$.

**Example 2**

- Input: `quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3`
- Output: `30.6666666667`

**Example 3**

- Input: `quality = [5,10,2], wage = [30,20,8], k = 1`
- Output: `8.0`
