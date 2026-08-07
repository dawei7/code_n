### Instruction

**Static Connectivity**

If the entire graph is provided upfront in the problem (for example, this problem directly provides the grid through a 2D array `grid`), and we are then asked queries about connectivity (such as whether there exists a path from the start to the end), this is referred to as **static connectivity**.

The opposite concept is **dynamic connectivity**, where graph updates and connectivity queries are interleaved. In other words, after a connectivity query, the graph may still be modified. For example, if this problem included multiple queries where each query modifies a position in `grid` and then checks whether a valid path exists, with modifications persisting across queries, then it would be considered a dynamic connectivity problem.

**About This Question**

For static connectivity problems, depth-first search, breadth-first search, and union-find can generally be used. These methods are conceptually similar, and the main challenge lies in constructing the graph, specifically determining which pairs of nodes should be connected.

Once the graph is constructed, we can easily determine whether two nodes are connected using any of these approaches.

In this solution, we focus on the **Union-Find** method. We treat each cell as a node in the graph, and define edges based on **direct reachability** between adjacent cells. Here, "direct reachability" means that a cell can move directly to one of its neighboring cells (up, down, left, or right).

For example, a cell with value $1$ represents a street connecting the left and right cells, while a cell with value $3$ connects the left and bottom cells. Therefore, if a cell with value $1$ is to the left of a cell with value $3$, these two cells are directly reachable. We can use Union-Find to maintain these relationships.

However, Union-Find operates on one-dimensional indices, while our grid is two-dimensional. Therefore, we map each cell $(x, y)$ to a unique integer ID using the formula:
$$
\text{id} = x \times n + y
$$
where $n$ is the number of columns. This mapping ensures that each cell corresponds to a unique node in the Union-Find structure.

After this transformation, the core challenge becomes: how do we efficiently determine whether two adjacent cells are directly reachable? The complexity and clarity of this check significantly affect the overall solution. We will introduce two different approaches below.

### Approach 1: Constructing a Graph Based on Adjacent Relationships

#### Intuition

A straightforward method is as follows: for each cell $(x, y)$ in the grid, its value determines at most two directions in which it connects to neighboring cells.

We define four helper functions: `detectL(x, y)`, `detectR(x, y)`, `detectU(x, y)`, and `detectD(x, y)`, corresponding to checking connections in the left, right, up, and down directions, respectively. For example, if `grid[x][y] = 1`, the cell connects left and right, so we call `detectL(x, y)` and `detectR(x, y)`.

What do these functions do? Consider `grid[x][y] = 1`. When calling `detectL(x, y)`, we examine the left neighbor $(x, y - 1)$. This neighbor must have a connection to the right to form a valid path. Therefore, `grid[x][y - 1]` must be one of `[1, 4, 6]`. In `detectL(x, y)`, we first check whether the neighbor exists, and then verify whether its value satisfies this condition. The other functions follow the same logic.

We traverse the entire grid, and for each cell, call the appropriate two functions based on its value. Whenever a valid connection exists, we merge the two corresponding nodes in the Union-Find structure.

After processing all cells, we simply check whether the top-left cell and the bottom-right cell belong to the same connected component.

#### Implementation


