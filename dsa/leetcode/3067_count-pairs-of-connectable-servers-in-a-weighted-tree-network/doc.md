# Count Pairs of Connectable Servers in a Weighted Tree Network

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3067 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Tree, Depth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-pairs-of-connectable-servers-in-a-weighted-tree-network](https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/).

### Goal
Given a weighted tree representing a network of servers, identify for every server `i` the number of pairs of other servers `(a, b)` such that the paths from `a` to `i` and `b` to `i` are both divisible by a given integer `signalSpeed`, and these paths only intersect at server `i`.

### Function Contract
**Inputs**

- `edges`: A list of lists where each element `[u, v, w]` represents an undirected edge between nodes `u` and `v` with weight `w`.
- `signalSpeed`: An integer representing the divisor for path weights.

**Return value**

- A list of integers where the `i`-th element is the count of valid server pairs for server `i`.

### Examples
**Example 1**

- Input: `edges = [[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]], signalSpeed = 1`
- Output: `[0,4,6,6,4,0]`

**Example 2**

- Input: `edges = [[0,6,3],[6,5,3],[6,1,1],[1,2,2],[2,3,4],[2,4,4]], signalSpeed = 3`
- Output: `[2,0,0,0,0,0,2]`

---

## Solution
### Approach
The problem is solved using Depth-First Search (DFS) on an adjacency list representation of the tree. For each node, we treat it as a root and explore its subtrees. If a subtree contains `k` nodes whose distance from the root is divisible by `signalSpeed`, these nodes can be paired with nodes from other subtrees of the same root that also satisfy the condition. The total count for a root is the sum of products of counts from distinct subtrees.

### Complexity Analysis
- **Time Complexity**: `O(n^2)`, where `n` is the number of servers. For each of the `n` nodes, we perform a DFS traversal of the tree, which takes `O(n)`.
- **Space Complexity**: `O(n)` to store the adjacency list and the recursion stack.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict
import sys

def solve(edges: list[list[int]], signalSpeed: int) -> list[int]:
    n = len(edges) + 1
    sys.setrecursionlimit(max(sys.getrecursionlimit(), n * 2 + 50))
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    def count_divisible_paths(curr, parent, current_dist):
        count = 1 if current_dist % signalSpeed == 0 else 0
        for neighbor, weight in adj[curr]:
            if neighbor != parent:
                count += count_divisible_paths(neighbor, curr, current_dist + weight)
        return count

    results = [0] * n

    for i in range(n):
        subtree_counts = []
        for neighbor, weight in adj[i]:
            subtree_counts.append(count_divisible_paths(neighbor, i, weight))

        # Calculate pairs: if we have subtrees with counts c1, c2, c3...
        # The number of pairs is the sum of (ci * cj) for all i < j
        total_pairs = 0
        prefix_sum = 0
        for count in subtree_counts:
            total_pairs += prefix_sum * count
            prefix_sum += count

        results[i] = total_pairs

    return results
```
</details>
