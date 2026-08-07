## Description

You are given a 2D array of integers `coordinates` of length `n` and an integer `k`, where $0 \le k < n$.

$\text{coordinates}[i] = [x_{i}, y_{i}]$ indicates the point $(x_{i}, y_{i})$ in a 2D plane.

An **increasing path** of length `m` is defined as a list of points $(x_{1}, y_{1})$, $(x_{2}, y_{2})$, $(x_{3}, y_{3})$, ..., $(x_{m}, y_{m})$ such that:

- $x_{i} < x_{i} + 1$ and $y_{i} < y_{i} + 1$ for all `i` where $1 \le i < m$.

- $(x_{i}, y_{i})$ is in the given coordinates for all `i` where $1 \le i \le m$.

Return the **maximum** length of an **increasing path** that contains $\text{coordinates}[k]$.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** coordinates = [[3,1],[2,2],[4,1],[0,0],[5,3]], k = 1

**Output:** 3

**Explanation:**

`(0, 0)`, `(2, 2)`, `(5, 3)`<!-- notionvc: 082cee9e-4ce5-4ede-a09d-57001a72141d --> is the longest increasing path that contains `(2, 2)`.

</div>
#### Example 2

<div class="example-block">
**Input:** coordinates = [[2,1],[7,0],[5,6]], k = 2

**Output:** 2

**Explanation:**

`(2, 1)`, `(5, 6)` is the longest increasing path that contains `(5, 6)`.

</div>
### Constraints

- $1 \le n = \text{coordinates.length} \le 10^{5}$

- $\text{coordinates}[i].length = 2$

- $0 \le \text{coordinates}[i][0], \text{coordinates}[i][1] \le 10^{9}$

- All elements in `coordinates` are **distinct**.<!-- notionvc: 6e412fc2-f9dd-4ba2-b796-5e802a2b305a --><!-- notionvc: c2cf5618-fe99-4909-9b4c-e6b068be22a6 -->

- $0 \le k \le n - 1$