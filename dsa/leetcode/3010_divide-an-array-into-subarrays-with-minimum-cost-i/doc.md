# Divide an Array Into Subarrays With Minimum Cost I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3010 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sorting, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/) |

## Problem Description

### Goal

You are given an integer array `nums`. Divide the entire array, without
reordering, into exactly three nonempty, disjoint, contiguous subarrays.

The cost of a subarray is its first element. Return the minimum possible sum of
the three subarray costs.

The first subarray necessarily starts at index 0. Thus a division is determined
by choosing two later starting indices in increasing order; every element must
belong to exactly one of the resulting three segments.

### Function Contract

**Inputs**

- `nums`: the array to partition into three nonempty contiguous pieces

Let $N=\lvert\texttt{nums}\rvert$. The contract guarantees $3\le N\le50$
and $1\le\texttt{nums[i]}\le50$.

**Return value**

Return the minimum sum of the first elements of the three chosen subarrays.

### Examples

#### Example 1

- **Input:** `nums = [1,2,3,12]`
- **Output:** `6`

The partition `[1]`, `[2]`, and `[3,12]` has costs 1, 2, and 3.

#### Example 2

- **Input:** `nums = [5,4,3]`
- **Output:** `12`

Each of the three elements must form its own subarray.

#### Example 3

- **Input:** `nums = [10,3,1,1]`
- **Output:** `12`

Starting the second and third subarrays at the two values 1 gives the minimum.
