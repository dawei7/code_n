# Count Collisions of Monkeys on a Polygon

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2550 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [count-collisions-of-monkeys-on-a-polygon](https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/) |

## Problem Description

### Goal

A regular convex polygon has $n$ vertices labeled clockwise from 0 through $n-1$, with exactly one monkey initially at every vertex. All monkeys move simultaneously, and each independently chooses one of the two neighboring vertices.

A collision occurs if at least two monkeys finish at the same vertex or if monkeys traveling in opposite directions intersect along an edge. Count the movement choices that produce at least one collision, and return the count modulo $10^9+7$.

### Function Contract

**Inputs**

- `n`: The number of polygon vertices and monkeys.

The constraint is $3 \le n \le 10^9$.

**Return value**

Return the number of simultaneous direction assignments causing at least one collision, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `n = 3`
- Output: `6`
- Explanation: There are $2^3 = 8$ direction assignments, and only the two uniform directions avoid collisions.

**Example 2**

- Input: `n = 4`
- Output: `14`
- Explanation: Of the 16 assignments, all except the all-clockwise and all-counterclockwise choices collide.
