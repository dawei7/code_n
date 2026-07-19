# Reach a Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 754 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reach-a-number/) |

## Problem Description

### Goal

You start at position `0` on an infinite number line and want to reach integer `target`. On the `i`th move, beginning with $i = 1$, choose either direction and travel exactly `i` positions left or right.

Return the minimum number of moves required to land exactly on `target`. The direction may change independently on every move, but the move distance is fixed by its one-based move number; passing the target during an earlier move is allowed.

### Function Contract

**Inputs**

- `target`: an integer position, possibly negative or zero.

**Return value**

- The minimum count of successively longer signed moves whose sum equals `target`.

### Examples

**Example 1**

- Input: `target = 2`
- Output: `3`
- Explanation: Moves `+1`, `-2`, and `+3` finish at `2`.

**Example 2**

- Input: `target = 3`
- Output: `2`
- Explanation: Moving `+1` and then `+2` reaches `3` directly.
