# Delete Columns to Make Sorted III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 960 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [delete-columns-to-make-sorted-iii](https://leetcode.com/problems/delete-columns-to-make-sorted-iii/) |

## Problem Description

### Goal

You are given an array `strs` of $R$ strings, all with the same length $C$. Choose any set of column indices and delete those positions from every string. The undeleted columns keep their original left-to-right order.

After the deletions, each individual row must be in lexicographic order: reading within a row from left to right, every character must be less than or equal to the next one. The rows do not need to be ordered relative to one another. For example, deleting indices `0`, `2`, and `3` from `strs = ["abcdef","uvwxyz"]` leaves `["bef","vyz"]`.

Return the minimum possible number of deleted columns that makes every remaining row lexicographically ordered.

### Function Contract

**Inputs**

- `strs`: a list of $R$ equal-length strings, where $1 \le R \le 100$ and $1 \le C \le 100$.
- Every string consists only of lowercase English letters.

**Return value**

Return the minimum number of common column indices that must be deleted.

### Examples

**Example 1**

- Input: `strs = ["babca","bbazb"]`
- Output: `3`
- Explanation: Deleting columns `0`, `1`, and `4` leaves `["bc","az"]`; both remaining rows are individually ordered.

**Example 2**

- Input: `strs = ["edcba"]`
- Output: `4`

**Example 3**

- Input: `strs = ["ghi","def","abc"]`
- Output: `0`
