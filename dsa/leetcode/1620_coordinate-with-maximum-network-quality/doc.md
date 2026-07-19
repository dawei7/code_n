# Coordinate With Maximum Network Quality

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1620 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/coordinate-with-maximum-network-quality/) |

## Problem Description
### Goal
Each entry `[x_i, y_i, q_i]` describes a network tower at an integral coordinate with quality factor $q_i$. Distances on the plane are Euclidean. At an integral coordinate $(x,y)$, tower $i$ is reachable only when its distance $d_i$ is at most `radius`; a reachable tower contributes

$$
\left\lfloor \frac{q_i}{1+d_i} \right\rfloor
$$

to the network quality, while an unreachable tower contributes nothing. The total network quality is the sum of all reachable contributions.

Return the non-negative integral coordinate with maximum network quality. If several coordinates have the same maximum, choose the lexicographically smallest one: minimize the $x$-coordinate first, then the $y$-coordinate.

### Function Contract
**Inputs**

- `towers`: a nonempty list of $T$ entries `[x_i, y_i, q_i]`, where $1 \le T \le 50$ and $0 \le x_i,y_i,q_i \le 50$.
- `radius`: the inclusive reach distance, where $1 \le \texttt{radius} \le 50$.

**Return value**

Return `[c_x, c_y]`, the lexicographically smallest non-negative integral coordinate attaining the greatest total network quality.

### Examples
**Example 1**

- Input: `towers = [[1,2,5],[2,1,7],[3,1,9]], radius = 2`
- Output: `[2,1]`

**Example 2**

- Input: `towers = [[23,11,21]], radius = 9`
- Output: `[23,11]`

**Example 3**

- Input: `towers = [[1,2,13],[2,1,7],[0,1,9]], radius = 2`
- Output: `[1,2]`
