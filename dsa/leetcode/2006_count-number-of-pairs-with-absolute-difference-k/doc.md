# Count Number of Pairs With Absolute Difference K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2006 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/) |

## Problem Description

### Goal

Given an integer array `nums` and a positive integer `k`, count the index pairs
$(i,j)$ for which $i<j$ and

$$
\lvert \texttt{nums[i]}-\texttt{nums[j]} \rvert=k.
$$

Each pair is distinguished by its indices, so equal values at different
positions can participate in separate pairs. Absolute value ignores the sign
of a difference: $\lvert x\rvert=x$ when $x\ge0$, and
$\lvert x\rvert=-x$ when $x<0$. Consequently, either endpoint may contain the
larger value; only their distance and index order determine whether the pair
qualifies.

### Function Contract

**Inputs**

- `nums`: a list of $N$ integers, where $1\le N\le200$ and
  $1\le\texttt{nums[i]}\le100$.
- `k`: the required absolute difference, where $1\le k\le99$.

**Return value**

Return the number of index pairs satisfying the stated order and absolute
difference.

### Examples

**Example 1**

- Input: `nums = [1, 2, 2, 1], k = 1`
- Output: `4`
- Explanation: Each of the two positions containing `1` pairs with each of the
  two positions containing `2`.

**Example 2**

- Input: `nums = [1, 3], k = 3`
- Output: `0`
- Explanation: The only absolute difference is $2$, not $3$.

**Example 3**

- Input: `nums = [3, 2, 1, 5, 4], k = 2`
- Output: `3`
- Explanation: The value pairs are `3` with `1`, `3` with `5`, and `2` with
  `4`.
