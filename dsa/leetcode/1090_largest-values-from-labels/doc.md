# Largest Values From Labels

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1090 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/largest-values-from-labels/) |

## Problem Description

### Goal

There are $n$ items. Item `i` has value `values[i]` and label `labels[i]`, so the two arrays describe the same items by matching index. Values and labels are nonnegative integers.

Choose a subset whose value sum is as large as possible. The subset may contain at most `numWanted` items, and for every label it may contain at most `useLimit` items carrying that label. Return the maximum attainable sum; the subset itself is not required.

### Function Contract

**Inputs**

- `values`: a list of $n$ nonnegative item values, where $1 \le n \le 2\cdot 10^4$.
- `labels`: a length-$n$ list whose entry at each index is that item's nonnegative label.
- `numWanted`: the maximum total number of selected items, from 1 through $n$.
- `useLimit`: the maximum selected count for any one label, from 1 through $n$.

**Return value**

- The greatest possible sum of values among subsets satisfying both selection limits.

### Examples

**Example 1**

- Input: `values = [5, 4, 3, 2, 1]`, `labels = [1, 1, 2, 2, 3]`, `numWanted = 3`, `useLimit = 1`
- Output: `9`

Select values 5, 3, and 1, one from each label.

**Example 2**

- Input: `values = [5, 4, 3, 2, 1]`, `labels = [1, 3, 3, 3, 2]`, `numWanted = 3`, `useLimit = 2`
- Output: `12`

**Example 3**

- Input: `values = [9, 8, 8, 7, 6]`, `labels = [0, 0, 0, 1, 1]`, `numWanted = 3`, `useLimit = 1`
- Output: `16`
