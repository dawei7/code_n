# Jump Game VIII

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2297 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Stack, Graph Theory, Monotonic Stack, Shortest Path |
| Official Link | [LeetCode](https://leetcode.com/problems/jump-game-viii/) |

## Problem Description

### Goal

A 0-indexed array `nums` describes $n$ positions, and the walk begins at index
$0$. A forward jump from $i$ to $j$, where $i<j$, is allowed in either of two
cases: if `nums[i] <= nums[j]`, every value strictly between them must be less
than `nums[i]`; or if `nums[i] > nums[j]`, every intervening value must be at
least `nums[i]`.

The parallel array `costs` gives the price of landing at each position:
jumping to $j$ adds `costs[j]`, while the starting position has no charge.
Choose valid forward jumps that reach index $n-1$ and return the minimum total
landing cost.

### Function Contract

**Inputs**

- `nums`: The values that determine which forward jumps are legal.
- `costs`: Nonnegative landing costs for the same $n$ positions.

The arrays have equal length, $1 \le n \le 10^5$, and every entry of either
array is between $0$ and $10^5$ inclusive.

**Return value**

The minimum sum of destination costs along a valid path from index $0$ to
index $n-1$. For $n=1$, return `0`.

### Examples

#### Example 1

- **Input:** `nums = [3, 2, 4, 4, 1], costs = [3, 7, 6, 4, 2]`
- **Output:** `8`

#### Example 2

- **Input:** `nums = [0, 1, 2], costs = [1, 1, 1]`
- **Output:** `2`

#### Example 3

- **Input:** `nums = [7], costs = [100]`
- **Output:** `0`
