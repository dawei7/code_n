# Delete Columns to Make Sorted

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 944 |
| Difficulty | Easy |
| Topics | Array, String |
| Official Link | [LeetCode](https://leetcode.com/problems/delete-columns-to-make-sorted/) |

## Problem Description

### Goal

An array `strs` contains strings of equal length. Place the strings on separate rows in their given order to form a character grid. Each zero-indexed column is read from the top row downward.

A column is lexicographically sorted when its characters are in non-decreasing order from top to bottom. Delete every column that is not sorted in that sense, and return how many columns are deleted. Columns are evaluated independently; deleting one column does not reorder rows or change whether another column is sorted.

### Function Contract

Let $r$ be the number of strings and $c$ their common length.

**Inputs**

- `strs`: a list of $r$ strings with $1 \le r \le 100$.
- Every string has the same length $c$, where $1 \le c \le 1000$, and consists only of lowercase English letters.

**Return value**

Return the number of column indices whose characters are not in non-decreasing lexicographic order from row $0$ through row $r-1$.

### Examples

**Example 1**

- Input: `strs = ["cba", "daf", "ghi"]`
- Output: `1`

Columns `0` and `2` are sorted from top to bottom, but column `1` reads `"bfa"` and must be deleted.

**Example 2**

- Input: `strs = ["a", "b"]`
- Output: `0`

**Example 3**

- Input: `strs = ["zyx", "wvu", "tsr"]`
- Output: `3`

Every column decreases from the first row to the next, so all three columns are deleted.
