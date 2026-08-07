### Preface

For a grid $\textit{grid}$ of size $m \times n$, we can treat each position as a node and connect an undirected edge between any two adjacent nodes (up, down, left, right) that have the same value. In this way, a cycle in $\textit{grid}$ corresponds to a cycle in the constructed graph. Therefore, the problem reduces to checking whether a cycle exists in this graph.

Common approaches for detecting cycles in an undirected graph include depth-first search (DFS) and breadth-first search (BFS). However, here we introduce an approach based on the Union-Find data structure.

### Approach: Union-Find Set

#### Intuition

Using a Union-Find data structure to detect cycles in an undirected graph is both concise and intuitive:

- For any edge $(x, y)$ in the graph, we attempt to merge the sets containing $x$ and $y$. If $x$ and $y$ are already in the same set, it means they are already connected, and adding the edge $(x, y)$ will form a cycle.

We can apply this idea by traversing each position in the array $\textit{grid}$. If the current position has the same value as the position above or to the left, then there exists an edge, and we attempt to merge the corresponding nodes. This ensures that each edge is processed only once.

Since the Union-Find structure is one-dimensional while $\textit{grid}$ is two-dimensional, we map each position $(i, j)$ to a one-dimensional index using $i \times n + j$:

- The position above $(i, j)$ maps to $(i - 1) \times n + j$.
- The position to the left of $(i, j)$ maps to $i \times n + j - 1$.

#### Implementation

```python
class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.setCount = n
        self.parent = list(range(n))
        self.size = [1] * n

    def findset(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int):
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1

    def findAndUnite(self, x: int, y: int) -> bool:
        parentX, parentY = self.findset(x), self.findset(y)
        if parentX != parentY:
            self.unite(parentX, parentY)
            return True
        return False

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)
        for i in range(m):
            for j in range(n):
                if i > 0 and grid[i][j] == grid[i - 1][j]:
                    if not uf.findAndUnite(i * n + j, (i - 1) * n + j):
                        return True
                if j > 0 and grid[i][j] == grid[i][j - 1]:
                    if not uf.findAndUnite(i * n + j, i * n + j - 1):
                        return True
        return False
```

#### Complexity Analysis

- Time complexity: $O(mn \cdot \alpha(mn))$.

  The Union-Find structure uses path compression and union by size or rank, resulting in an amortized cost of $\alpha(mn)$ per operation. Each position participates in at most two union operations, leading to a total complexity of $O(mn \cdot \alpha(mn))$.

- Space complexity: $O(mn)$.

  This is the space required for the Union-Find data structure.

---