# Minimum Operations to Make Array Sum Divisible by K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3512 |
| Difficulty | Easy |
| Topics | Array, Math |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/) |

## Problem Description

### Goal

You are given an integer array `nums` and a positive integer `k`. In one operation, choose any index `i` and replace `nums[i]` with `nums[i] - 1`. The same or different positions may be selected in later operations, and a position may be decremented repeatedly.

Return the minimum number of operations needed to make the sum of every array element divisible by `k`.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, where $1 \le n \le 1000$ and $1 \le \texttt{nums[i]} \le 1000$.
- `k`: The divisor, where $1 \le k \le 100$.

**Return value**

Return the smallest number of single-unit decrements after which the array sum is a multiple of `k`.

### Examples

#### Example 1

- **Input:** `nums = [3, 9, 7], k = 5`
- **Output:** `4`
- **Explanation:** Four decrements reduce the sum from `19` to `15`, which is divisible by `5`.

#### Example 2

- **Input:** `nums = [4, 1, 3], k = 4`
- **Output:** `0`
- **Explanation:** The initial sum is `8`, already a multiple of `4`.

#### Example 3

- **Input:** `nums = [3, 2], k = 6`
- **Output:** `5`
- **Explanation:** Five decrements can reduce both elements to zero, making the sum divisible by `6`.
