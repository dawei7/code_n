# Decompress Run-Length Encoded List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1313 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/decompress-run-length-encoded-list/) |

## Problem Description
### Goal
An even-length integer array `nums` stores a run-length encoding as adjacent pairs. For pair index $i$, `nums[2 * i]` is a frequency and `nums[2 * i + 1]` is the associated value.

Expand each pair into a sublist containing exactly `freq` copies of `val`. Concatenate those sublists from left to right, preserving the order of the encoded pairs, and return the complete decompressed list.

### Function Contract
**Inputs**

- `nums`: an even-length integer array with $2\le\lvert\texttt{nums}\rvert\le100$.
- Every element of `nums`, including each frequency and value, is between 1 and 100 inclusive.
- The encoded pairs are `[nums[0], nums[1]]`, `[nums[2], nums[3]]`, and so on.

Let

$$
S=\sum_i \texttt{nums[2 * i]}
$$

be the decompressed output length, and let $n=\lvert\texttt{nums}\rvert$.

**Return value**

An array of length $S$ formed by concatenating `nums[2 * i]` copies of `nums[2 * i + 1]` for every pair in order.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4]`
- Output: `[2,4,4,4]`

**Example 2**

- Input: `nums = [1,1,2,3]`
- Output: `[1,3,3]`

**Example 3**

- Input: `nums = [2,5,1,9]`
- Output: `[5,5,9]`
