# Fruit Into Baskets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 904 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/fruit-into-baskets/) |

## Problem Description
### Goal
A farm has one row of fruit trees ordered from left to right. The integer `fruits[i]` identifies the fruit type produced by the tree at index `i`.

You have exactly two baskets. Each basket may hold unlimited fruit but only one fruit type. Choose any starting tree, then move right while picking exactly one fruit from every visited tree, including the start. You must stop when the next fruit type fits in neither basket.

Return the maximum number of fruits that can be collected under these rules.

### Function Contract
Let $n=\lvert\texttt{fruits}\rvert$.

**Inputs**

- `fruits`: an integer array with $1 \leq n \leq 10^5$ and $0 \leq \texttt{fruits}[i] < n$.

**Return value**

Return the length of the longest contiguous subarray containing at most two distinct fruit types.

### Examples
**Example 1**

- Input: `fruits = [1,2,1]`
- Output: `3`

**Example 2**

- Input: `fruits = [0,1,2,2]`
- Output: `3`

Starting at index `1` collects `[1,2,2]`.

**Example 3**

- Input: `fruits = [1,2,3,2,2]`
- Output: `4`

Starting at index `1` collects `[2,3,2,2]`.
