# Minimum Increment to Make Array Unique

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 945 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-increment-to-make-array-unique/) |

## Problem Description

### Goal

You are given an integer array `nums`. One move chooses an index `i` and performs `nums[i] += 1`; values may only be increased, never decreased or replaced by an arbitrary number.

Find the minimum total number of these single-step increments needed so that every value in the array is unique. The final values themselves do not need to be returned, and the test data guarantees that the minimum move count fits in a 32-bit integer.

### Function Contract

Let $n$ be the length of `nums`, and define

$$
M = \max(\texttt{nums}) + n + 1,
$$

the number of value positions sufficient to distribute all duplicates.

**Inputs**

- `nums`: a list of $n$ integers with $1 \le n \le 10^5$ and `0 <= nums[i] <= 100000`.

**Return value**

Return the minimum number of unit increments required to make all array values pairwise distinct.

### Examples

**Example 1**

- Input: `nums = [1, 2, 2]`
- Output: `1`

Incrementing one copy of `2` once produces distinct values such as `[1, 2, 3]`.

**Example 2**

- Input: `nums = [3, 2, 1, 2, 1, 7]`
- Output: `6`

One minimum-cost result is `[3, 4, 1, 2, 5, 7]`; no sequence of five moves can make every value unique.
