# Minimum Cost to Move Chips to The Same Position

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1217 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/) |

## Problem Description

### Goal

There are $n$ chips on a number line, and the $i$th chip is currently at `position[i]`. All chips must be moved to one common position.

In one step, a chip at `position[i]` may move to `position[i] + 2` or `position[i] - 2` at cost `0`. It may instead move to `position[i] + 1` or `position[i] - 1` at cost `1`. Any number of steps may be applied to each chip.

Return the minimum total cost needed to move all chips to the same position.

### Function Contract

**Inputs**

- `position`: A list containing the positions of $n$ chips, where $1\le n\le100$ and $1\le\texttt{position[i]}\le10^9$.

**Return value**

- The minimum total movement cost required to gather every chip at one position.

### Examples

**Example 1**

- Input: `position = [1,2,3]`
- Output: `1`

The chip at `3` can move to `1` by two units for free. Moving the chip at `2` to `1` costs `1`.

**Example 2**

- Input: `position = [2,2,2,3,3]`
- Output: `2`

Move both chips at `3` to `2`; each one-unit move costs `1`.

**Example 3**

- Input: `position = [1,1000000000]`
- Output: `1`
