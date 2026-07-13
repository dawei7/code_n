# Cycle Length Queries in a Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2509 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [cycle-length-queries-in-a-tree](https://leetcode.com/problems/cycle-length-queries-in-a-tree/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/cycle-length-queries-in-a-tree/).

### Goal
Given a perfect binary tree where nodes are labeled from 1 to $2^n - 1$ (where node $i$ has children $2i$ and $2i+1$), calculate the length of the cycle formed by adding an edge between two nodes $u$ and $v$. The cycle length is defined as the number of edges in the path between $u$ and $v$ plus the new edge connecting them.

### Function Contract
**Inputs**

- `n` (int): The power of 2 defining the tree depth (nodes are labeled up to $2^n - 1$).
- `queries` (List[List[int]]): A list of pairs $[u, v]$, where each pair represents an edge added between nodes $u$ and $v$.

**Return value**

- `List[int]`: A list containing the cycle length for each query.

### Examples
**Example 1**

- Input: `n = 3, queries = [[5, 3], [4, 7], [2, 3]]`
- Output: `[4, 5, 3]`

**Example 2**

- Input: `n = 2, queries = [[1, 2]]`
- Output: `[2]`

**Example 3**

- Input: `n = 3, queries = [[7, 1]]`
- Output: `[3]`

---

## Solution
### Approach
The problem relies on the properties of a binary heap-indexed tree. For any node $i$, its parent is $\lfloor i/2 \rfloor$. To find the distance between two nodes $u$ and $v$, we find their Lowest Common Ancestor (LCA) by iteratively moving the larger node index towards the root until both indices are equal. The distance is the sum of the number of steps taken to reach the LCA from both $u$ and $v$. The cycle length is simply `distance(u, v) + 1`.

### Complexity Analysis
- **Time Complexity**: $O(Q \cdot n)$, where $Q$ is the number of queries and $n$ is the depth of the tree. Each query takes $O(n)$ time to traverse up to the root.
- **Space Complexity**: $O(Q)$ to store the results of the queries.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(n: int, queries: List[List[int]]) -> List[int]:
    """
    Calculates the cycle length for each query in a perfect binary tree.
    In a perfect binary tree where node i has children 2i and 2i+1,
    the parent of node i is i // 2.
    The distance between two nodes u and v is the number of edges on the
    unique path between them. Adding an edge (u, v) creates a cycle of
    length distance(u, v) + 1.
    """
    results = []

    for u, v in queries:
        dist = 0
        curr_u, curr_v = u, v

        # Move nodes up until they meet at the Lowest Common Ancestor (LCA)
        while curr_u != curr_v:
            if curr_u > curr_v:
                curr_u //= 2
            else:
                curr_v //= 2
            dist += 1

        # The cycle length is the path length + 1 (the new edge)
        results.append(dist + 1)

    return results
```
</details>
