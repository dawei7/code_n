# Make a Positive Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3511 |
| Difficulty | Medium |
| Topics | Array, Greedy, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/make-a-positive-array/) |

## Problem Description

### Goal

An integer array is **positive** when every contiguous subarray containing more than two elements has a strictly positive sum.

In one operation, choose one position and replace its value with any integer in the inclusive range from $-10^{18}$ through $10^{18}$. An operation may be performed on any position, and there is no requirement to preserve the original value.

Determine the minimum number of replacements needed to make the entire array positive.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $3 \le n \le 10^5$ and $-10^9 \le \texttt{nums[i]} \le 10^9$.

**Return value**

Return the minimum number of operations required so that every subarray of length at least three has a sum greater than zero.

### Examples

#### Example 1

- **Input:** `nums = [-10, 15, -12]`
- **Output:** `1`
- **Explanation:** The whole array is the only subarray longer than two elements, and its sum is negative. Replacing one of its entries can make that sum positive.

#### Example 2

- **Input:** `nums = [-1, -2, 3, -1, 2, 6]`
- **Output:** `1`
- **Explanation:** Replacing the value at index `1` with `1` makes every previously non-positive qualifying subarray positive.

#### Example 3

- **Input:** `nums = [1, 2, 3]`
- **Output:** `0`
- **Explanation:** The array already satisfies the condition.
