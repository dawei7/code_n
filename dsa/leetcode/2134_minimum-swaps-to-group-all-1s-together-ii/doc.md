# Minimum Swaps to Group All 1's Together II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2134 |
| Difficulty | Medium |
| Topics | Array, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/) |

## Problem Description
### Goal
A swap exchanges the values at two distinct array positions. You are given a
binary circular array, so its first and last elements are considered adjacent.

Using swaps between any positions, group every `1` into one contiguous
circular block at any location. Return the minimum number of swaps needed.
The chosen block may cross the boundary between the end and beginning of the
stored array.

### Function Contract
**Inputs**

- `nums`: A binary array of length $n$, where $1\le n\le 10^5$.

**Return value**

The minimum number of swaps required to place all ones in one circularly
contiguous block.

### Examples
**Example 1**

- Input: `nums = [0,1,0,1,1,0,0]`
- Output: `1`

**Example 2**

- Input: `nums = [0,1,1,1,0,0,1,1,0]`
- Output: `2`

**Example 3**

- Input: `nums = [1,1,0,0,1]`
- Output: `0`
- Explanation: The ones already form one block across the circular boundary.
