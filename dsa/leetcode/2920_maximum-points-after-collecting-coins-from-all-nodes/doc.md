# Maximum Points After Collecting Coins From All Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2920 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Tree, Depth-First Search, Memoization |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-points-after-collecting-coins-from-all-nodes](https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/).

### Goal
Given a tree rooted at node 0, each node contains a specific number of coins. When visiting a node, you can collect its coins using one of two strategies: either take half the coins (integer division) or take all coins and then halve the coins of all its descendants. Because the halving effect compounds as you move deeper into the tree, the number of coins at any node depends on how many times its ancestors were halved. You must determine the maximum total coins collectable by traversing the tree optimally.

### Function Contract
**Inputs**

- `edges`: A list of lists representing the tree structure (undirected edges).
- `coins`: A list of integers where `coins[i]` is the initial value at node `i`.
- `k`: An integer representing the penalty reduction factor.

**Return value**

- An integer representing the maximum total coins that can be collected.

### Examples
**Example 1**

- Input: `edges = [[0,1],[1,2],[2,3]], coins = [10,10,3,3], k = 5`
- Output: `11`

**Example 2**

- Input: `edges = [[0,1],[0,2]], coins = [8,4,4], k = 0`
- Output: `16`

---

## Solution
### Approach
The problem is solved using Tree Dynamic Programming with Memoization. Since the halving effect only matters up to a certain depth (because `coins[i] // 2^14` eventually becomes 0), we can track the state as `(current_node, parent_node, halving_count)`. The `halving_count` is capped at 13 to prevent redundant states.

### Complexity Analysis
- **Time Complexity**: `O(N * K)`, where `N` is the number of nodes and `K` is the maximum number of effective halving operations (typically 14).
- **Space Complexity**: `O(N * K)` to store the memoization table.

### Reference Implementations
<details>
<summary>python</summary>

```python
import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

def solve(edges, coins, k):
    n = len(coins)
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Memoization table: (node, halving_count)
    # halving_count is capped at 13 because 10^9 // 2^14 is 0
    memo = {}

    def dfs(u, p, halving_count):
        # Cap halving_count at 13
        state = (u, halving_count)
        if state in memo:
            return memo[state]

        # Strategy 1: Take the current coins minus the penalty.
        # This does not add any new halving effect for descendants.
        val1 = (coins[u] >> halving_count) - k
        for v in adj[u]:
            if v != p:
                val1 += dfs(v, u, halving_count)

        # Strategy 2: Take half the current coins and halve the descendants.
        val2 = (coins[u] >> (halving_count + 1))
        for v in adj[u]:
            if v != p:
                val2 += dfs(v, u, min(halving_count + 1, 13))

        res = max(val1, val2)
        memo[state] = res
        return res

    return dfs(0, -1, 0)
```
</details>
