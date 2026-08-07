### Approach: Binary Answer + Minimum Spanning Tree

#### Prerequisites

This method assumes that the reader is already familiar with:

- The idea of binary search on the answer and its algorithmic framework.
- The definition of a minimum spanning tree and the Kruskal algorithm used to construct it, including its core idea and implementation.

#### Intuition

This problem essentially asks us to find the **maximum possible value of the minimum edge weight** in a spanning tree. Problems involving expressions such as "maximize the minimum" or "minimize the maximum" are often solved using a **binary search on the answer** framework. In this problem, we perform a binary search on the minimum edge weight and check whether it is possible to construct a spanning tree that satisfies this constraint.

Next, consider the following question: for a given minimum edge weight constraint, what strategy should we use to construct a spanning tree? A greedy strategy is the natural choice. If it is impossible to construct a spanning tree while selecting edges that satisfy the constraint as much as possible, then selecting less optimal edges will certainly not help satisfy the requirement. This reasoning follows directly from the greedy properties of spanning tree algorithms.

First, ignore the ability to double edge weights $k$ times. To make the selected edges satisfy the constraint as much as possible, we should greedily choose edges with **larger weights**. This is equivalent to constructing a **maximum spanning tree**. We use the $\text{Kruskal}$ algorithm as the basic framework for building this spanning tree.

Now consider the doubling strategy. Since we greedily choose edges with larger weights, the doubling opportunities are naturally used only when necessary. When we encounter an edge whose weight is less than the current constraint, we attempt to double its weight in order to satisfy the constraint and continue building the spanning tree. If the doubled weight is still less than the constraint, or if all doubling opportunities have already been used, then none of the remaining edges can satisfy the constraint, and this construction attempt fails.

During preprocessing, we first **force-select** the edges with $\textit{must} = 1$ to establish the initial state of the Union-Find structure. The minimum edge weight among these edges serves as the upper bound for the binary search. Meanwhile, to construct a maximum spanning tree, we sort the edges with $\textit{must} = 0$ in **descending order of weight**.

During the binary search process, we follow the steps of Kruskal's algorithm while applying the strategy described above. We continuously maintain the Union-Find structure to ensure correctness.

The problem states that the resulting spanning tree must satisfy three properties. Under the condition that the graph is **acyclic**, the properties of **connectivity** and **having exactly $n - 1$ edges** are equivalent. Since the Union-Find structure already guarantees that no cycles are formed, we simply check whether the number of selected edges is exactly $n - 1$ to determine whether a valid spanning tree has been constructed.

#### Implementation

```python
class DSU:
    def __init__(self, parent):
        self.parent = parent

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def join(self, x, y):
        px = self.find(x)
        py = self.find(y)
        self.parent[px] = py

MAX_STABILITY = 200000

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        ans = -1

        if len(edges) < n - 1:
            return -1

        mustEdges = [e for e in edges if e[3] == 1]
        optionalEdges = [e for e in edges if e[3] != 1]

        if len(mustEdges) > n - 1:
            return -1

        optionalEdges.sort(key=lambda x: x[2], reverse=True)

        selectedInit = 0
        mustMinStability = MAX_STABILITY
        dsuInit = DSU(list(range(n)))

        for u, v, s, must in mustEdges:
            if dsuInit.find(u) == dsuInit.find(v) or selectedInit == n - 1:
                return -1
            dsuInit.join(u, v)
            selectedInit += 1
            mustMinStability = min(mustMinStability, s)

        l = 0
        r = mustMinStability

        while l < r:
            mid = l + ((r - l + 1) >> 1)
            dsu = DSU(dsuInit.parent[:])
            selected = selectedInit
            doubledCount = 0

            for u, v, s, must in optionalEdges:
                if dsu.find(u) == dsu.find(v):
                    continue

                if s >= mid:
                    dsu.join(u, v)
                    selected += 1
                elif doubledCount < k and s * 2 >= mid:
                    doubledCount += 1
                    dsu.join(u, v)
                    selected += 1
                else:
                    break

                if selected == n - 1:
                    break

            if selected != n - 1:
                r = mid - 1
            else:
                ans = l = mid

        return ans
```

#### Complexity Analysis

Let $m$ be the length of $\textit{edges}$, and $v$ be the upper bound of the binary search.

- Time complexity: $O(m \log m + (n + m \cdot \log n) \cdot \log v)$.

  The `find` operation in the Union-Find structure takes $O(\log n)$ amortized time with path compression alone (without union by rank). Sorting the edges during preprocessing takes $O(m \log m)$ time. Preprocessing the edges with $\textit{must} = 1$ requires $O(m \cdot \log n)$ time.

  The binary search runs for $O(\log v)$ iterations. In each iteration, cloning the initial Union-Find state takes $O(n)$ time, and maintaining the Union-Find structure requires $O(m \cdot \log n)$. Therefore, the overall time complexity is $O(m \log m + (n + m \cdot \log n) \cdot \log v)$.

  > Note: The binary search is not strictly necessary here. Since Kruskal's algorithm processes edges in decreasing weight order, it naturally constructs a maximum spanning tree. After building the tree, the minimum edge weight (after optimally doubling the $k$ smallest tree edges) is the answer. This would simplify the time complexity to $O(m \log m + m \cdot \log n)$.

- Space complexity: $O(n + m)$.

  The Union-Find structure requires $O(n)$ space, and storing the separated edge lists requires $O(m)$ space.

---