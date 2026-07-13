# Minimum Height Trees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 310 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-height-trees/) |

## Problem Description
### Goal
Given an undirected tree with `n` labeled nodes and $n - 1$ edges, choose any node as its root. The resulting height is the maximum number of edges on a downward route from that root to any other node.

Return every root label that produces the minimum possible height, in any order. A tree has one or two such central nodes; include both when they tie. Re-rooting does not change the undirected edges, only parent-child orientation and measured depth. For a one-node tree, return its sole label. The task returns centers rather than the minimum height itself.

### Function Contract
**Inputs**

- `n`: the number of nodes labelled `0` through $n - 1$
- `edges`: the tree's $n - 1$ undirected edges

**Return value**

The one or two minimum-height root labels, in any order.

### Examples
**Example 1**

- Input: `n = 4, edges = [[1,0],[1,2],[1,3]]`
- Output: `[1]`

**Example 2**

- Input: `n = 6, edges = [[0,3],[1,3],[2,3],[4,3],[5,4]]`
- Output: `[3,4]`

**Example 3**

- Input: `n = 1, edges = []`
- Output: `[0]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Remove equal-height outer layers**

Every leaf has degree one and lies on the tree's current outer boundary. Enqueue all leaves, remove one complete layer at a time, and decrement the degree of each surviving neighbor. A neighbor whose degree becomes one joins the next layer.

Stop when at most two nodes remain. These final nodes are the tree's center or two adjacent centers and are exactly the possible minimum-height roots.

**Why leaves cannot be optimal while an interior remains**

If more than two nodes remain, any current leaf has a single route into the rest of the tree. Moving the root from that leaf to its neighbor shortens the distance to every node beyond the neighbor by one, while increasing distance only to the discarded leaf. The leaf therefore cannot have smaller eccentricity than the interior.

Removing all leaves simultaneously subtracts one from the distance layers surrounding every surviving candidate. It preserves which surviving nodes minimize the maximum distance, so the same argument may be repeated on the smaller tree.

For a six-node path `0-1-2-3-4-5`, removing `0,5` leaves `1-2-3-4`; removing `1,4` leaves centers `2,3`. Rooting at either gives height three, while moving farther from the middle increases the height.

**The final layer is the center of every longest path**

A tree diameter has either one middle vertex or two adjacent middle vertices. Each leaf-trimming round removes one endpoint layer from every longest remaining path. When one or two nodes remain, they are precisely those diameter middles.

For any root, the farthest endpoint of a diameter gives a height at least its distance from that root. A diameter middle minimizes the larger distance to the two endpoints, and no other node can do better. Therefore the final layer contains all and only minimum-height roots.

#### Complexity detail

Building adjacency and degrees takes $O(n)$ time for $n - 1$ edges. Every node enters the leaf queue once and every edge is processed from its removed endpoint at most twice, so trimming is $O(n)$. Adjacency, degrees, and the queue use $O(n)$ space.

#### Alternatives and edge cases

- **Run BFS or DFS from every possible root:** computes every height directly but takes $O(n^2)$.
- **Find a diameter with two searches:** the diameter's middle node or nodes give the same answer in $O(n)$.
- A one-node tree returns that node. A two-node tree has both endpoints as equally optimal roots.

</details>
