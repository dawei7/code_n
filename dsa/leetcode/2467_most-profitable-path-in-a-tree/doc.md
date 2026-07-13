# Most Profitable Path in a Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2467 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Tree, Depth-First Search, Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [most-profitable-path-in-a-tree](https://leetcode.com/problems/most-profitable-path-in-a-tree/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/most-profitable-path-in-a-tree/).

### Goal
Given an undirected tree representing a network of nodes, each containing a specific amount of income (or cost), Alice starts at root node 0 and Bob starts at the given `bob` node. Alice moves toward any leaf, while Bob moves one step per turn toward root node 0. When they land on a node, they collect the income; if they arrive at the same time, they split the income. If one arrives after the other, the first person collects the entire amount. The goal is to find the maximum net income Alice can accumulate by the time she reaches any leaf node.

### Function Contract
**Inputs**

- `edges`: A list of lists where each sublist `[u, v]` represents an undirected edge between nodes `u` and `v`.
- `bob`: An integer representing the starting node for Bob.
- `amount`: A list of integers where `amount[i]` is the income/cost at node `i`.

**Return value**

- An integer representing the maximum profit Alice can achieve upon reaching any leaf node.

### Examples
**Example 1**

- Input: `edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]`
- Output: `6`

**Example 2**

- Input: `edges = [[0,1]], bob = 1, amount = [-7280,2350]`
- Output: `-7280`

**Example 3**

- Input: `edges = [[0,1],[1,2],[1,3]], bob = 2, amount = [0,4,2,6]`
- Output: `8`

---

## Solution
### Approach
The problem is solved using a combination of **Depth-First Search (DFS)** and **Breadth-First Search (BFS)**. First, we use DFS to determine the path Bob takes to reach the root and record the time at which he visits each node. Then, we perform a second DFS to simulate Alice's traversal, calculating her cumulative income based on her arrival time relative to Bob's arrival time at each node.

### Complexity Analysis
- **Time Complexity**: `O(N)`, where `N` is the number of nodes in the tree. We traverse the tree a constant number of times.
- **Space Complexity**: `O(N)` to store the adjacency list, the path/time map for Bob, and the recursion stack.

### Reference Implementations
<details>
<summary>python</summary>

```python
import collections

def solve(edges, bob, amount):
    n = len(amount)
    adj = collections.defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Find Bob's path to root (0)
    bob_time = {bob: 0}
    parent = {0: -1}
    stack = [0]

    # Build parent pointers to trace Bob's path
    q = collections.deque([0])
    visited = {0}
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                parent[v] = u
                q.append(v)

    curr = bob
    time = 0
    while curr != 0:
        curr = parent[curr]
        time += 1
        bob_time[curr] = time

    # Alice's DFS
    max_profit = float('-inf')

    def dfs(u, p, time, current_income):
        nonlocal max_profit

        # Calculate income at current node
        if u not in bob_time or time < bob_time[u]:
            current_income += amount[u]
        elif time == bob_time[u]:
            current_income += amount[u] // 2

        # Check if leaf
        is_leaf = True
        for v in adj[u]:
            if v != p:
                is_leaf = False
                dfs(v, u, time + 1, current_income)

        if is_leaf:
            max_profit = max(max_profit, current_income)

    dfs(0, -1, 0, 0)
    return max_profit
```
</details>
