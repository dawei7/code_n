### Approach: Dijkstra

#### Intuition

$\textit{Dijkstra}$ is a commonly used algorithm for solving shortest path problems. In this problem, we need to find the shortest path from node $0$ to node $n - 1$, with the special condition that each node has a one-time opportunity to reverse its adjacent edges. However, this special condition can be modeled directly in the graph construction, allowing us to apply the standard $\textit{Dijkstra}$ algorithm without modifying its core logic.

Each node effectively has a “can be used at most once” switch, and the effect of reversing edges applies only to a single move. To incorporate this behavior, for every original edge $[x, y, w]$, we add an additional directed edge $[y, x, 2w]$ to the graph. This transformation encodes the reversal operation directly into the graph structure, so we no longer need to handle it explicitly during the algorithm.

After constructing the graph in this way, we can directly run the $\textit{Dijkstra}$ algorithm to find the shortest path from $0$ to $n - 1$.

It is worth noting that $\textit{Dijkstra}$ can be efficiently implemented using a min-heap. At each step, the node with the smallest tentative distance among all unvisited nodes is extracted from the heap, and the distances of its adjacent nodes are relaxed accordingly. Although a node may be inserted into the heap multiple times, only the first time it is removed from the heap does it need to be processed. This guarantees an overall time complexity of $O(m \log m)$, where $n$ is the number of nodes and $m$ is the number of edges.

#### Implementation

```python
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append((y, w))
            g[y].append((x, 2 * w))

        dist = [inf] * n
        visited = [False] * n
        dist[0] = 0
        heap = [(0, 0)]  # (Distance, Node)

        while heap:
            cur_dist, x = heapq.heappop(heap)

            if x == n - 1:
                return cur_dist

            # already processed
            if visited[x]:
                continue
            visited[x] = True

            # relaxing neighbors
            for y, w in g[x]:
                new_dist = cur_dist + w
                if new_dist < dist[y]:
                    dist[y] = new_dist
                    heapq.heappush(heap, (new_dist, y))

        return -1
```

#### Complexity Analysis

Let $n$ be the number of vertices and $m$ be the number of edges.

- Time complexity: $O(n + m\log m)$.
- Space complexity: $O(n + m)$.

---