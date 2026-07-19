# Falling Squares

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 699 |
| Difficulty | Hard |
| Topics | Array, Segment Tree, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/falling-squares/) |

## Problem Description
### Goal
Squares are dropped one at a time onto the x-axis of a two-dimensional plane. Each `positions[i] = [left_i, sideLength_i]` gives a square's left x-coordinate and side length; it falls vertically until its bottom reaches the x-axis or the top of a previously landed square beneath an overlapping horizontal interval.

Once landed, a square remains fixed. After every drop, record the current greatest height of any stack and return all recorded heights in order. Squares that only touch along a left or right edge do not horizontally overlap and do not support one another.

### Function Contract
**Inputs**

- `positions`: a list of `[left, side_length]` pairs describing each square

**Return value**

- A list whose entry after each drop is the maximum height anywhere among all squares placed so far

### Examples
**Example 1**

- Input: `positions = [[1,2],[2,3],[6,1]]`
- Output: `[2,5,5]`

**Example 2**

- Input: `positions = [[100,100],[200,100]]`
- Output: `[100,100]`
- Explanation: the intervals meet at one edge but do not overlap.

**Example 3**

- Input: `positions = [[1,5],[2,2],[3,1]]`
- Output: `[5,7,8]`
