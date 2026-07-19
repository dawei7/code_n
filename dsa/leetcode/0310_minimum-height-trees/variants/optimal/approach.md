## General
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

## Complexity detail
Building adjacency and degrees takes $O(n)$ time for $n - 1$ edges. Every node enters the leaf queue once and every edge is processed from its removed endpoint at most twice, so trimming is $O(n)$. Adjacency, degrees, and the queue use $O(n)$ space.

## Alternatives and edge cases
- **Run BFS or DFS from every possible root:** computes every height directly but takes $O(n^2)$.
- **Find a diameter with two searches:** the diameter's middle node or nodes give the same answer in $O(n)$.
- A one-node tree returns that node. A two-node tree has both endpoints as equally optimal roots.
