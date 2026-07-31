# Maximum Number of Robots Within Budget

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2398 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Queue, Sliding Window, Heap (Priority Queue), Prefix Sum, Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-robots-within-budget/) |

## Problem Description

### Goal

There are $n$ robots arranged in index order. Robot `i` has a one-time charge
cost `chargeTimes[i]` and a running cost `runningCosts[i]`. You may choose a
contiguous group of $k$ robots rather than arbitrary positions.

The group's total cost is its largest individual charge time plus $k$ times
the sum of all running costs in that group. Given `budget`, find the maximum
possible group length whose total cost does not exceed the budget. Return zero
when even every single-robot group is too expensive.

### Function Contract

**Inputs**

- `chargeTimes`: A list of $n$ positive charge costs.
- `runningCosts`: A list of $n$ positive running costs aligned with
  `chargeTimes`.
- `budget`: The maximum allowed total cost, with
  $1 \le \texttt{budget} \le 10^{15}$.

The shared length satisfies $1 \le n \le 5\cdot10^4$, and every array value is
between 1 and $10^5$, inclusive.

**Return value**

Return the largest length $k$ of a contiguous interval $[l,r]$ satisfying

$$
\max_{l\le i\le r}\texttt{chargeTimes[i]}
+ k\sum_{i=l}^{r}\texttt{runningCosts[i]}
\le \texttt{budget},
$$

where $k=r-l+1$. Return `0` if no nonempty interval qualifies.

### Examples

**Example 1**

- Input: `chargeTimes = [3,6,1,3,4]`,
  `runningCosts = [2,1,3,4,5]`, `budget = 25`
- Output: `3`
- Explanation: The first three robots cost $6 + 3(2+1+3)=24$.

**Example 2**

- Input: `chargeTimes = [11,12,19]`, `runningCosts = [10,8,7]`,
  `budget = 19`
- Output: `0`
- Explanation: Every individual robot already exceeds the budget.

**Example 3**

- Input: `chargeTimes = [9,1,1]`, `runningCosts = [1,1,1]`,
  `budget = 5`
- Output: `2`
- Explanation: After excluding the first robot, the last two cost
  $1 + 2(1+1)=5$.
