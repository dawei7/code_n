# Maximum Median Sum of Subsequences of Size 3

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3627 |
| Difficulty | Medium |
| Topics | Array, Math, Greedy, Sorting, Game Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/) |

## Problem Description
### Goal

You are given an integer array `nums` whose length is divisible by three. Empty the array through a sequence of steps. At each step, choose any three remaining elements, compute the median of those three values, and remove all three selected elements.

For an odd-length sequence, the median is the middle value after sorting the sequence in non-decreasing order. Add the median obtained at every removal step and return the maximum total that any sequence of choices can achieve.

### Function Contract
**Inputs**

- `nums`: A list of $n$ positive integers, where $1 \le n \le 5\cdot10^5$, $n$ is divisible by $3$, and $1 \le \texttt{nums[i]} \le 10^9$.

**Return value**

Return the maximum possible sum of the $n/3$ medians.

### Examples
**Example 1**

- Input: `nums = [2,1,3,2,1,3]`
- Output: `5`
- Explanation: Groups with medians 3 and 2 achieve the maximum sum.

**Example 2**

- Input: `nums = [1,1,10,10,10,10]`
- Output: `20`
- Explanation: Each low value can accompany two values of 10, making both medians 10.
