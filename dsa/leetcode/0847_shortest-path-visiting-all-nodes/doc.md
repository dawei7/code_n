# Shortest Path Visiting All Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 847 |
| Difficulty | Hard |
| Topics | Dynamic Programming, Bit Manipulation, Breadth-First Search, Graph Theory, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) |

## Problem Description
### Goal
You are given a connected, undirected graph with $n$ nodes labeled from $0$ through $n-1$. The adjacency list `graph[i]` contains every node joined to node `i` by an edge. It contains no self-loop, and every undirected edge is represented in both endpoints' lists.

Find the minimum number of edges in a path that visits every node at least once. The path may begin and end at any nodes, may revisit a node any number of times, and may traverse the same edge more than once; only its total edge count is minimized.

### Function Contract
**Inputs**

- `graph`: the adjacency list of a connected undirected graph with $n$ nodes, where $1 \leq n \leq 12$, `graph[i]` excludes `i`, and $0 \leq \lvert\texttt{graph[i]}\rvert < n$.

**Return value**

Return the length, measured in traversed edges, of the shortest path that visits all $n$ nodes.

### Examples
**Example 1**

- Input: `graph = [[1,2,3],[0],[0],[0]]`
- Output: `4`

One shortest path is `[1,0,2,0,3]`; revisiting the center is necessary.

**Example 2**

- Input: `graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]`
- Output: `4`

The path `[0,1,4,2,3]` visits every node in four edge traversals.

**Example 3**

- Input: `graph = [[]]`
- Output: `0`

The only node is already visited when the path starts.

### Required Complexity
- **Time:** $O(n^2 \cdot 2^n)$
- **Space:** $O(n \cdot 2^n)$

<details>
<summary>Approach</summary>

#### General

**A node alone does not describe progress**

Reaching the same node after visiting different subsets creates different future possibilities. Encode the visited subset as a bitmask: bit $i$ is one exactly when node $i$ has appeared on the path. A search state is therefore `(node, mask)`, not just `node`. Revisiting a graph node is allowed whenever the combined state is new.

**Every possible starting node is a zero-length source**

Because the path may start anywhere, initialize the breadth-first queue with `(node, 1 << node)` for every node, all at distance zero. This is a multi-source BFS over an implicit unweighted state graph. From `(node, mask)`, traversing an edge to `neighbor` produces `(neighbor, mask | (1 << neighbor))`.

Let `full_mask = (1 << n) - 1`. The first generated state whose mask equals `full_mask` gives the answer. BFS processes states in nondecreasing path length, so no later state can reach all nodes with fewer edges.

**Why discarding a repeated state is safe**

Two paths that end at the same `node` with the same `mask` have identical legal continuations. Keeping only the first is sufficient because BFS found it with minimum length; any later copy is no shorter. Every permitted graph walk maps to a sequence of these state transitions, including walks that reuse nodes or edges. Thus the search includes an optimal visiting path and returns exactly its length when the full mask first appears.

#### Complexity detail

There are at most $n2^n$ states. Expanding a state scans the current node's adjacency list; over all masks this is $O(2^n E)$ work for $E$ undirected edges, bounded by $O(n^2 \cdot 2^n)$. The queue and visited set store at most $n2^n$ states, using $O(n \cdot 2^n)$ space.

#### Alternatives and edge cases

- **Subset dynamic programming:** Compute the shortest distance to every `(mask, node)` state through relaxations; it has comparable exponential bounds but BFS matches the unit edge weights more directly.
- **All-pairs distances plus node permutations:** Enumerating every possible visit order is correct when consecutive nodes use shortest paths, but takes factorial time.
- **Search by node only:** Marking a node globally visited is incorrect because returning to it with a larger visited subset can be essential.
- **Single node:** Starting there already visits the complete graph, so the answer is `0`.
- **Trees with branches:** Revisiting articulation points and reusing edges is permitted and may be unavoidable.
- **Complete graph:** A path can visit a new node on every edge, giving length $n-1$.
- **Cycles:** The path need not return to its starting node; visiting all nodes once along the cycle minus one edge is enough.
- **Duplicate queue arrivals:** The `(node, mask)` visited set removes paths with identical future state without forbidding legitimate node revisits.

</details>
