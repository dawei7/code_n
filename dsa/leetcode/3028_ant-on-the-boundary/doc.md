# Ant on the Boundary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3028 |
| Difficulty | Easy |
| Topics | Array, Simulation, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/ant-on-the-boundary/) |

## Problem Description

### Goal

An ant starts at a boundary separating an infinite line into left and right sides. You are given a list `nums` of nonzero movements, read from beginning to end. A negative value moves the ant left by its absolute value, while a positive value moves it right by that value.

After each complete movement, check whether the ant is back at the boundary and count that visit. Crossing the boundary during a movement does not count unless the movement finishes exactly there. The initial position before any movement is not a return. Report the total number of completed steps whose resulting position is the boundary.

### Function Contract

**Inputs**

- `nums`: A list of $N$ nonzero integers, where $1\le N\le100$ and $-10\le\texttt{nums[i]}\le10$.

**Return value**

The number of prefixes of `nums` whose signed sum is zero.

### Examples

#### Example 1

- **Input:** `nums = [2, 3, -5]`
- **Output:** `1`

The ant's positions after the steps are `2`, `5`, and `0`, so it returns once.

#### Example 2

- **Input:** `nums = [3, 2, -3, -4]`
- **Output:** `0`

The completed positions are `3`, `5`, `2`, and `-2`; crossing zero on the last movement does not count.
