# Number of Good Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1512 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Math, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-good-pairs/) |

## Problem Description
### Goal

Given an integer array `nums`, count its good index pairs. A pair $(i,j)$ is good exactly when $i<j$ and `nums[i] == nums[j]`.

The order condition means each two equal occurrences contributes once, with the earlier index first. Equal values may be separated by any number of other elements; only their values and index order matter. Return the total across every value in the array, counting pairs from repeated groups independently.

### Function Contract
**Inputs**

Let $n$ be the length of `nums` and $u$ the number of distinct values it contains.

- `nums`: An integer array with $1 \leq n \leq 100$.
- Every value satisfies $1 \leq \texttt{nums[i]} \leq 100$.
- Indices are distinct positions; equal occurrences at different positions may form a pair.

**Return value**

Return the number of pairs $(i,j)$ satisfying both $i<j$ and `nums[i] == nums[j]`.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 1, 1, 3]`
- Output: `4`
- Explanation: Value 1 contributes three pairs and value 3 contributes one.

**Example 2**

- Input: `nums = [1, 1, 1, 1]`
- Output: `6`
- Explanation: Every choice of two of the four indices is good.

**Example 3**

- Input: `nums = [1, 2, 3]`
- Output: `0`
