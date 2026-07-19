# Make the XOR of All Segments Equal to Zero

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/) |
| Frontend ID | 1787 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Dynamic Programming, Bit Manipulation, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given an integer array `nums` and an integer `k`. The XOR of a segment `[left, right]` is the bitwise XOR of every array value from `nums[left]` through `nums[right]`, inclusive.

Change as few array elements as possible so that every contiguous segment of length `k` has XOR equal to zero. A changed element may be replaced by any legal ten-bit value. Return the minimum number of changed positions.

### Function Contract

**Inputs**

- `nums`: an array of length $n$, where $1 \le n \le 2000$ and $0 \le \texttt{nums[i]} < 2^{10}$.
- `k`: the required segment length, where $1 \le k \le n$.

Let $X=2^{10}=1024$, the complete domain of possible values and XOR states.

**Return value**

- Return the minimum number of positions that must be changed so every length-`k` contiguous segment has XOR zero.

### Examples

**Example 1**

- Input: `nums = [1,2,0,3,0], k = 1`
- Output: `3`

Every length-one segment must contain zero, so the three nonzero values change.

**Example 2**

- Input: `nums = [3,4,5,2,1,7,3,4,7], k = 3`
- Output: `3`

The array can be made periodic with chosen group values `3`, `4`, and `7`, whose XOR is zero.

**Example 3**

- Input: `nums = [1,2,4,1,2,5,1,2,6], k = 3`
- Output: `3`

Changing the third residue class to repeated value `3` makes every length-three segment XOR to zero.
