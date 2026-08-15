### 1. Description

You are given a 2D array `grid` of size `m x n`, and an integer `k`. There are `k` cells in `grid` containing the values from 1 to `k` **exactly once**, and the rest of the cells have a value 0.

You can start at any cell, and move from a cell to its neighbors (up, down, left, or right). You must find a path in `grid` which:

- Visits each cell in `grid` **exactly once**.

- Visits the cells with values from 1 to `k` **in order**.

Return a 2D array `result` of size $(m * n) x 2$, where $\text{result}[i] = [x_{i}, y_{i}]$ represents the $$i^{\text{th}}$$ cell visited in the path. If there are multiple such paths, you may return **any** one.

If no such path exists, return an **empty** array.

### 2. Function Contract

- Refer to method signature.

### 3. Examples

#### Example 1

- **Input:** grid = [[0,0,0],[0,1,2]], k = 2

- **Output:** [[0,0],[1,0],[1,1],[1,2],[0,2],[0,1]]

- **Explanation:** ![](images/ezgifcom-animated-gif-maker1.gif)

#### Example 2

- **Input:** grid = [[1,0,4],[3,0,2]], k = 4

- **Output:** []

- **Explanation:** There is no possible path that satisfies the conditions.

### 4. Constraints

- $1 \le m = \text{grid.length} \le 5$

- $1 \le n = \text{grid}[i].length \le 5$

- $1 \le k \le m * n$

- $0 \le \text{grid}[i][j] \le k$

- `grid` contains all integers between 1 and `k` **exactly** once.
