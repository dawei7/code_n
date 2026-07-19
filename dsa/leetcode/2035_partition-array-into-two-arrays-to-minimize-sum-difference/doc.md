# Partition Array Into Two Arrays to Minimize Sum Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2035 |
| Difficulty | Hard |
| Topics | Array, Two Pointers, Binary Search, Dynamic Programming, Bit Manipulation, Sorting, Ordered Set, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/) |

## Problem Description

### Goal

An integer array `nums` contains exactly $2n$ elements. Partition all of its
elements into two arrays, placing each original element in exactly one array
and requiring both resulting arrays to have length $n$.

Among every partition that satisfies this equal-cardinality rule, minimize the
absolute difference between the two array sums. Return that minimum difference.
Values may be positive, negative, or zero, so the optimal groups are determined
by their sums rather than by the individual magnitudes alone.

### Function Contract

Let $n$ be half the length of `nums`.

**Inputs**

- `nums`: an integer array of length $2n$, where $1 \le n \le 15$ and
  $-10^7 \le \texttt{nums[i]} \le 10^7$.

**Return value**

- The minimum possible absolute difference between the sums of two
  length-$n$ arrays formed by partitioning every input element.

### Examples

**Example 1**

- Input: `nums = [3, 9, 7, 3]`
- Output: `2`
- Explanation: Groups `[3, 9]` and `[7, 3]` have sums `12` and `10`.

**Example 2**

- Input: `nums = [-36, 36]`
- Output: `72`
- Explanation: Each of the two single-element groups must contain one value.

**Example 3**

- Input: `nums = [2, -1, 0, 4, -2, -9]`
- Output: `0`
- Explanation: `[2, 4, -9]` and `[-1, 0, -2]` both sum to `-3`.
