# Minimum Time to Collect All Apples in a Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1443 |
| Difficulty | Medium |
| Topics | Hash Table, Tree, Depth-First Search, Breadth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/) |

## Problem Description
### Goal

An undirected tree has $n$ vertices numbered from $0$ through $n-1$. Some
vertices contain an apple. Traversing either direction across one edge costs
one second, and any apple at a visited vertex is collected.

The journey must start at vertex $0$, collect every apple in the tree, and
return to vertex $0$. The array `edges` lists the tree's $n-1$ undirected
connections, while `hasApple[i]` states whether vertex `i` contains an
apple. Return the minimum total traversal time required for the complete
round trip.

### Function Contract
**Inputs**

- `n`: the number of vertices, where $1 \le n \le 10^5$.
- `edges`: a list of exactly $n-1$ pairs `[a, b]` describing an
  undirected tree on vertices $0$ through $n-1$.
- `hasApple`: a Boolean list of length $n$; `hasApple[i]` is true exactly
  when vertex `i` has an apple.

**Return value**

Return the minimum number of seconds needed to start at vertex $0$, collect
all apples, and finish again at vertex $0$.

### Examples
**Example 1**

- Input: `n = 7, edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], hasApple = [false, false, true, false, true, true, false]`
- Output: `8`
- Explanation: The required part of the tree contains four edges, each of
  which must be traversed once outward and once on the return.

**Example 2**

- Input: `n = 7, edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], hasApple = [false, false, true, false, false, true, false]`
- Output: `6`

**Example 3**

- Input: `n = 7, edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], hasApple = [false, false, false, false, false, false, false]`
- Output: `0`

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Identify the only edges that can belong to an optimal walk**

Root the tree at vertex $0$. For any non-root vertex $v$, the edge joining
$v$ to its parent separates the entire subtree of $v$ from the root. That
edge is useful precisely when the subtree contains at least one apple. If the
subtree has no apple, entering it cannot help and only adds cost.

If the subtree does contain an apple, every valid journey must cross its
parent edge to reach that apple. Because the journey must finish back at
vertex $0$ and a tree has no alternate route, it must cross the same edge
again in the opposite direction. Consequently, every required edge contributes
exactly two seconds, and every unnecessary edge contributes zero.

**Establish parent relationships without recursive-depth risk**

Build an adjacency list for the undirected edges. Starting at vertex $0$,
perform an iterative depth-first traversal that records each vertex's parent
and appends vertices to an `order` list. A tree has exactly one path from
the root to each vertex, so skipping the recorded parent is enough to avoid
walking back and forth during this traversal.

An iterative traversal is important for the upper bound $n=10^5$: a tree may
be one long chain, which can exceed Python's recursion depth even though the
algorithm itself is linear.

**Propagate apple requirements from children to parents**

Process `order` in reverse so every child is handled before its parent.
Maintain `needed[v]`, which is true when vertex $v$ or any vertex in its
rooted subtree contains an apple. It begins as a copy of `hasApple`.

For each non-root vertex $v$, if `needed[v]` is true, add two seconds for
the edge between $v$ and its parent and set `needed[parent[v]]` to true.
This propagation ensures that an apple at any depth marks every edge on its
unique route to the root, while shared ancestors are charged only once.

The resulting sum is attainable: traverse the union of all marked root-to-
apple paths depth-first, returning along each edge after its subtree is
finished. It is also a lower bound because every marked edge is the sole
connection between at least one apple and the root and therefore must be
crossed in both directions. Since the construction meets that lower bound,
the total is minimum.

#### Complexity detail

The tree contains $n-1$ edges. Building the adjacency list touches each edge
twice, the rooting traversal visits every vertex and adjacency entry once,
and the reverse propagation processes every vertex once. The total time is
$O(n)$. The adjacency list, parent array, traversal order, stack, and
`needed` flags together use $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Recursive postorder DFS:** A recursive function can return whether a
  subtree contains an apple and add two for each required child edge. It has
  the same asymptotic bounds but can overflow the call stack on a legal
  $10^5$-vertex chain unless recursion limits and stack capacity are handled.
- **Walk from every apple to the root:** Marking all ancestors separately is
  correct when required edges are deduplicated, but a chain with many apples
  repeats the same long prefixes and can take $O(n^2)$ time.
- **Leaf pruning:** Repeatedly remove apple-free leaves until only the minimal
  root-connected apple subtree remains. With degrees and a queue this can also
  be $O(n)$, but the rooted postorder formulation maps more directly to the
  required-edge proof.
- **No apples:** No edge is required, so the correct round trip stays at the
  root and costs zero.
- **Apple only at vertex zero:** The apple is already collected at the start;
  no traversal is necessary.
- **Multiple apples on one branch:** An apple at an ancestor does not add a
  second charge to edges already required by a deeper apple. Each edge is
  counted once, then traversed twice.
- **Apples in different branches:** Their paths share the upper edges near the
  root. Propagated Boolean state naturally deduplicates that common route.

</details>
