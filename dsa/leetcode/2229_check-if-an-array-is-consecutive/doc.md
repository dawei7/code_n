# Check if an Array Is Consecutive

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2229 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-an-array-is-consecutive/) |

## Problem Description

### Goal

Determine whether the integer array `nums` is consecutive. If $x$ is its minimum value and $n$ is its length, being consecutive means that the array contains every integer in the inclusive range $[x,x+n-1]$.

The input order does not matter, but every required value must occur. Because the array itself has exactly $n$ positions and the target range has exactly $n$ distinct integers, a duplicated value necessarily leaves another value missing and makes the result false. Return a boolean expressing whether the complete range is present.

### Function Contract

**Inputs**

- `nums`: A nonempty list of integers, each between $0$ and $10^5$ inclusive.

Let $n=\lvert\texttt{nums}\rvert$, where $1\le n\le 10^5$.

**Return value**

Return `true` exactly when `nums` contains each integer from its minimum through that minimum plus $n-1`; otherwise return `false`.

### Examples

#### Example 1

- **Input:** `nums = [1, 3, 4, 2]`
- **Output:** `true`

#### Example 2

- **Input:** `nums = [1, 3]`
- **Output:** `false`

#### Example 3

- **Input:** `nums = [3, 5, 4]`
- **Output:** `true`
