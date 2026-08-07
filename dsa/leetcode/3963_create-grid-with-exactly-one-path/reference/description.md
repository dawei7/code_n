## Description

You are given two integers `m` and `n`, representing the number of rows and columns of a grid.

Construct **any** `m x n` grid consisting only of the characters `'.'` and `'#'`, where:

- `'.'` represents a free cell.

- `'#'` represents an obstacle cell.

A **valid path** is a sequence of free cells that:

- Starts at the top-left cell `(0, 0)`.

- Ends at the bottom-right cell $(m - 1, n - 1)$.

- Moves only:

		<li>Right, from `(i, j)` to $(i, j + 1)$, or

- Down, from `(i, j)` to $(i + 1, j)$.

	</li>

Return any grid such that there is **exactly one valid path** from the top-left cell to the bottom-right cell.
### Function Contract

**Inputs**

- `m`: The positive number of grid rows.
- `n`: The positive number of grid columns.

**Return value**

Return a list of `m` strings, each of length `n`, containing only `.` and `#`. The free cells must admit exactly one right-or-down path from `(0, 0)` to `(m - 1, n - 1)`.

### Examples
#### Example 1

<div class="example-block">
**Input:** m = 2, n = 3

**Output:** ["..#","#.."]

**Explanation:**

![](images/screenshot-2026-05-26-at-61005pm.png)

The only valid path is: `(0,0) → (0,1) → (1,1) → (1,2)`

</div>
#### Example 2

<div class="example-block">
**Input:** m = 3, n = 3

**Output:** ["..#","#..","##."]

**Explanation:**

![](images/screenshot-2026-05-26-at-61129pm.png)

The only valid path is: `(0,0) → (0,1) → (1,1) → (1,2) → (2,2)`

</div>
#### Example 3

<div class="example-block">
**Input:** m = 1, n = 4

**Output:** ["...."]

**Explanation:**

The only valid path is: `(0,0) → (0,1) → (0,2) → (0,3)`

</div>
### Constraints

- $1 \le m, n \le 25$