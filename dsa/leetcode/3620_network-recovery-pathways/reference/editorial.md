### Approach 1: Binary Answer + Shortest Path (Dijkstra)

#### Intuition

Let's first summarize the key observations from the problem:

1. We are given a directed graph, where the online status of each node is determined by the array $\textit{online}$.
2. An edge is considered **valid** only if both of its endpoints are online.
3. We need to find a path from node $0$ to node $n - 1$ whose total edge weight does not exceed $k$, and every node on the path must be online.
4. The **score** of a path is defined as the minimum edge weight along that path. Our goal is to maximize this score.
5. If no valid path exists, return $-1$.

Problems that ask us to **maximize the minimum value** often exhibit a monotonic property, making binary search a natural solution.

Suppose there exists a path from node $0$ to node $n - 1$ such that
1. its total weight is at most $k$, and
2. its minimum edge weight is at least $x$.

Then, for any threshold $y \le x$, the same path also satisfies
1. its total weight is still at most $k$, and
2. every edge weight is at least $y$.

Therefore,
* if $\textit{check}(x)$ is feasible, then $\textit{check}(y)$ is also feasible for every $y \le x$;
* if $\textit{check}(x)$ is infeasible, then $\textit{check}(z)$ is also infeasible for every $z > x$.

This monotonicity allows us to binary search the answer.

For each candidate value $\textit{mid}$, we check whether a valid path exists under the following restriction:
1. Only edges whose weights are at least $\textit{mid}$ may be used.
2. The total weight of the path must not exceed $k$.

If $\textit{check}(\textit{mid})$ returns `true`, then a path exists whose minimum edge weight is at least $\textit{mid}$, so we try a larger threshold.

Otherwise, no such path exists, and we decrease the threshold.

The remaining question is how to implement `check()`. In this approach, we use **Dijkstra's algorithm**.

The procedure is straightforward:

1. Build the graph using only edges whose endpoints are both online.
2. For each candidate threshold $\textit{mid}$:
   * Ignore every edge whose weight is smaller than $\textit{mid}$.
   * Run Dijkstra's algorithm to compute the shortest path from node $0$ to node $n - 1$.
   * If the shortest distance is at most $k$, then $\textit{mid}$ is feasible.

#### Implementation

```python
class Solution:
    def findMaxPathScore(
        self, edges: List[List[int]], online: List[bool], k: int
    ) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        l, r = float("inf"), 0

        for u, v, w in edges:
            if not online[u] or not online[v]:
                continue
            g[u].append((v, w))
            l = min(l, w)
            r = max(r, w)

        def check(mid: int) -> bool:
            dis = [float("inf")] * n
            pq = [(0, 0)]
            dis[0] = 0

            while pq:
                d, u = heapq.heappop(pq)

                if d > k:
                    return False
                if u == n - 1:
                    return True
                if d > dis[u]:
                    continue

                for v, w in g[u]:
                    if w < mid:
                        continue
                    if dis[v] > dis[u] + w:
                        dis[v] = dis[u] + w
                        heapq.heappush(pq, (dis[v], v))
            return False

        if not check(l):
            return -1

        while l <= r:
            mid = (l + r) >> 1
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r
```

#### Complexity Analysis

Let $V$ be the number of nodes, $E$ be the number of edges, and $U$ be the maximum edge weight.

- Time complexity: $O((E + V) \log V \log U)$

  Constructing the graph takes $O(E)$ time. Binary search performs $O(\log U)$ iterations, and each iteration runs Dijkstra's algorithm in $O((V + E)\log V)$ time.

- Space complexity: $O(V +E)$.

  The adjacency list requires $O(V + E)$ space, while the temporary arrays used in `check()` require $O(V)$ space.

---

### Approach 2: Binary Answer + Memoization Search

#### Intuition

In this approach, we implement `check()` using memoized depth-first search. As before, we first construct the graph using only online nodes.

