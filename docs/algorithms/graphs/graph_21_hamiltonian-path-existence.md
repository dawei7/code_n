# Hamiltonian Path Existence

| | |
|---|---|
| **ID** | `graph_21` |
| **Category** | graphs |
| **Complexity (required)** | $O(V!)$ Time, $O(V)$ Space |
| **Difficulty** | 7/10 |
| **Interview relevance** | 3/10 |
| **GeeksForGeeks Equivalent** | [Hamiltonian Cycle](https://www.geeksforgeeks.org/hamiltonian-cycle/) |

## Problem statement

Given an unweighted graph (either directed or undirected). Determine if there exists a Hamiltonian Path.
A Hamiltonian Path is a path that visits every single vertex in the graph exactly once.
(A Hamiltonian Cycle is a Hamiltonian Path that also contains an edge connecting the final vertex back to the starting vertex).

**Input:** Number of vertices `V` and an adjacency list `adj`.
**Output:** A boolean. `True` if a Hamiltonian Path exists, `False` otherwise.

## When to use it

- To solve the unweighted decision-variant of the Travelling Salesperson Problem.
- Like Graph Coloring, this is **NP-Complete**. Since we don't care about the *shortest* path (no edge weights), DP optimization (Held-Karp) is overkill unless checking all paths. We generally just use pure Backtracking.

## Approach

**1. The Backtracking State:**
We maintain an array `path[]` that stores the ordered sequence of vertices we are visiting.
We also maintain a `visited` set to ensure we don't visit the same vertex twice (which would violate the definition of a Hamiltonian Path).

**2. The Recursive Step:**
Our recursive function `backtrack(curr, path_length)` attempts to grow the path.
If `path_length == V`, we did it! We successfully touched every node exactly once! Return `True`.
Otherwise, iterate through all `neighbors` of `curr`.
If a `neighbor` is NOT in `visited`:
- Add it to `visited` and append it to `path`.
- Recurse: `if backtrack(neighbor, path_length + 1) == True: return True`.
- Backtrack: Remove it from `visited` and pop it from `path`.

**3. The Global Loop:**
Because we don't know *which* vertex the Hamiltonian Path might start from, we must wrap our backtracking function in a global loop that attempts to start the path from `0`, then `1`, then `2`, etc., until one succeeds.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for graph_21: Hamiltonian Path Existence.

DFS from 0. Stop at n-1 when count == n.
"""


def solve(n, edges):
    if n <= 1:
        return n == 1
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    visited = [False] * n
    visited[0] = True

    def dfs(u, count):
        if count == n:
            return u == n - 1
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                if dfs(v, count + 1):
                    return True
                visited[v] = False
        return False

    return dfs(0, 1)
```

</details>

## Walk-through

`V = 4`. `adj = {0:[1,2], 1:[0,3], 2:[0,3], 3:[1,2]}`. (A square `0-1-3-2-0`).

1. **Start `0`:** `visited={0}`, `path=[0]`.
   - `backtrack(0, 1)`:
     - Try neighbor `1`. `visited={0,1}`.
     - `backtrack(1, 2)`:
       - Try neighbor `3`. `visited={0,1,3}`.
       - `backtrack(3, 3)`:
         - Try neighbor `2`. `visited={0,1,3,2}`.
         - `backtrack(2, 4)`:
           - `length == 4 == V`. RETURN `True`!
2. Success bubbles up. The path is `[0, 1, 3, 2]`. ✓

*Note: If we wanted to check for a Hamiltonian CYCLE, at the very end when `length == V`, we would add one extra check: `if path[0] in adj[curr]: return True`.*

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(V)$ | $O(V)$ |
| **Average** | $O(V!)$ | $O(V)$ |
| **Worst** | $O(V!)$ | $O(V)$ |

In the worst-case scenario (a highly dense graph where NO Hamiltonian Path exists), the algorithm explores every single valid permutation of the vertices before failing. The number of permutations of V vertices is V!. Time complexity is mathematically bounded by $O(V!)$.
Space complexity is strictly $O(V)$ for the `visited` set, the `path` array, and the maximum depth of the recursion stack.

## Variants & optimizations

- **Dirac's Theorem (Mathematical Shortcut):** If the graph is simple and has V \ge 3 vertices, and EVERY single vertex has a degree \ge \frac{V}{2}, then the graph is mathematically guaranteed to contain a Hamiltonian Cycle! You don't even need to run an algorithm to answer `True`!
- **Held-Karp DP:** You can apply the exact same DP Bitmasking from TSP (`graph_20`). `dp(mask, curr)` returns a Boolean. The transition is `dp(mask, curr) = ANY(dp(mask | (1 << nxt), nxt))`. This solves Hamiltonian Path in $O(V^2 2^V)$ time instead of $O(V!)$, making V=20 solvable in milliseconds!

## Real-world applications

- **Knight's Tour:** Can a chess Knight visit every square on an 8 x 8 chessboard exactly once? This is exactly the Hamiltonian Path problem applied to a 64-vertex graph where edges represent valid L-shaped jumps!

## Related algorithms in cOde(n)

- **[graph_20 - Travelling Salesperson](graph_20_travelling-salesman-held-karp-dp.md)** — The Weighted (Optimization) variant of this exact problem.
- **[graph_19 - M-Coloring Problem](graph_19_m-coloring-problem.md)** — Another classic NP-Complete Graph algorithm solvable purely via Backtracking.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
