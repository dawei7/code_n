# Smallest Range II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 910 |
| Difficulty | Medium |
| Topics | Array, Math, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-range-ii/) |

## Problem Description
### Goal
You are given an integer array `nums` and a nonnegative integer `k`. For every index `i`, change `nums[i]` to exactly one of the two values `nums[i] + k` or `nums[i] - k`. Each index makes its choice independently, and every index must be changed according to one of those alternatives.

The score of the resulting array is its maximum element minus its minimum element. Choose the sign used at every index so that this score is as small as possible, and return that minimum score.

### Function Contract
Let $n=\lvert\texttt{nums}\rvert$.

**Inputs**

- `nums`: an integer array with $1 \leq n \leq 10^4$ and $0 \leq \texttt{nums}[i] \leq 10^4$.
- `k`: an integer with $0 \leq \texttt{k} \leq 10^4$.

**Return value**

Return the minimum possible difference between the largest and smallest values after replacing every element by that element plus or minus `k`.

### Examples
**Example 1**

- Input: `nums = [1], k = 0`
- Output: `0`

**Example 2**

- Input: `nums = [0,10], k = 2`
- Output: `6`

Choosing `0 + 2` and `10 - 2` produces `[2,8]`.

**Example 3**

- Input: `nums = [1,3,6], k = 3`
- Output: `3`

One optimal choice produces `[4,6,3]`, whose score is $6-3=3$.
