### 1. Description

You are given a 2D matrix `grid` of size `m x n`. In one **operation**, you can change the value of **any** cell to **any** non-negative number. You need to perform some **operations** such that each cell $\text{grid}[i][j]$ is:

- Equal to the cell below it, i.e. $\text{grid}[i][j] = grid[i + 1][j]$ (if it exists).

- Different from the cell to its right, i.e. $\text{grid}[i][j] \neq \text{grid}[i][j + 1]$ (if it exists).

Return the **minimum** number of operations needed.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** grid = [[1,0,2],[1,0,2]]

**Output:** 0

**Explanation:**

**

![](images/examplechanged.png)

**

All the cells in the matrix already satisfy the properties.

</div>
#### Example 2

<div class="example-block">
**Input:** grid = [[1,1,1],[0,0,0]]

**Output:** 3

**Explanation:**

**

![](images/example21.png)

**

The matrix becomes `[[1,0,1],[1,0,1]]` which satisfies the properties, by doing these 3 operations:

- Change $\text{grid}[1][0]$ to 1.

- Change $\text{grid}[0][1]$ to 0.

- Change $\text{grid}[1][2]$ to 1.

</div>
#### Example 3

<div class="example-block">
**Input:** grid = [[1],[2],[3]]

**Output:** 2

**Explanation:**

![](images/changed.png)

There is a single column. We can change the value to 1 in each cell using 2 operations.

</div>

### 4. Constraints

- $1 \le n, m \le 1000$

- $0 \le \text{grid}[i][j] \le 9$