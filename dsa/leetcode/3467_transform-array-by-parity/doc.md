# Transform Array by Parity

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3467 |
| Difficulty | Easy |
| Topics | Array, Sorting, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/transform-array-by-parity/) |

## Problem Description

### Goal

Given an integer array `nums`, transform every element according to its parity. The operations must be applied in the exact specified order: replace each even value with `0`, replace each odd value with `1`, and then sort the modified array in non-decreasing order. The original magnitudes and positions do not otherwise affect the transformation.

Return the resulting array after all three operations. It has the same length as `nums` and contains only zeroes and ones; its ordering must reflect the final non-decreasing sort, rather than the order in which the original even and odd values appeared.

### Function Contract

**Inputs**

- `nums`: The integer array to transform.

Let $n=\lvert\texttt{nums}\rvert$. The constraints are $1\le n\le100$ and $1\le\texttt{nums[i]}\le1000$.

**Return value**

Return the parity-transformed array sorted in non-decreasing order.

### Examples

#### Example 1

- **Input:** `nums = [4,3,2,1]`
- **Output:** `[0,0,1,1]`

The even values become zeroes and the odd values become ones; sorting places the two zeroes first.

#### Example 2

- **Input:** `nums = [1,5,1,4,2]`
- **Output:** `[0,0,1,1,1]`

Two values are even and three are odd, so the transformed array contains two zeroes followed by three ones.
