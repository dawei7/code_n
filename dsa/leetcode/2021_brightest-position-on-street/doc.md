# Brightest Position on Street

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2021 |
| Difficulty | Medium |
| Topics | Array, Sorting, Prefix Sum, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/brightest-position-on-street/) |

## Problem Description

### Goal

A straight street is modeled as a number line containing several lamps. Each
entry `lights[i] = [position_i, range_i]` describes a lamp centered at
`position_i`. Its light covers every position in the inclusive interval from
`position_i - range_i` through `position_i + range_i`.

The brightness at a position is the number of lamp intervals containing that
position. Return a position with maximum brightness. If the maximum occurs at
several positions, return the smallest such position.

### Function Contract

Let $N$ be the number of lamps.

**Inputs**

- `lights`: a list of $N$ pairs `[position_i, range_i]`, where
  $1 \le N \le 10^5$, $-10^8 \le \text{position}_i \le 10^8$, and
  $0 \le \text{range}_i \le 10^8$.

**Return value**

- The smallest integer position attaining the greatest brightness.

### Examples

**Example 1**

- Input: `lights = [[-3, 2], [1, 2], [3, 3]]`
- Output: `-1`
- Explanation: Brightness is two at `-1` and throughout `0` through `3`;
  `-1` is the smallest maximizer.

**Example 2**

- Input: `lights = [[1, 0], [0, 1]]`
- Output: `1`
- Explanation: Both lamps cover position `1`, giving it brightness two.

**Example 3**

- Input: `lights = [[1, 2]]`
- Output: `-1`
- Explanation: Every position from `-1` through `3` has brightness one, so
  the smallest one is returned.
