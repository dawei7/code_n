# Mirror Reflection

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 858 |
| Difficulty | Medium |
| Topics | Math, Geometry, Number Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/mirror-reflection/) |

## Problem Description
### Goal
A square room has mirrored walls of length `p`. Three receptors occupy every corner except the southwest corner: receptor `0` is southeast, receptor `1` is northeast, and receptor `2` is northwest. A laser ray starts at the southwest corner and initially travels toward the east wall.

The ray's first contact with the east wall is `q` units above receptor `0`. It reflects from each wall with equal incoming and outgoing angles. Given `p` and `q`, determine which numbered receptor the ray reaches first. The input guarantees that the ray eventually reaches a receptor.

### Function Contract
**Inputs**

- `p`: the positive side length of the square room.
- `q`: the height of the ray's first east-wall contact measured from receptor `0`, where $1 \leq q \leq p \leq 1000$.

Let $g = \gcd(p,q)$, $h = p/g$, and $v = q/g$. In the unfolded construction, $h$ is the number of room widths crossed before a corner is reached and $v$ is the corresponding number of room heights.

**Return value**

Return `0`, `1`, or `2`, identifying the first receptor reached by the ray.

### Examples
**Example 1**

- Input: `p = 2, q = 1`
- Output: `2`

The first receptor reached is on the left wall after one reflection.

**Example 2**

- Input: `p = 3, q = 1`
- Output: `1`

**Example 3**

- Input: `p = 3, q = 2`
- Output: `0`
