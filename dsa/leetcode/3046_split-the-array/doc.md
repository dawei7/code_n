# Split the Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3046 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/split-the-array/) |

## Problem Description

### Goal

You are given an integer array `nums` whose length is even. Split all of its elements into two arrays, `nums1` and `nums2`, subject to three requirements:

- `nums1.length == nums2.length == nums.length / 2`.
- Every value in `nums1` is distinct from every other value in `nums1`.
- Every value in `nums2` is distinct from every other value in `nums2`.

Return `true` if at least one such split exists, and `false` otherwise. The relative order of elements is irrelevant; only assigning every occurrence to one of the two equal-sized parts matters.

### Function Contract

Let $n=\lvert\texttt{nums}\rvert$.

**Inputs**

- `nums`: An integer array with even length $n$, where $1\le n\le100$ and every value lies between `1` and `100` inclusive.

**Return value**

Return `True` exactly when the elements can be distributed into two length-$n/2$ arrays that each contain only distinct values.

### Examples

#### Example 1

- **Input:** `nums = [1,1,2,2,3,4]`
- **Output:** `true`
- **Explanation:** One valid split is `nums1 = [1,2,3]` and `nums2 = [1,2,4]`.

#### Example 2

- **Input:** `nums = [1,1,1,1]`
- **Output:** `false`
- **Explanation:** Four copies of `1` cannot be placed into two arrays without repeating `1` inside at least one part.
