# 3Sum With Multiplicity

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 923 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Two Pointers, Sorting, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/3sum-with-multiplicity/) |

## Problem Description
### Goal

You are given an integer array `arr` and an integer `target`. Select three distinct positions whose indices occur in the strict order $i<j<k$. A selection contributes to the answer exactly when `arr[i] + arr[j] + arr[k] == target`; the positions themselves, rather than only their three values, identify the selection.

Count every qualifying index triple. Equal values appearing at different positions can therefore produce several distinct triples, and all of that multiplicity must be included. Because the resulting count may be very large, return it modulo $10^9+7$.

### Function Contract
Let $n$ be the length of `arr`, and let $V=101$ be the number of possible values from $0$ through $100$.

**Inputs**

- `arr`: an array of $n$ integers, where $3 \le n \le 3000$ and every value is from $0$ through $100$.
- `target`: an integer from $0$ through $300$.

**Return value**

The number of ordered index choices $i<j<k$ whose three values sum to `target`, reduced modulo $10^9+7$.

### Examples
**Example 1**

- Input: `arr = [1,1,2,2,3,3,4,4,5,5], target = 8`
- Output: `20`
- Explanation: Value triples `(1,2,5)`, `(1,3,4)`, `(2,2,4)`, and `(2,3,3)` contribute with their index multiplicities.

**Example 2**

- Input: `arr = [1,1,2,2,2,2], target = 5`
- Output: `12`

**Example 3**

- Input: `arr = [2,1,3], target = 6`
- Output: `1`
