# Find Three Consecutive Integers That Sum to a Given Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2177 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/) |

## Problem Description

### Goal

Given a nonnegative integer `num`, find three consecutive integers whose sum
equals `num`. Return those integers in increasing order.

The integers may include negative values even though `num` is nonnegative. If
no three consecutive integers have the required sum, return an empty array.
The result, when it exists, is unique because the middle integer determines
both neighbors. The returned order must be ascending rather than an arbitrary
permutation of the same three values.

### Function Contract

**Inputs**

- `num`: an integer satisfying $0\le\texttt{num}\le10^{15}$.

**Return value**

Return `[x - 1, x, x + 1]` when these three consecutive integers sum to `num`;
otherwise return `[]`.

### Examples

#### Example 1

- **Input:** `num = 33`
- **Output:** `[10,11,12]`

#### Example 2

- **Input:** `num = 4`
- **Output:** `[]`

#### Example 3

- **Input:** `num = 0`
- **Output:** `[-1,0,1]`
