### 1. Description

You are given `n` `points` in the plane that are all **distinct**, where $\text{points}[i] = [x_{i}, y_{i}]$. A **boomerang** is a tuple of points `(i, j, k)` such that the distance between `i` and `j` equals the distance between `i` and `k` **(the order of the tuple matters)**.

Return *the number of boomerangs*.

### 2. Function Contract

**Inputs**

- `points`: An array of distinct two-dimensional integer coordinates.

**Return value**

- Return the number of ordered boomerangs. The first point is the pivot, and the remaining two points are different equidistant endpoints.

### 3. Examples

#### Example 1

- **Input:** $points = [[0,0],[1,0],[2,0]]$
- **Output:** `2`
- **Explanation:** The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].
#### Example 2

- **Input:** $points = [[1,1],[2,2],[3,3]]$
- **Output:** `2`
#### Example 3

- **Input:** $points = [[1,1]]$
- **Output:** `0`

### 4. Constraints

- $n = \text{points.length}$

- $1 \le n \le 500$

- $\text{points}[i].length = 2$

- $-10^{4} \le x_{i}, y_{i} \le 10^{4}$

- All the points are **unique**.