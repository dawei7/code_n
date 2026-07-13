# Redundant Connection II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 685 |
| Difficulty | Hard |
| Topics | Depth-First Search, Breadth-First Search, Union-Find, Graph Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/redundant-connection-ii/) |

## Problem Description
### Goal
A rooted tree is a directed graph with one root having no parent, every other node having exactly one parent, and every node reachable as a descendant of the root. The input began as such a tree on nodes `1` through `n`, then one extra directed edge was added.

Return one input edge whose removal restores a rooted tree. Edge `[u, v]` points from parent candidate `u` to child candidate `v`. If several removals would produce a valid rooted tree, return the qualifying edge that occurs last in the input order.

### Function Contract
**Inputs**

- `edges`: `n` directed edges `[parent, child]` on nodes labeled `1` through `n`

**Return value**

- The endpoints of the last input edge whose removal restores a rooted directed tree

### Examples
**Example 1**

- Input: `edges = [[1,2],[1,3],[2,3]]`
- Output: `[2,3]`

**Example 2**

- Input: `edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]`
- Output: `[4,1]`

**Example 3**

- Input: `edges = [[2,1],[3,1],[4,2],[1,4]]`
- Output: `[2,1]`

### Required Complexity

- **Time:** $O(N \alpha(N))$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**First identify whether a node has two parents**

Scan edges in input order while recording the first incoming edge for each child. If another edge enters the same child, save the earlier edge as `first_parent` and the later one as `second_parent`. A rooted tree cannot contain both, and no other node can have this conflict under the one-extra-edge contract.

**Test connectivity while tentatively skipping the later parent**

Run undirected union-find over the edges, omitting `second_parent` when it exists. Direction is irrelevant for detecting the single underlying cycle: if an edge joins endpoints already in the same component, a cycle remains.

**Resolve the three structural cases**

If there was no two-parent conflict, the union failure is the pure cycle's last input edge and must be removed. If a conflict exists and skipping the later edge removes every cycle, `second_parent` is the answer: its removal restores the rooted tree. If a cycle still appears while the later edge is skipped, the earlier parent edge lies on that cycle, so `first_parent` must be removed instead.

**Why these cases are exhaustive**

Adding one edge to a rooted tree can create a cycle, a second parent, or both. The indegree scan detects exactly the second-parent condition, and the union pass after the tentative skip distinguishes whether the earlier parent participates in a remaining cycle. Each returned edge removes the unique structural defect, and choosing the later conflicting edge whenever both choices restore a tree enforces the input-order rule.

#### Complexity detail

Both scans process `N` edges. Path compression and union by size make each disjoint-set operation amortized $O(\alpha(N))$, for $O(N \alpha(N))$ time. Incoming-edge, parent, and size arrays use $O(N)$ space.

#### Alternatives and edge cases

- **Remove and validate every edge:** test indegrees, find a root, and traverse the remaining graph for every candidate; it is direct but takes $O(N^2)$ time.
- **Directed DFS with cycle and indegree bookkeeping:** can solve the cases in linear time, but coordinating cycle membership with the last valid edge is more intricate.
- **Topological pruning:** can isolate cycle nodes after handling indegrees, though union-find expresses the case split more compactly.
- In the two-parent case, the later incoming edge is preferred unless skipping it leaves a cycle.
- A pure directed cycle has no two-parent node; return the cycle edge encountered last in input order.
- Edge direction must be preserved in the returned pair even though union-find treats endpoints as undirected for cycle detection.

</details>
