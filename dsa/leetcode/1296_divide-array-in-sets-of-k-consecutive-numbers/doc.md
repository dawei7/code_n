# Divide Array in Sets of K Consecutive Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1296 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/) |

## Problem Description
### Goal
Given an integer array `nums` and a positive integer `k`, determine whether every array element can be assigned to a set of exactly `k` consecutive integer values. A set beginning at $x$ must contain $x, x+1, \ldots, x+k-1$, using one occurrence of each value.

The sets form a partition: every occurrence in `nums` must be used once, duplicate values may belong to different sets, and the original array order is irrelevant. Return `true` when such a division exists and `false` otherwise.

### Function Contract
**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.
- `k`: the required size of every set, where $1 \le k \le n$.

**Return value**

`true` if all occurrences can be partitioned into sets of `k` consecutive numbers; otherwise, `false`.

### Examples
**Example 1**

- Input: `nums = [1,2,3,3,4,4,5,6]`, `k = 4`
- Output: `true`
- Explanation: The sets can be `[1,2,3,4]` and `[3,4,5,6]`.

**Example 2**

- Input: `nums = [3,2,1,2,3,4,3,4,5,9,10,11]`, `k = 3`
- Output: `true`
- Explanation: One partition is `[1,2,3]`, `[2,3,4]`, `[3,4,5]`, and `[9,10,11]`.

**Example 3**

- Input: `nums = [1,2,3,4]`, `k = 3`
- Output: `false`
- Explanation: Four elements cannot be split into sets of three.