```python
class Solution:
    class DisjointSet:
        def __init__(self, n):
            self.f = list(range(n))

        def find(self, x):
            if x == self.f[x]:
                return x
            self.f[x] = self.find(self.f[x])
            return self.f[x]

        def merge(self, x, y):
            self.f[self.find(x)] = self.find(y)

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        ds = Solution.DisjointSet(m * n)

        def getId(x, y):
            return x * n + y

        def detectL(x, y):
            if y - 1 >= 0 and grid[x][y - 1] in [1, 4, 6]:
                ds.merge(getId(x, y), getId(x, y - 1))

        def detectR(x, y):
            if y + 1 < n and grid[x][y + 1] in [1, 3, 5]:
                ds.merge(getId(x, y), getId(x, y + 1))

        def detectU(x, y):
            if x - 1 >= 0 and grid[x - 1][y] in [2, 3, 4]:
                ds.merge(getId(x, y), getId(x - 1, y))

        def detectD(x, y):
            if x + 1 < m and grid[x + 1][y] in [2, 5, 6]:
                ds.merge(getId(x, y), getId(x + 1, y))

        def handler(x, y):
            if grid[x][y] == 1:
                detectL(x, y)
                detectR(x, y)
            elif grid[x][y] == 2:
                detectU(x, y)
                detectD(x, y)
            elif grid[x][y] == 3:
                detectL(x, y)
                detectD(x, y)
            elif grid[x][y] == 4:
                detectR(x, y)
                detectD(x, y)
            elif grid[x][y] == 5:
                detectL(x, y)
                detectU(x, y)
            else:
                detectR(x, y)
                detectU(x, y)

        for i in range(m):
            for j in range(n):
                handler(i, j)

        return ds.find(getId(0, 0)) == ds.find(getId(m - 1, n - 1))
```


#### Complexity Analysis

Let the total number of cells be $t = m \times n$.

* Time complexity: $O(t \times \alpha(t))$
  The Union-Find structure uses path compression but not union by rank. In the worst case, each operation takes $O(\log t)$ time, while the amortized time complexity is $O(\alpha(t))$, where $\alpha$ is the inverse Ackermann function, which grows extremely slowly. Since each cell performs at most a constant number of union operations, the total time complexity is $O(t \times \alpha(t))$.

* Space complexity: $O(t)$
  The Union-Find array `f` stores $t$ elements, so the space complexity is $O(t)$.

---

### Approach 2: Constructing a Graph Based on Cell Property

#### Intuition

We label the four directions as follows:

    ```
         0
         ^
         |
    3 <-- --> 1
         |
         v
         2
    ```

Each cell can be represented using a 4-bit binary number, where the $i$-th bit is set to 1 if there is a street in the $i$-th direction. Since each cell connects exactly two directions, each binary representation contains exactly two set bits.

This representation leads to an important observation:

* If a cell has a connection in direction $i$, then the adjacent cell in that direction must have a connection in direction $(i + 2) \bmod 4$.

Using this rule, we traverse the grid. For each cell $(x, y)$, we check all four directions. If the current cell has a connection in direction $i$, and the adjacent cell exists and has a corresponding connection in direction $(i + 2) \bmod 4$, we merge the two cells in the Union-Find structure.

After processing all cells, we check whether the top-left and bottom-right cells belong to the same connected component.

#### Implementation


```python
class Solution:
    class DisjointSet:
        def __init__(self, n):
            self.f = list(range(n))

        def find(self, x):
            if x == self.f[x]:
                return x
            self.f[x] = self.find(self.f[x])
            return self.f[x]

        def merge(self, x, y):
            self.f[self.find(x)] = self.find(y)

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        patterns = [0, 0b1010, 0b0101, 0b1100, 0b0110, 0b1001, 0b0011]
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        ds = Solution.DisjointSet(m * n)

        def getId(x, y):
            return x * n + y

        def handler(x, y):
            pattern = patterns[grid[x][y]]
            for i, (dx, dy) in enumerate(dirs):
                if (pattern & (1 << i)) > 0:
                    sx, sy = x + dx, y + dy
                    if (
                        0 <= sx < m
                        and 0 <= sy < n
                        and (patterns[grid[sx][sy]] & (1 << ((i + 2) % 4))) > 0
                    ):
                        ds.merge(getId(x, y), getId(sx, sy))

        for i in range(m):
            for j in range(n):
                handler(i, j)

        return ds.find(getId(0, 0)) == ds.find(getId(m - 1, n - 1))
```


#### Complexity Analysis

Let the total number of cells be $t = m \times n$.

- Time complexity: $O(t \times \alpha(t))$.

- Space complexity: $O(t)$.

    Approach 2 differs from Approach 1 only in how connectivity between adjacent cells is determined. Since this check takes constant time $O(1)$ in both approaches, their overall time and space complexities remain the same.

---