Define $\textit{dfs}(u)$ as the minimum total path weight from node $u$ to node $n - 1$, considering only edges whose weights are at least $\textit{mid}$.

For every outgoing edge $(u, v)$ with weight $w \ge \textit{mid}$, we have the transition

$\textit{dfs}(u)=\min_v(\textit{dfs}(v)+w).$

The recursion starts from node $0$, while the base case is
$\textit{dfs}(n-1)=0.$

To avoid repeated computation, we use a memoization array, where $\text{memo}[u]$ stores the minimum total path weight from node $u$ to node $n-1$.

Finally, if $\textit{dfs}(0)\le k$, then a valid path exists under the current threshold. Otherwise, no valid path exists.

#### Implementation

```python
class Solution:
    def findMaxPathScore(
        self, edges: List[List[int]], online: List[bool], k: int
    ) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        l, r = float("inf"), 0

        for u, v, w in edges:
            if not online[u] or not online[v]:
                continue
            g[u].append((v, w))
            l = min(l, w)
            r = max(r, w)

        def check(mid: int) -> bool:
            memo = [-1] * n

            def dfs(u: int) -> int:
                if u == n - 1:
                    return 0
                if memo[u] != -1:
                    return memo[u]

                res = float("inf")
                for v, w in g[u]:
                    if w >= mid:
                        res = min(res, dfs(v) + w)

                memo[u] = res
                return res

            return dfs(0) <= k

        if not check(l):
            return -1

        while l <= r:
            mid = (l + r) >> 1
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1

        return r
```

#### Complexity Analysis

Let $V$ be the number of nodes, $E$ the number of edges, and $U$ the maximum edge weight.

- Time complexity: $O((V + E) \log U)$.

- Space complexity: $O(V + E)$.

---

### Approach 3: Binary Answer + Topological Sorting + Dynamic Programming

#### Intuition

Instead of memoized DFS, we can compute the minimum path weight using **topological sorting** combined with dynamic programming.

Before processing the graph, we first remove nodes that are unreachable from node $0$.

Let $\text{dp}[u]$ denote the minimum total path weight from node $0$ to node $u$.

For every edge $u \rightarrow v$ whose weight satisfies $w\ge\textit{mid},$ the transition is $\text{dp}[v]=\min(\text{dp}[v],\text{dp}[u]+w).$

The topological order lets us process vertices from node $0$ toward node $n-1$, updating each state exactly once.

Conceptually, this approach is equivalent to the memoized DFS in Approach 2. Memoized DFS computes the states recursively from the destination back to the source, while topological DP computes them iteratively from the source to the destination.

#### Implementation

```python
class Solution:
    def findMaxPathScore(
        self, edges: List[List[int]], online: List[bool], k: int
    ) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        deg = [0] * n
        l, r = float("inf"), 0

        for u, v, w in edges:
            if not online[u] or not online[v]:
                continue
            g[u].append((v, w))
            deg[v] += 1
            l = min(l, w)
            r = max(r, w)

        # Delete unreachable nodes
        q = deque([i for i in range(1, n) if deg[i] == 0])
        while q:
            u = q.popleft()
            for v, _ in g[u]:
                deg[v] -= 1
                if v and deg[v] == 0:
                    q.append(v)

        def check(mid: int) -> bool:
            dp = [math.inf] * n
            cdeg = deg.copy()
            dp[0] = 0

            q = deque([0])
            while q:
                u = q.popleft()
                if u == n - 1:
                    return dp[u] <= k

                for v, w in g[u]:
                    if w >= mid:
                        dp[v] = min(dp[v], dp[u] + w)
                    cdeg[v] -= 1
                    if cdeg[v] == 0:
                        q.append(v)
            return False

        if not check(l):
            return -1

        while l <= r:
            mid = (l + r) >> 1
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1

        return r
```

#### Complexity Analysis

Let $V$ be the number of nodes, $E$ the number of edges, and $U$ be the maximum edge weight.

- Time complexity: $O((V + E) \log U)$.

- Space complexity: $O(V + E)$.

---