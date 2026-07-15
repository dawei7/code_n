# Flower Planting With No Adjacent

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1042 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/flower-planting-with-no-adjacent/) |

## Problem Description

### Goal

There are $N$ gardens labeled from $1$ through $N$. Each pair `paths[i] = [x_i, y_i]` describes a bidirectional path connecting gardens $x_i$ and $y_i$. Every garden has at most three paths entering or leaving it.

Plant exactly one of four flower types in each garden. Any two gardens joined directly by a path must receive different flower types.

Return any valid assignment as an array `answer` of length $N$, where `answer[i]` is the type planted in garden $i+1$. Flower types are represented by `1`, `2`, `3`, and `4`, and a valid assignment is guaranteed to exist.

### Function Contract

**Inputs**

- `n`: the number $N$ of gardens, where $1 \le N \le 10^4$.
- `paths`: the $P$ bidirectional paths, where $0 \le P \le 2\cdot10^4$; every entry contains two distinct labels in $[1,N]$, and each garden has degree at most three.

**Return value**

- Any length-$N$ array of flower types from `1` through `4` such that connected gardens have different types.

### Examples

**Example 1**

- Input: `n = 3, paths = [[1,2],[2,3],[3,1]]`
- Output: `[1,2,3]`
- Explanation: Each pair of gardens in the triangle receives different flower types. Other valid assignments are also accepted.

**Example 2**

- Input: `n = 4, paths = [[1,2],[3,4]]`
- Output: `[1,2,1,2]`

**Example 3**

- Input: `n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]`
- Output: `[1,2,3,4]`

### Required Complexity

- **Time:** $O(N+P)$
- **Space:** $O(N+P)$

<details>
<summary>Approach</summary>

#### General

**Build the undirected graph:** Convert each 1-based path endpoint to a 0-based index and add both directions to an adjacency list. This makes every garden's at most three neighbors directly available while it is being assigned.

**Color gardens greedily:** Visit the gardens in label order. For the current garden, collect the nonzero flower types already assigned to its neighbors. Choose the smallest type among `1`, `2`, `3`, and `4` that is absent from that set. Neighbors processed later are still uncolored and will avoid the current choice when their turns arrive.

**Use the degree guarantee:** A garden has at most three neighbors, so at most three flower types can be forbidden when it is processed. Among four types, at least one is always available; the greedy step can never get stuck.

For every path, whichever endpoint is processed second observes the type already assigned to the first endpoint and chooses a different type. Therefore every connected pair differs in the completed assignment. This argument applies independently to disconnected components and isolated gardens.

#### Complexity detail

Building the adjacency list takes $O(N+P)$ time and space. Across all gardens, neighbor inspection visits $2P$ adjacency entries, and checking the fixed set of four flower types costs $O(N)$ total. The answer and adjacency list therefore give $O(N+P)$ space.

#### Alternatives and edge cases

- **Depth-first or breadth-first traversal:** Components may be colored in traversal order using the same smallest-available rule. The degree guarantee still ensures a free type, with the same asymptotic cost.
- **Backtracking graph coloring:** Trying colors recursively is unnecessary here; the maximum degree of three and availability of four types make every greedy order succeed.
- **Rescan every path per garden:** Finding neighbors by traversing all $P$ paths for each garden remains correct but costs $O(NP)$ time.
- **Isolated gardens:** A garden with no paths may use any type; the deterministic greedy implementation assigns type `1`.
- **Disconnected graph:** Components have no constraints between them and may reuse the same flower types.
- **Maximum degree:** Even when three already colored neighbors use three distinct types, the fourth type remains available.
- **Non-unique output:** Many assignments may be valid; correctness depends on the path constraints, not on matching one particular color permutation.

</details>
