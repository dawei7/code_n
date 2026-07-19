# Maximum Number of People That Can Be Caught in Tag

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1989 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-people-that-can-be-caught-in-tag/) |

## Problem Description
### Goal
People stand at the indexed positions of the binary array `team`. A value of
`1` marks a person who is “it,” while `0` marks someone who may be caught. A
person who is “it” at index `i` may catch one person at an index from
`i - dist` through `i + dist`, including both endpoints.

Each catcher may catch at most one other person, and each non-catcher may be
caught at most once. Choose the pairings to maximize the total number of caught
people, and return that maximum.

### Function Contract
**Inputs**

- `team`: a binary list of length $N$, where $1 \le N \le 10^5$; `1` denotes
  a catcher and `0` denotes a person who can be caught.
- `dist`: the inclusive maximum index distance $D$, where $1 \le D \le N$.

**Return value**

- The maximum number of disjoint catcher–person pairs whose index difference is
  at most $D$.

### Examples
**Example 1**

- Input: `team = [0, 1, 0, 1, 0], dist = 3`
- Output: `2`

The two catchers can be paired with any two of the three other people.

**Example 2**

- Input: `team = [1], dist = 1`
- Output: `0`

**Example 3**

- Input: `team = [0], dist = 1`
- Output: `0`
