# Minimum Cost to Make Array Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2448 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Greedy, Sorting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Minimum Cost to Make Array Equal](https://leetcode.com/problems/minimum-cost-to-make-array-equal/) |

## Problem Description

### Goal

You are given two 0-indexed arrays, `nums` and `cost`, of the same length. Both contain positive integers. In one operation, you may choose any position and increase or decrease its value in `nums` by exactly 1. An operation performed at index `i` costs `cost[i]`, regardless of its direction.

You may perform any number of operations, possibly none. Return the minimum total cost required to make every element of `nums` equal to one common integer. The chosen common value is not supplied and must be selected as part of the optimization.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^6$.
- `cost`: A list of $n$ positive per-operation costs, where $\lvert\texttt{cost}\rvert=n$ and $1 \le \texttt{cost[i]} \le 10^6$.

The test data guarantees that the result does not exceed $2^{53}-1$.

**Return value**

- The minimum total cost needed to make all values in `nums` equal.

### Examples

#### Example 1

- **Input:** `nums = [1, 3, 5, 2], cost = [2, 3, 1, 14]`
- **Output:** `8`
- **Explanation:** Choosing 2 costs 2 to move the first value, 3 to move the second, and 3 to move the third.

#### Example 2

- **Input:** `nums = [2, 2, 2, 2, 2], cost = [4, 2, 8, 1, 3]`
- **Output:** `0`
- **Explanation:** Every value is already equal.
