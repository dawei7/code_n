## Description

Given the coordinates of four points in 2D space `p1`, `p2`, `p3` and `p4`, return `true` *if the four points construct a square*.

The coordinate of a point $p_{i}$ is represented as $[x_{i}, y_{i}]$. The input is **not** given in any order.

A **valid square** has four equal sides with positive length and four equal angles (90-degree angles).
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** $p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]$
- **Output:** `true`
#### Example 2

- **Input:** $p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]$
- **Output:** `false`
#### Example 3

- **Input:** $p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]$
- **Output:** `true`
### Constraints

- $\text{p1.length} = \text{p2.length} = \text{p3.length} = \text{p4.length} = 2$

- $-10^{4} \le x_{i}, y_{i} \le 10^{4}$