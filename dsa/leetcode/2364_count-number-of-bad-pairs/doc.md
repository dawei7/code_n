# Count Number of Bad Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2364 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-number-of-bad-pairs/) |

## Problem Description

### Goal

Given the 0-indexed integer array `nums`, consider every index pair
$(i,j)$ with $i<j$. The pair is bad when the index difference $j-i$ is not
equal to the value difference `nums[j] - nums[i]`.

Return the total number of bad pairs. Count pairs of positions, so equal array
values at different indices remain separate elements, and each unordered
choice of two indices is considered only in its increasing-index order.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers.

The constraints are $1\le n\le10^5$ and
$1\le\texttt{nums[i]}\le10^9$.

**Return value**

Return the number of index pairs satisfying the bad-pair inequality. The result
may exceed 32-bit signed range.

### Examples

#### Example 1

- **Input:** `nums = [4,1,3,3]`
- **Output:** `5`

#### Example 2

- **Input:** `nums = [1,2,3,4,5]`
- **Output:** `0`
