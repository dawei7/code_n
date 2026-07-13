# Minimize the Total Price of the Trips

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2646 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Tree, Depth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimize-the-total-price-of-the-trips](https://leetcode.com/problems/minimize-the-total-price-of-the-trips/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimize-the-total-price-of-the-trips/).

### Goal
Given an undirected tree representing a network of cities, calculate the minimum total cost of a set of trips. For each trip, you must traverse the unique path between two nodes. You have the option to halve the price of any node, but you cannot halve the prices of two adjacent nodes. The goal is to minimize the sum of all prices across all trips after applying the halving operation optimally.

### Function Contract
**Inputs**

- `n` (int): The number of nodes in the tree.
- `edges` (List[List[int]]): A list of undirected edges representing the tree structure.
- `price` (List[int]): A list where `price[i]` is the cost of visiting node `i`.
- `trips` (List[List[int]]): A list of trips, where each trip is defined by a start and end node.

**Return value**

- `int`: The minimum total cost after applying the halving operation to a subset of non-adjacent nodes.

### Examples
**Example 1**

- Input: `n = 4, edges = [[0,1],[1,2],[1,3]], price = [2,2,10,6], trips = [[0,3],[2,1],[2,3]]`
- Output: `23`

**Example 2**

- Input: `n = 2, edges = [[0,1]], price = [2,2], trips = [[0,0]]`
- Output: `1`

**Example 3**

- Input: `n = 3, edges = [[0,1],[1,2]], price = [4,5,6], trips = [[0,1]]`
- Output: `7`

---

## Solution
### Approach
1. **Path Finding (DFS/BFS)**: Since the graph is a tree, there is a unique path between any two nodes. We use DFS to find the frequency of each node being visited across all trips.
2. **Tree Dynamic Programming**: Once we have the frequency of visits for each node, we define `dp[node][state]` where `state` is 0 (node is not halved) or 1 (node is halved). The recurrence relation is:
   - `dp[u][0] = price[u] * freq[u] + sum(min(dp[v][0], dp[v][1]))`
   - `dp[u][1] = (price[u] // 2) * freq[u] + sum(dp[v][0])`

### Complexity Analysis
- **Time Complexity**: `O(n * T + n)`, where `T` is the number of trips. Finding paths takes `O(n * T)` and the DP traversal takes `O(n)`.
- **Space Complexity**: `O(n + T)`, to store the adjacency list, the frequency array, and the recursion stack.

### Reference Implementations
<details>
<summary>python</summary>

```python
import collections

def solve(n: int, edges: list[list[int]], price: list[int], trips: list[list[int]]) -> int:
    adj = collections.defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    freq = [0] * n

    def get_path(curr, target, parent, path):
        path.append(curr)
        if curr == target:
            return True
        for neighbor in adj[curr]:
            if neighbor != parent:
                if get_path(neighbor, target, curr, path):
                    return True
        path.pop()
        return False

    for start, end in trips:
        path = []
        get_path(start, end, -1, path)
        for node in path:
            freq[node] += 1

    # dp[u][0]: min cost for subtree u, u is NOT halved
    # dp[u][1]: min cost for subtree u, u IS halved
    memo = {}

    def dfs(u, p):
        cost0 = price[u] * freq[u]
        cost1 = (price[u] // 2) * freq[u]

        for v in adj[u]:
            if v == p:
                continue
            c0, c1 = dfs(v, u)
            cost0 += min(c0, c1)
            cost1 += c0

        return cost0, cost1

    res0, res1 = dfs(0, -1)
    return min(res0, res1)
```
</details>
