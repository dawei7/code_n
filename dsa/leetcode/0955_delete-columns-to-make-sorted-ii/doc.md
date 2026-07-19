# Delete Columns to Make Sorted II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 955 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [delete-columns-to-make-sorted-ii](https://leetcode.com/problems/delete-columns-to-make-sorted-ii/) |

## Problem Description

### Goal

You are given `strs`, an array of strings that all have the same length. Choose a set of column indices and delete every chosen column from every string; all undeleted characters retain their original left-to-right order.

After the deletions, the array of resulting strings must be in lexicographic non-decreasing order, so each row is no greater than the row immediately after it. The characters inside an individual row do not themselves need to be sorted. Return the minimum number of columns that must be deleted to satisfy the row ordering.

### Function Contract

Let $N$ be the number of strings and $M$ their common length.

**Inputs**

- `strs`: a list of $N$ lowercase English strings of equal length $M$, where $1 \le N,M \le 100$.

**Return value**

Return the minimum number of common column deletions needed to make `strs` lexicographically non-decreasing.

### Examples

**Example 1**

- Input: `strs = ["ca","bb","ac"]`
- Output: `1`
- Explanation: Deleting the first column leaves `["a","b","c"]`.

**Example 2**

- Input: `strs = ["xc","yb","za"]`
- Output: `0`
- Explanation: The rows are already in lexicographic order.

**Example 3**

- Input: `strs = ["zyx","wvu","tsr"]`
- Output: `3`
- Explanation: Every column must be deleted.
