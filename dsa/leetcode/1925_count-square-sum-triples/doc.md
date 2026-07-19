# Count Square Sum Triples

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/count-square-sum-triples/) |
| Frontend ID | 1925 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A square triple is an ordered triple of integers `(a, b, c)` satisfying

$$
a^2+b^2=c^2.
$$

Given an upper bound `n`, count all square triples for which each of `a`, `b`, and `c` lies between $1$ and $n$, inclusive. The order of the first two values matters: when $a \ne b$, `(a, b, c)` and `(b, a, c)` are distinct triples and both contribute.

### Function Contract

**Inputs**

- `n`: the inclusive upper bound for every component, with $1 \le n \le 250$.

**Return value**

- Return the number of ordered triples `(a, b, c)` in $[1,n]^3$ satisfying $a^2+b^2=c^2$.

### Examples

**Example 1**

- Input: `n = 5`
- Output: `2`

The triples are `(3,4,5)` and `(4,3,5)`.

**Example 2**

- Input: `n = 10`
- Output: `4`

The two orientations of `(3,4,5)` and `(6,8,10)` qualify.
