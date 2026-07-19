# Find the Winner of the Circular Game

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/find-the-winner-of-the-circular-game/) |
| Frontend ID | 1823 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Recursion, Queue, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

There are `n` friends numbered from 1 through `n` clockwise around a circle. Moving clockwise after friend `n` returns to friend 1. The game begins at friend 1.

Count `k` friends clockwise, including the friend where the count starts; wrapping may visit friends more than once when `k` exceeds the current circle size. The `k`th counted friend leaves. If multiple friends remain, resume counting at the friend immediately clockwise of the one removed. Repeat until one friend remains, and return that winner's label.

### Function Contract

**Inputs**

- `n`: the number of friends, with $1 \le n \le 500$.
- `k`: the number counted in every round, with $1 \le k \le n$.

**Return value**

- Return the surviving friend's 1-based label.

### Examples

**Example 1**

- Input: `n = 5, k = 2`
- Output: `3`

Friends leave in the order 2, 4, 1, and 5, leaving friend 3.

**Example 2**

- Input: `n = 6, k = 5`
- Output: `1`

The elimination order is 5, 4, 6, 2, and 3.
