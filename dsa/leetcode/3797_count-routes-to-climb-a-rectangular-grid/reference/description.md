### 1. Description

You are given a string array `grid` of size `n`, where each string $\text{grid}[i]$ has length `m`. The character $\text{grid}[i][j]$ is one of the following symbols:

- `'.'`: The cell is available.

- `'#'`: The cell is blocked.

You want to count the number of different routes to climb `grid`. Each route must start from *any cell* in the bottom row (row $n - 1$) and end in the top row (row 0).

However, there are some constraints on the route.

- You can only move from one available cell to **another** available cell.

- The **Euclidean distance** of each move is **at most** `d`, where `d` is an integer parameter given to you. The Euclidean distance between two cells `(r1, c1)`, `(r2, c2)` is $sqrt((r1 - r2)^2 + (c1 - c2)^2)$.

- Each move either stays on the same row or moves to the row directly above (from row `r` to $r - 1$).

- You cannot stay on the same row for two consecutive turns. If you stay on the same row in a move (and this move is not the last move), your next move must go to the row above.

Return an integer denoting the number of such routes. Since the answer may be very large, return it **modulo** $10^{9} + 7$.

### 2. Function Contract

**Inputs**

- `grid`: A nonempty rectangular array of equal-length strings containing only `'.'` and `'#'`.
- `d`: The inclusive Euclidean-distance limit for every move.

The bottom and top rows coincide when `grid` has one row. In that case, selecting one available starting cell already forms a route; one legal same-row move may also be the final move. A move must change cells, so remaining at the same coordinate is not an additional route step.

**Return value**

Return the number of cell sequences satisfying the start, finish, availability, distance, row-direction, and consecutive-same-row rules, reduced modulo $1{,}000{,}000{,}007$.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** grid = ["..","#."], d = 1

**Output:** 2

**Explanation:**

We label the cells we visit in the routes sequentially, starting from 1. The two routes are:

```
.2
#1
```

```
32
#1
```

We can move from the cell (1, 1) to the cell (0, 1) because the Euclidean distance is $sqrt((1 - 0)^2 + (1 - 1)^2) = sqrt(1) \le d$.

However, we cannot move from the cell (1, 1) to the cell (0, 0) because the Euclidean distance is $sqrt((1 - 0)^2 + (1 - 0)^2) = sqrt(2) > d$.

</div>
#### Example 2

<div class="example-block">
**Input:** grid = ["..","#."], d = 2

**Output:** 4

**Explanation:**

Two of the routes are given in example 1. The other two routes are:

```
2.
#1
```

```
23
#1
```

Note that we can move from (1, 1) to (0, 0) because the Euclidean distance is $sqrt(2) \le d$.

</div>
#### Example 3

<div class="example-block">
**Input:** grid = ["#"], d = 750

**Output:** 0

**Explanation:**

We cannot choose any cell as the starting cell. Therefore, there are no routes.

</div>
#### Example 4

<div class="example-block">
**Input:** grid = [".."], d = 1

**Output:** 4

**Explanation:**

The possible routes are:

```
.1
```

```
1.
```

```
12
```

```
21
```

</div>

### 4. Constraints

- $1 \le n = \text{grid.length} \le 750$

- $1 \le m = \text{grid}[i].length \le 750$

- $\text{grid}[i][j]$ is `'.'` or `'#'`.

- $1 \le d \le 750$