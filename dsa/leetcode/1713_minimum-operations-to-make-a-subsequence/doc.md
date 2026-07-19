# Minimum Operations to Make a Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1713 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/) |

## Problem Description
### Goal

You are given a `target` array of distinct integers and another array `arr`, which may contain duplicates. In one operation, insert any integer at any position in `arr`, including before its first element or after its last.

Find the fewest insertions needed so that `target` appears as a subsequence of the resulting `arr`. Existing elements cannot be deleted or reordered, but unrelated elements may remain between the selected target values.

### Function Contract
**Inputs**

- `target`: a list of $n$ distinct integers
- `arr`: a list of $m$ integers, possibly with duplicates
- $1 \le n,m \le 10^5$
- every value lies between $1$ and $10^9$

**Return value**

The minimum number of insertions required to make the complete `target` sequence a subsequence of `arr`.

### Examples
**Example 1**

- Input: `target = [5, 1, 3], arr = [9, 4, 2, 3, 4]`
- Output: `2`

Only the final target value `3` is already usable; insert `5` and `1` before it.

**Example 2**

- Input: `target = [6, 4, 8, 1, 3, 2], arr = [4, 7, 6, 2, 3, 8, 6, 1]`
- Output: `3`

Three target values can be retained in their required relative order, so the other three must be inserted.

**Example 3**

- Input: `target = [1, 2, 3], arr = [1, 2, 3]`
- Output: `0`

The target is already a subsequence.
