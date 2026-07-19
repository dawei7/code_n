## General
**Rooting the undirected tree at the capital**

Temporarily ignore each road's arrow and root the resulting tree at city `0`. Every city other than `0` then has exactly one parent: its next city on the unique undirected path toward the capital. For that city to reach `0`, the road connecting it to its parent must point from the city to the parent.

This observation removes any global choice. A road that already points from child to parent is correct; a road that points from parent to child must be reversed. Because a tree has no alternate route around that edge, no change elsewhere can compensate for its wrong direction.

**Encoding direction while traversing both ways**

Build an adjacency list that permits traversal across every road in either direction. For an original road `a -> b`, add `(b, 1)` to `a`'s adjacency list: if a traversal rooted at `0` moves from `a` to the unvisited `b`, it is following the original arrow away from the capital, so that road costs one reversal. Also add `(a, 0)` to `b`'s list: traversing from `b` to `a` means the original arrow already points toward the capital and costs nothing.

The numeric marker does not change the graph. It merely remembers how the original directed road aligns with the root-to-child traversal. This avoids maintaining a separate set of original ordered pairs.

**Counting each forced reversal once**

Start a depth-first or breadth-first traversal at city `0`. For each adjacency entry leading to an unvisited city, add its marker to the answer and visit that city. The visited condition prevents walking back over the parent edge, so each of the tree's $n-1$ roads contributes exactly once.

Consider the first sample. From root `0`, crossing the original edge `0 -> 1` uses marker `1`, so it must reverse. From `1`, the edge `1 -> 3` also costs one. The route reaches `2` by traversing the reverse view of `2 -> 3`, which costs zero. Likewise `4 -> 0` costs zero when traversed from `0` to `4`, while `4 -> 5` costs one. The total is three.

**Why the count is both necessary and sufficient**

Every marker-`1` edge points from a parent toward a child in the tree rooted at `0`. The child-side component has no other connection to the capital, so that edge must reverse in every feasible solution; the traversal's count is a lower bound on the answer.

After reversing exactly those counted edges, every parent-child road points from the child to the parent. Repeatedly following parents therefore takes any city one level closer to root `0` until it reaches the capital. The counted changes are sufficient, meet the lower bound, and are consequently minimal.

## Complexity detail
The adjacency list contains two entries per road, hence $2(n-1)$ entries. Building it takes $O(n)$ time, and the traversal visits each city once and inspects each adjacency entry once, also taking $O(n)$ time.

The adjacency lists, visited structure, and explicit traversal stack or queue each use $O(n)$ space. An iterative traversal avoids recursion-depth failures on a chain of up to $5\cdot10^4$ cities.

## Alternatives and edge cases
- **Recursive depth-first search:** It uses the same direction markers and asymptotic bounds, but a chain-shaped tree can exceed Python's recursion limit unless recursion settings or an iterative stack are used.
- **Original-edge set:** Store an undirected adjacency list plus a set of ordered original roads. During traversal, membership of `(parent, child)` determines whether to increment. This is correct but uses a second hash structure instead of embedding the marker in adjacency entries.
- **Repeated reachability checks:** Reversing roads one at a time and retesting which cities reach `0` can take quadratic or worse time and obscures the tree's forced orientation.
- **Already correct orientation:** If every edge points from child to parent under the root-at-zero view, every marker encountered is zero and the answer is `0`.
- **All roads point away from zero:** Every one of the $n-1$ roads must reverse, so the maximum answer is $n-1$.
- **Connection order:** The input pairs may appear in any order. Traversal correctness depends on the tree topology, not the serialization order.
- **Capital as traversal root:** Rooting at a different city changes parent-child relationships and counts the wrong objective. The tree must be rooted specifically at city `0`.
- **No cycles:** The source guarantee that the undirected network is a tree is decisive. A general graph could offer alternate paths, and its minimum-reversal problem would require different reasoning.
