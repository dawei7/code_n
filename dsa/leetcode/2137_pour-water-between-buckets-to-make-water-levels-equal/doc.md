# Pour Water Between Buckets to Make Water Levels Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2137 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/pour-water-between-buckets-to-make-water-levels-equal/) |

## Problem Description
### Goal
You have $n$ buckets whose initial water amounts are given in gallons. You may
pour any real-valued quantity from one bucket into another. Whenever $k$
gallons are poured, `loss` percent of $k$ is spilled, so only the remaining
fraction reaches the destination.

Transfer water until every bucket contains the same amount. Determine the
maximum common level that can be achieved. An answer within $10^{-5}$ of the
exact value is accepted.

### Function Contract
**Inputs**

- `buckets`: A list of $n$ integer water amounts with $1\le n\le 10^5$ and
  $0\le \texttt{buckets[i]}\le 10^5$.
- `loss`: The percentage lost from every poured quantity, from `0` through
  `99`.

Let $R=\max(\texttt{buckets})-\min(\texttt{buckets})$ and let $\varepsilon$
denote the required numerical precision.

**Return value**

The maximum equal water level as a floating-point value.

### Examples
**Example 1**

- Input: `buckets = [1,2,7]`, `loss = 80`
- Output: `2.00000`

**Example 2**

- Input: `buckets = [2,4,6]`, `loss = 50`
- Output: `3.50000`

**Example 3**

- Input: `buckets = [3,3,3,3]`, `loss = 40`
- Output: `3.00000`
