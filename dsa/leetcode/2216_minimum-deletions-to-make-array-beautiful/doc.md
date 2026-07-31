# Minimum Deletions to Make Array Beautiful

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2216 |
| Difficulty | Medium |
| Topics | Array, Stack, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/) |

## Problem Description
### Goal

An integer array is beautiful when its length is even and, for every even index $i$, the elements at positions $i$ and $i+1$ are different. The empty array satisfies these conditions and is therefore beautiful.

You may delete any number of elements. After a deletion, all elements to its right shift left by one position while those to its left keep their positions. Return the minimum number of deletions required to make the resulting array beautiful.

### Function Contract
**Inputs**

- `nums`: A nonempty list of nonnegative integers.

Let $n=\lvert\texttt{nums}\rvert$.

**Return value**

Return the minimum number of elements that must be deleted so the remaining array has even length and different values within every pair starting at an even index.

### Examples
**Example 1**

- Input: `nums = [1, 1, 2, 3, 5]`
- Output: `1`

**Example 2**

- Input: `nums = [1, 1, 2, 2, 3, 3]`
- Output: `2`

**Example 3**

- Input: `nums = [1, 2]`
- Output: `0`
