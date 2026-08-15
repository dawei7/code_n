# Minimize OR of Remaining Elements Using Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3022 |
| Difficulty | Hard |
| Topics | Array, Greedy, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/minimize-or-of-remaining-elements-using-operations/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums` and an integer `k`. In one operation, choose an index `i` with $0 \le i < \lvert\texttt{nums}\rvert - 1$, replace the adjacent values `nums[i]` and `nums[i + 1]` by their bitwise `AND`, and shorten the array by one position. Later operations may combine this new value with another adjacent value.

After performing at most `k` operations, take the bitwise `OR` of every value that remains. Return the minimum value this final `OR` can have. Because every merge combines adjacent values, any final element is the bitwise `AND` of one contiguous segment of the original array.

### Function Contract

**Inputs**

- `nums`: A list of $N$ integers, where $1 \le N \le 10^5$ and $0 \le \texttt{nums[i]} < 2^{30}$.
- `k`: The maximum number of operations, with $0 \le k < N$.

**Return value**

The minimum possible bitwise `OR` of the remaining elements after at most `k` adjacent-`AND` operations.

### Examples

#### Example 1

- **Input:** `nums = [3, 5, 3, 2, 7], k = 2`
- **Output:** `3`

Merging `3 & 5` and separately merging `2 & 7` leaves `[1, 3, 2]`, whose bitwise `OR` is `3`.

#### Example 2

- **Input:** `nums = [7, 3, 15, 14, 2, 8], k = 4`
- **Output:** `2`

Four valid adjacent merges can leave `[2, 0]`, so the final bitwise `OR` is `2`.

#### Example 3

- **Input:** `nums = [10, 7, 10, 3, 9, 14, 9, 4], k = 1`
- **Output:** `15`

The original array already has bitwise `OR` equal to `15`, and one merge cannot produce a smaller result.
