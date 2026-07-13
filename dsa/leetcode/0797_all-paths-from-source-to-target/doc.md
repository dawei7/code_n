# All Paths From Source to Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 797 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Backtracking, Depth-First Search, Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/all-paths-from-source-to-target/) |

## Problem Description

### Goal

Given a directed acyclic graph as an adjacency list, nodes are numbered from `0` through $n - 1$, and `graph[i]` lists every node reachable by one outgoing edge from `i`.

Return every directed path from source node `0` to target node $n - 1$, with each path represented by its complete sequence of node numbers including both endpoints. Paths may be returned in any order, and the acyclic guarantee prevents a path from looping indefinitely.

### Function Contract

**Inputs**

- `graph`: an adjacency list in which `graph[i]` contains every node reachable by one outgoing edge from node `i`.

**Return value**

- A list of all source-to-target paths, with each path represented by its sequence of node numbers. The paths may be returned in any order.

### Examples

**Example 1**

- Input: `graph = [[1,2],[3],[3],[]]`
- Output: `[[0,1,3],[0,2,3]]`
- Explanation: The source has two branches, and each reaches the target.

**Example 2**

- Input: `graph = [[1],[]]`
- Output: `[[0,1]]`
- Explanation: The only edge is also the only complete path.

**Example 3**

- Input: `graph = [[4,3,1],[3,2,4],[3],[4],[]]`
- Output: `[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]`
- Explanation: A path may go directly to node `4` or follow any directed branch that eventually reaches it.

### Required Complexity

- **Time:** $O(V + E + P \cdot V)$
- **Space:** $O(V + E + P \cdot V)$

<details>
<summary>Approach</summary>

#### General

**Identify branches that can finish**

Reverse every edge and traverse backward from target $n - 1$. A node marked by this traversal has at least one route to the target. This preprocessing prevents the enumerator from exploring a large directed subgraph whose paths can never become answers.

**Build one path in place**

Start a depth-first search at node `0` with a mutable path containing the source. For each outgoing neighbor that can reach the target, append it, recurse, and then remove it before considering the next branch. The graph is acyclic, so the recursion cannot revisit a node already on the same path indefinitely and does not need a visited set.

Whenever the search reaches $n - 1$, copy the current path into the result. Every recorded sequence follows graph edges from source to target, so it is valid. Conversely, every valid path uses only nodes marked by the reverse traversal, and DFS considers its next edge at every node; induction along that sequence shows the search records it. Backtracking gives each distinct path exactly one sequence of branch choices.

#### Complexity detail

Let `V` and `E` be the numbers of nodes and edges, and let `P` be the number of returned paths. Building and traversing the reverse graph takes $O(V + E)$. Enumerating and copying paths takes $O(P \cdot V)$ in the worst case because a path contains at most `V` nodes. The reverse graph, reachability marks, and recursion use $O(V + E)$ space, while the required output can occupy $O(P \cdot V)$ space.

#### Alternatives and edge cases

- **Plain backtracking:** DFS without reverse reachability is shorter and has the same output-sensitive behavior when every reachable branch can reach the target, but it may enumerate exponentially many dead prefixes.
- **Memoized suffix paths:** Caching all target-reaching suffixes from each node avoids repeated dead searches, but it retains many intermediate path lists and requires careful copying when prefixes are attached.
- **Breadth-first path expansion:** A queue can enumerate the same answers, but storing many partial paths simultaneously generally uses more memory than depth-first backtracking.
- **No source-to-target route:** If node `0` is not marked as target-reaching, return an empty list.
- **Direct edge:** `[0, n - 1]` is a complete answer even when longer alternatives also exist.
- **Merging branches:** Different prefixes that reach the same node remain distinct paths and must all be returned.
- **Output order:** Traversal order may vary; correctness depends on the set of paths, not their ordering.

</details>
