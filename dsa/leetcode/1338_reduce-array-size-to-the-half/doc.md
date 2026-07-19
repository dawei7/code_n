# Reduce Array Size to The Half

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1338 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy, Sorting, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/reduce-array-size-to-the-half/) |

## Problem Description
### Goal
Given an even-length integer array `arr`, choose a set of integer values. For every chosen value, remove all of its occurrences from the array.

Return the minimum possible size of the chosen set such that at least half of the original array elements are removed. Only distinct selected values count toward that size, regardless of how many occurrences each one removes. The values themselves do not need to be returned.

### Function Contract
**Inputs**

- `arr`: an even-length integer array of length $n$, where $2\le n\le10^5$ and $1\le\texttt{arr[i]}\le10^5$.

**Return value**

The smallest number of distinct values whose complete removal deletes at least $n/2$ elements.

### Examples
**Example 1**

- Input: `arr = [3,3,3,3,5,5,5,2,2,7]`
- Output: `2`
- Explanation: Removing all copies of 3 and any suitable additional value removes at least five elements.

**Example 2**

- Input: `arr = [7,7,7,7,7,7]`
- Output: `1`

**Example 3**

- Input: `arr = [1,2,3,4]`
- Output: `2`
- Explanation: Every selected value removes only one element.
