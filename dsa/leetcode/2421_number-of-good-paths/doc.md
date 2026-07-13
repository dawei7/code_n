# Number of Good Paths

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2421 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Tree, Union-Find, Graph Theory, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-good-paths](https://leetcode.com/problems/number-of-good-paths/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-good-paths/).

### Goal
Given an undirected tree where each node has an associated value, identify the total number of "good paths." A path between two nodes is considered "good" if the starting node and the ending node share the same value, and every node along the simple path between them has a value less than or equal to that shared value.

### Function Contract
**Inputs**

- `vals`: A list of integers where `vals[i]` represents the value at node `i`.
- `edges`: A list of pairs `[u, v]` representing an undirected edge between nodes `u` and `v`.

**Return value**

- An integer representing the total count of good paths in the tree.

### Examples
**Example 1**

- Input: `vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]`
- Output: `6`

**Example 2**

- Input: `vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]`
- Output: `7`

**Example 3**

- Input: `vals = [1], edges = []`
- Output: `1`

---

## Solution
### Approach
The problem is solved using the **Disjoint Set Union (DSU)** data structure combined with a **sorting-based processing strategy**. By sorting nodes by their values, we can incrementally build the graph. For each unique value, we unite nodes connected by edges whose endpoints have values less than or equal to the current value. Within each connected component, we track the frequency of the current value to calculate the number of valid pairs (good paths) that can be formed.

### Complexity Analysis
- **Time Complexity**: `O(N log N)`, where `N` is the number of nodes. This is dominated by sorting the nodes by their values. The DSU operations take nearly constant time, `O(N α(N))`, where `α` is the inverse Ackermann function.
- **Space Complexity**: `O(N)` to store the adjacency list, the DSU parent/size arrays, and the frequency maps for each component.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(vals: list[int], edges: list[list[int]]) -> int:
    n = len(vals)
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # DSU structures
    parent = list(range(n))
    # count stores the frequency of the max value in the component
    count = [{vals[i]: 1} for i in range(n)]

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            # Merge smaller component into larger one (or just merge)
            if len(count[root_i]) < len(count[root_j]):
                root_i, root_j = root_j, root_i

            parent[root_j] = root_i
            for val, freq in count[root_j].items():
                count[root_i][val] = count[root_i].get(val, 0) + freq
            count[root_j] = {} # Clear memory

    # Sort nodes by value
    nodes = sorted(range(n), key=lambda i: vals[i])

    ans = n  # Every single node is a good path of length 0

    # Process nodes in increasing order of values
    for u in nodes:
        for v in adj[u]:
            if vals[v] <= vals[u]:
                root_u = find(u)
                root_v = find(v)
                if root_u != root_v:
                    # Before merging, calculate paths formed by current value
                    # The number of new paths is (count of u in root_u) * (count of u in root_v)
                    c_u = count[root_u].get(vals[u], 0)
                    c_v = count[root_v].get(vals[u], 0)
                    ans += c_u * c_v
                    union(root_u, root_v)

    return ans
```
</details>
