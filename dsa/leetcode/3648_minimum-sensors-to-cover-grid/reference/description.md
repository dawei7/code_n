### 1. Description

You are given `n × m` grid and an integer `k`.

A sensor placed on cell `(r, c)` covers all cells whose **Chebyshev distance** from `(r, c)` is **at most** `k`.

The **Chebyshev distance** between two cells $(r_{1}, c_{1})$ and $(r_{2}, c_{2})$ is $max(|r_{1} − r_{2}|,|c_{1} − c_{2}|)$.

Your task is to return the **minimum** number of sensors required to cover every cell of the grid.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** n = 5, m = 5, k = 1

**Output:** 4

**Explanation:**

Placing sensors at positions `(0, 3)`, `(1, 0)`, `(3, 3)`, and `(4, 1)` ensures every cell in the grid is covered. Thus, the answer is 4.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 2, m = 2, k = 2

**Output:** 1

**Explanation:**

With $k = 2$, a single sensor can cover the entire $2 * 2$ grid regardless of its position. Thus, the answer is 1.

</div>

### 4. Constraints

- $1 \le n \le 10^{3}$

- $1 \le m \le 10^{3}$

- $0 \le k \le 10^{3}$