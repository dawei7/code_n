## General

Only one root-to-deepest-node path matters. Edges outside that path are explicitly ignored, and every deepest node has the same number of edges from root `1`. The solution therefore needs two ingredients:

1. find the maximum depth `d` of the rooted tree;
2. count assignments of weights `1` and `2` to those `d` path edges whose sum is odd.

The tree traversal finds `d`, while a parity symmetry gives the closed form `2^{d-1}`.

**Why the identity of the deepest node does not matter**

Depth counts edges, not their eventual weights. If several nodes have maximum depth `d`, every root-to-one-of-those-nodes path contains exactly `d` edges. The count of valid binary weight assignments depends only on the number of edges, not on the branch labels or structure.

Thus the source does not store a particular deepest node or reconstruct its path. It computes only the maximum root depth.

**Building the tree**

There are `n = len(edges) + 1` nodes labeled from `1` through `n`. The adjacency list has `n + 1` slots so each label can be used directly and index zero can remain unused.

Every undirected edge `[u, v]` is stored in both directions: `v` is appended to `g[u]` and `u` to `g[v]`. This lets the depth-first search move from a node to all of its tree neighbors.

**What dfs returns**

`dfs(i, fa)` returns the largest number of edges on a downward path from node `i` to any descendant when `fa` is treated as its parent.

The local result begins at zero. This is correct for a leaf: it has no child edge, so its longest downward path contains zero edges.

For each neighbor `j` other than the parent, the recursive call returns the longest downward distance starting at `j`. Reaching `j` from `i` uses one additional edge, so the candidate is `dfs(j, i) + 1`. Taking the maximum over all children gives the longest downward distance from `i`.

The call `dfs(1)` uses the default parent value zero. Since zero is not a real node label, no legitimate root neighbor is skipped. Because the graph is guaranteed to be a tree, ignoring the immediate parent is sufficient to prevent revisiting nodes; no other cycle exists.

By induction from the leaves upward, every call returns its claimed subtree height. Therefore `d = dfs(1)` is the maximum depth of the complete tree rooted at node `1`.

**Reducing weighted sums to parity**

Each of the `d` relevant edges independently receives weight `1` or `2`. Weight `2` is even and contributes zero to parity. Weight `1` is odd and flips parity. The total path cost is odd exactly when an odd number of edges receive weight `1`.

There are `2^d` total assignments because each of `d` edges has two choices.

For `d \ge 1`, exactly half have odd total and half have even total. One direct pairing proof is to choose a fixed edge and toggle its weight between `1` and `2`. This operation is reversible and flips the path-sum parity. It pairs every even assignment with exactly one odd assignment, so the two sets have equal size.

Therefore the number of odd-cost assignments is

$$
\frac{2^d}{2} = 2^{d-1}.
$$

The constraint `n \ge 2` guarantees that a valid tree has at least one edge, so `d \ge 1` and the exponent `d - 1` is never negative.

**An equivalent recurrence**

For additional intuition, let `E_t` and `O_t` be the counts of even- and odd-sum assignments for `t` edges. Adding one new edge:

- weight `2` preserves the previous parity;
- weight `1` flips the previous parity.

Hence

$$
E_t = E_{t-1} + O_{t-1},
\qquad
O_t = E_{t-1} + O_{t-1}.
$$

Starting from `E_0 = 1` and `O_0 = 0`, the counts become equal after the first edge and remain equal. For `t \ge 1`, both are `2^{t-1}`. The source uses the resulting formula rather than allocating a DP table.

**Computing the modular power**

`pow(2, d - 1, 10**9 + 7)` performs modular exponentiation directly. It never constructs the enormous exact value `2^{d-1}` before reducing it. Python’s three-argument `pow` uses repeated squaring, so it needs only logarithmically many multiplication steps in the exponent.

The modulo changes only the representation of the final count, not the parity reasoning that produced it.

## Complexity detail

Building the adjacency list takes `O(n)` time and space because a tree has `n - 1` edges and stores two adjacency entries per edge.

The DFS visits every node once and examines every adjacency entry once, so it takes `O(n)` time. Modular exponentiation takes `O(\log d)` time, which is contained in `O(n)`. Overall time is `O(n)`.

The adjacency list uses `O(n)` memory. In the worst case of a chain, the recursive call stack also has depth `O(n)`. Total auxiliary space is `O(n)`.

There is an important implementation limitation: Python’s normal recursion limit is far below the allowed `n = 10^5`. On a sufficiently deep chain, this exact recursive source can raise `RecursionError` even though its mathematical algorithm and asymptotic bounds are correct. An iterative traversal is needed for robust source-level correctness at the maximum depth.

## Alternatives and edge cases

- **Iterative DFS or BFS for depth:** A stack or queue can compute the maximum depth in `O(n)` time and space without risking Python recursion overflow. This is the safer implementation for the published maximum constraint.
- **Dynamic programming for parity counts:** Maintaining even and odd counts for every depth makes the recurrence explicit, but both counts become `2^{t-1}`, so the closed form is simpler and uses no depth-sized table.
- **Binomial summation:** The answer is also the sum of `\binom{d}{r}` over odd `r`. The binomial identity gives `2^{d-1}`, while evaluating the sum directly is unnecessary.
- **Choose and reconstruct a deepest path:** Parent pointers could recover an actual root-to-deepest path, but the assignment count depends only on its edge count. Reconstruction adds storage and work without changing the answer.
- **Several deepest nodes:** Any one may be selected because all corresponding paths have length `d` and therefore the same number of assignments.
- **The smallest valid tree:** With two nodes, `d = 1`. Only weight `1` produces an odd cost, so `2^0 = 1` is correct.
- **Star-shaped tree:** Every non-root node has depth one, again producing one valid assignment regardless of which leaf is selected.
- **Chain-shaped tree:** The mathematical answer remains `2^{n-2}` modulo the modulus, but this shape exposes the recursive source’s depth failure.
- **Ignored branches:** Edges outside the selected root-to-deepest path are not assigned for purposes of this count. Multiplying by choices on those edges would contradict the note.
- **Weight values:** The proof uses only that `1` is odd and `2` is even. If the permitted weights had different parity behavior, the half-of-all-assignments conclusion would need reevaluation.
- **Modulo arithmetic:** The source applies the required modulus during exponentiation, preventing huge intermediate powers.
- **Tree guarantee:** Parent skipping is enough only because the input is an undirected tree. A general cyclic graph would require an explicit visited structure.
