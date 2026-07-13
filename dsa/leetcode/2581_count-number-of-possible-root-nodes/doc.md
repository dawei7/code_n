# Count Number of Possible Root Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2581 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Dynamic Programming, Tree, Depth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-number-of-possible-root-nodes](https://leetcode.com/problems/count-number-of-possible-root-nodes/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-number-of-possible-root-nodes/).

### Goal
Given an undirected tree structure defined by edges and a set of directed "guesses" (parent-child relationships), determine how many nodes in the tree could serve as the root such that at least `k` of the provided guesses are satisfied.

### Function Contract
**Inputs**

- `edges`: A list of lists where each inner list `[u, v]` represents an undirected edge between nodes `u` and `v`.
- `guesses`: A list of lists where each inner list `[u, v]` represents a guess that `u` is the parent of `v`.
- `k`: An integer representing the minimum number of satisfied guesses required.

**Return value**

- An integer representing the count of nodes that, when chosen as the root, satisfy at least `k` guesses.

### Examples
**Example 1**

- Input: `edges = [[0,1],[1,2],[1,3],[4,2]], guesses = [[1,3],[0,1],[1,0],[2,4]], k = 3`
- Output: `3`

**Example 2**

- Input: `edges = [[0,1],[1,2],[2,3],[3,4]], guesses = [[1,0],[3,4],[2,1],[3,2]], k = 1`
- Output: `5`

---

## Solution
### Approach
The problem is solved using the **Re-rooting Technique** (a form of Dynamic Programming on Trees).
1. First, perform a DFS to calculate the number of satisfied guesses when node `0` is the root.
2. Perform a second DFS to propagate the count of satisfied guesses as the root moves from a parent to its child. When moving from `u` to `v`, if `(u, v)` was a guess, it becomes unsatisfied, and if `(v, u)` was a guess, it becomes satisfied.

### Complexity Analysis
- **Time Complexity**: `O(N + G)`, where `N` is the number of nodes and `G` is the number of guesses. We traverse the tree twice and perform constant-time lookups using a hash set for guesses.
- **Space Complexity**: `O(N + G)` to store the adjacency list and the set of guesses.

### Reference Implementations
<details>
<summary>python</summary>

```python
import collections

def solve(edges: list[list[int]], guesses: list[list[int]], k: int) -> int:
    n = len(edges) + 1
    adj = collections.defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    guess_set = set(tuple(g) for g in guesses)

    # Initial count of satisfied guesses if root is 0
    current_satisfied = 0

    def dfs_initial(u, p):
        nonlocal current_satisfied
        for v in adj[u]:
            if v != p:
                if (u, v) in guess_set:
                    current_satisfied += 1
                dfs_initial(v, u)

    dfs_initial(0, -1)

    ans = 0

    # Re-rooting DFS
    def dfs_reroot(u, p, count):
        nonlocal ans
        if count >= k:
            ans += 1

        for v in adj[u]:
            if v != p:
                # Transition: moving root from u to v
                # If (u, v) was a guess, it's no longer satisfied
                # If (v, u) was a guess, it becomes satisfied
                next_count = count
                if (u, v) in guess_set:
                    next_count -= 1
                if (v, u) in guess_set:
                    next_count += 1

                dfs_reroot(v, u, next_count)

    dfs_reroot(0, -1, current_satisfied)

    return ans
```
</details>
