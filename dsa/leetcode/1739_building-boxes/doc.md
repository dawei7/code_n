# Building Boxes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1739 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Binary Search, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/building-boxes/) |

## Problem Description

### Goal

A cubic storeroom has equal width, length, and height, each measuring `n` units. Place exactly `n` unit-cube boxes inside it. Boxes may be put anywhere on the floor, but a box can support another box only when each of its four vertical sides is adjacent either to another box or to a wall.

Arrange the boxes while obeying that support rule and return the minimum possible number that touch the floor. The room is large enough for every valid input, and $1 \le n \le 10^9$.

### Function Contract

**Inputs**

- `n`: the positive number of unit-cube boxes to place.

**Return value**

- Return the smallest possible count of boxes whose bottom face touches the floor.

### Examples

**Example 1**

- Input: `n = 3`
- Output: `3`
- Explanation: None of the three boxes can yet be supported above another, so all three touch the floor.

**Example 2**

- Input: `n = 4`
- Output: `3`
- Explanation: Three boxes can form a supported corner base for the fourth box.

**Example 3**

- Input: `n = 10`
- Output: `6`
- Explanation: A complete three-level corner stack contains ten boxes and has six floor boxes.
