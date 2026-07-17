# Number Of Ways To Reconstruct A Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1719 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Tree, Graph Theory, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/) |

## Problem Description

### Goal

You are given distinct pairs `[x, y]` with $x < y$. The node values appearing anywhere in `pairs` are exactly the nodes of an unknown rooted tree, which may have any number of children per node. A pair is present if and only if one of its values is an ancestor of the other in that tree. An ancestor lies on the root-to-node path and excludes the node itself.

Count how many rooted trees have exactly those ancestor-comparability pairs. Two reconstructions differ when at least one node has a different parent. Return `0` when no tree works, `1` when exactly one works, and `2` when more than one reconstruction works; the exact count beyond one is not required.

### Function Contract

**Inputs**

- `pairs`: between $1$ and $10^5$ distinct two-element arrays `[x, y]`, where $1 \le x < y \le 500$.
- Let $V$ be the number of distinct node values appearing in `pairs`.

**Return value**

- Return `0`, `1`, or `2` according to whether the number of matching rooted trees is zero, exactly one, or greater than one.

### Examples

**Example 1**

- Input: `pairs = [[1,2],[2,3]]`
- Output: `1`
- Explanation: Node $2$ must be the root with $1$ and $3$ as its children, so the reconstruction is unique.

**Example 2**

- Input: `pairs = [[1,2],[2,3],[1,3]]`
- Output: `2`
- Explanation: All three nodes are mutually comparable, and more than one parent assignment forms a valid chain.

**Example 3**

- Input: `pairs = [[1,2],[2,3],[2,4],[1,5]]`
- Output: `0`
- Explanation: No node is comparable with every other node, so none can serve as the required root.

### Required Complexity

- **Time:** $O(V^2)$
- **Space:** $O(V^2)$

<details>
<summary>Approach</summary>

#### General

**Interpret each pair as undirected comparability**

Build an adjacency set for every node: two nodes are adjacent exactly when the input says one must be an ancestor of the other. The root is an ancestor of every other node, so its adjacency degree must be $V-1$. If no such node exists, reconstruction is impossible.

**Choose the nearest possible parent by degree**

For each non-root node `u`, every ancestor of `u` must be adjacent to `u`. A parent must therefore be one of `u`'s neighbors and must have degree at least `u`'s degree, because everything comparable with `u` except that parent must also be comparable with the parent. Among eligible neighbors, choose one with the smallest degree; a larger-degree choice would skip a nearer required ancestor.

After selecting parent `p`, verify that every neighbor of `u` other than `p` also belongs to `p`'s adjacency set. Failure of this containment means the claimed comparabilities cannot be nested along a rooted-tree path, so no reconstruction exists.

**Detect when the parent relation is interchangeable**

If `u` and its selected parent have equal degrees, their comparability neighborhoods provide no evidence that forces which one is above the other. Swapping their parent relationship produces another valid reconstruction, so the answer becomes `2`. Otherwise the relation is forced. If every node passes containment and no equal-degree ambiguity occurs, the reconstruction is unique.

#### Complexity detail

At most $\binom{V}{2}$ distinct pairs exist. Building the adjacency sets takes $O(V^2)$ time and space in the dense case. Across all nodes, parent selection and containment inspect $O(V^2)$ adjacency entries, with each set membership check taking expected $O(1)$ time. The total bounds are therefore $O(V^2)$ time and $O(V^2)$ space.

#### Alternatives and edge cases

- **Explicitly enumerate rooted trees:** Testing parent assignments against the pair set gives a direct oracle on very small node sets, but the number of labeled rooted trees grows exponentially and is unsuitable for the full domain.
- **Linear membership structures:** Adjacency lists raise dense-case containment to $O(V^3)$; checking each required relation by rescanning the raw pair list can take $O(V^4)$.
- **No universal node:** Without a degree-$V-1$ node, no possible root is comparable with every other node, so return `0`.
- **Equal degrees:** Equality between a node and its valid parent is evidence of multiple reconstructions, not an inconsistency.
- **A single pair:** Either endpoint can be the root of the two-node tree, so the result is `2`.
- **Input direction:** Although each pair is stored with its smaller value first, numeric order says nothing about which node is the ancestor.

</details>
