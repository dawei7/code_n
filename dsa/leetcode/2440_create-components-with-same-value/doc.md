# Create Components With Same Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2440 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Tree, Depth-First Search, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [create-components-with-same-value](https://leetcode.com/problems/create-components-with-same-value/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/create-components-with-same-value/).

### Goal
Given an undirected tree represented by node values and edges, determine the maximum number of components the tree can be partitioned into by removing edges such that the sum of node values in every resulting component is identical.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the value of each node.
- `edges`: A list of pairs representing the undirected connections between nodes.

**Return value**

- An integer representing the maximum number of edges that can be removed so every resulting component has the same value sum.

### Examples
**Example 1**

- Input: `nums = [6,2,2,2,6], edges = [[0,1],[1,2],[1,3],[3,4]]`
- Output: `2`

**Example 2**

- Input: `nums = [2], edges = []`
- Output: `0`

**Example 3**

- Input: `nums = [1,2,1,2,1], edges = [[0,1],[1,2],[2,3],[3,4]]`
- Output: `0`

---

## Solution
### Approach
The problem relies on **DFS (Depth-First Search)** for tree traversal and **Divisor Enumeration**. Since the total sum of the tree must be partitioned into $k$ equal parts, $k$ must be a divisor of the total sum. We iterate through possible values of $k$ (starting from the largest possible) and use a post-order DFS to check if the tree can be partitioned into components of size `total_sum / k`.

### Complexity Analysis
- **Time Complexity**: $O(N \cdot d(S))$, where $N$ is the number of nodes and $d(S)$ is the number of divisors of the total sum $S$. For each divisor, we perform a linear time DFS traversal.
- **Space Complexity**: $O(N)$ to store the adjacency list and the recursion stack.

### Reference Implementations
<details>
<summary>python</summary>

```python
import collections

def solve(nums: list[int], edges: list[list[int]]) -> int:
    n = len(nums)
    if n == 0:
        return 0

    total_sum = sum(nums)
    adj = collections.defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def can_partition(target: int) -> bool:
        # Returns the sum of the current subtree if it can be partitioned,
        # otherwise returns -1.
        def dfs(u, p):
            current_sum = nums[u]
            for v in adj[u]:
                if v == p:
                    continue
                res = dfs(v, u)
                if res == -1:
                    return -1
                current_sum += res

            if current_sum == target:
                return 0
            return current_sum

        return dfs(0, -1) == 0

    # We want to maximize k, which means minimizing target_sum = total_sum / k.
    # k can range from n down to 1.
    # target_sum must be a divisor of total_sum.
    # The smallest possible target_sum is max(nums).

    max_val = max(nums)
    for k in range(n, 0, -1):
        if total_sum % k == 0:
            target = total_sum // k
            if target >= max_val:
                if can_partition(target):
                    return k - 1

    return 0
```
</details>
