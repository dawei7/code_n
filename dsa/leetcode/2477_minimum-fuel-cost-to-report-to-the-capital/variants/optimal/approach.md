## General

**Root the road tree at the capital.** Starting from city `0`, record each city's parent and a traversal order. Because the graph is a tree, every non-capital city has exactly one parent edge that all representatives in its subtree must cross on their way to the capital.

**Charge each edge by its subtree population.** Suppose a non-capital subtree contains $p$ representatives. At least $\lceil p / \texttt{seats}\rceil$ cars must cross its parent edge because each car carries at most `seats` people. That lower bound is achievable: representatives combine into as few cars as possible before crossing the edge, then may combine again with representatives from sibling subtrees at the parent.

Process cities in reverse traversal order. Initialize every subtree population to one for its local representative. For a city, add `ceil(population / seats)` to the fuel total, then add its population to its parent. The capital has no parent edge, so it contributes no final crossing cost.

The sum is globally minimal because the tree supplies only one route from each city to the capital, and the independently achievable lower bound is met on every edge. An iterative traversal avoids recursion failure on a legal tree that is a chain of $10^5$ cities.

## Complexity detail

Let $n = \lvert\texttt{roads}\rvert + 1$. Building the adjacency list, rooting the tree, and aggregating all subtrees each inspect $O(n)$ vertices or edges, for $O(n)$ time. The adjacency list, parent array, traversal order, and subtree counts require $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Recursive post-order DFS:** It expresses subtree aggregation directly, but a chain-shaped legal tree can exceed Python's recursion limit.
- **Repeated subtree counting:** Recomputing every child-side population independently is correct but can take $O(n^2)$ time on a chain.
- **Leaf-pruning queue:** Populating the tree from leaves toward the capital also achieves $O(n)$ time, though parent/order construction makes the proof especially direct.
- **Only the capital:** With no roads, no representative travels and the answer is zero.
- **Rounding car counts:** Use $\lceil p / \texttt{seats}\rceil$ for every non-capital subtree; integer division that rounds down undercounts partially filled cars.
- **Arbitrary edge order:** Rooting from city `0` determines direction; input edge ordering carries no orientation.
