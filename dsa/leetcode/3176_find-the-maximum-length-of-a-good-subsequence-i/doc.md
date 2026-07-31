# Find the Maximum Length of a Good Subsequence I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3176 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/) |

## Problem Description
### Goal
You are given an integer array `nums` and a non-negative integer `k`. A sequence `seq` is called good when there are at most $k$ indices $i$ in the range from $0$ through `seq.length - 2` for which adjacent values differ: `seq[i] != seq[i + 1]`.

Choose a subsequence of `nums`, preserving the relative order of its selected elements. Among every subsequence satisfying the good-sequence condition, return the maximum possible length. Equal adjacent selected values do not consume the change allowance, even when other array elements were skipped between them.

### Function Contract
**Inputs**

- `nums`: A list of $n$ positive integers from which a subsequence may be selected.
- `k`: A non-negative integer giving the maximum allowed number of unequal adjacent pairs in the selected subsequence.

The constraints are $1 \le n \le 500$, $1 \le \texttt{nums[i]} \le 10^9$, and $0 \le k \le \min(n,25)$.

**Return value**

Return the maximum length of a subsequence whose adjacent unequal-pair count is at most $k$.

### Examples
**Example 1**

- Input: `nums = [1, 2, 1, 1, 3], k = 2`
- Output: `4`

For example, `[1, 2, 1, 1]` has two adjacent value changes and length four.

**Example 2**

- Input: `nums = [1, 2, 3, 4, 5, 1], k = 0`
- Output: `2`

Selecting the two occurrences of `1` gives `[1, 1]`, which has no adjacent value change.
