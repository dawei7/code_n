# Apply Operations to Make All Array Elements Equal to Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2772 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [2772. Apply Operations to Make All Array Elements Equal to Zero](https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums` and a positive integer `k`. In one operation, choose any contiguous subarray containing exactly `k` elements and decrease every value in that subarray by exactly $1$. The operation may be performed any number of times, and the chosen subarray may differ between operations.

Determine whether some sequence of these operations makes every array element equal to $0$. Values cannot be increased, and each operation affects its entire length-$k$ subarray, so reducing one position may also force changes at neighboring positions. Return `True` precisely when an all-zero result is attainable.

### Function Contract

**Inputs**

- `nums`: A list of $n$ non-negative integers.
- `k`: The exact length of every subarray selected by an operation.

The inputs satisfy $1 \le k \le n \le 10^5$ and $0 \le \texttt{nums}[i] \le 10^6$.

**Return value**

Return `True` if repeated legal operations can make every element zero; otherwise return `False`.

### Examples

#### Example 1

- **Input:** `nums = [2, 2, 3, 1, 1, 0], k = 3`
- **Output:** `True`
- **Explanation:** Applying the operation to the first three positions twice and then to positions $2$ through $4$ once produces all zeros.

#### Example 2

- **Input:** `nums = [1, 3, 1, 1], k = 2`
- **Output:** `False`
- **Explanation:** Clearing the first position forces one decrement on the second, after which the remaining values cannot all be cleared with length-$2$ operations.
