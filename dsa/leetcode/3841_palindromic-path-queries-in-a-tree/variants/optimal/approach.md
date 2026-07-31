## General

**Reduce every path to letter parity**

Assign bit $0$ to `'a'`, bit $1$ to `'b'`, and so on. XORing the one-bit masks of a collection leaves a set bit exactly for each letter with odd frequency. A path can be rearranged into a palindrome precisely when its resulting mask is zero or has one set bit, which is tested by `mask & (mask - 1) == 0`.

Root the tree at node `0`. For every node $x$, let $P_0(x)$ be the XOR mask on the initial root-to-$x$ path, including both endpoints. If $w=\operatorname{LCA}(u,v)$, then the current path mask satisfies

$$
M(u,v)=P(u)\mathbin{\oplus}P(v)\mathbin{\oplus}\operatorname{bit}(w).
$$

The two root paths contain their shared prefix through $w$ twice, so those letters cancel under XOR. The extra mask for $w$ restores that inclusive endpoint, which otherwise also cancels.

**Turn a node update into one subtree interval**

An iterative depth-first traversal records each node's preorder entry time and exclusive subtree exit time. Every subtree is then one contiguous interval. Changing node $x$ from one letter mask to another produces a difference mask $\Delta$. Exactly the root paths of nodes in $x$'s subtree contain the changed character, so apply $\Delta$ to that complete Euler interval.

A Fenwick tree is used as an XOR difference array: XOR $\Delta$ at the interval's entry and again at its exclusive exit. A prefix query at `entry[y]` now returns the combined differences from every updated ancestor of $y$. Therefore the current root-path mask is the authored computation `initial_root_mask[y] ^ accumulated_at(entry[y])` without touching individual descendants during an update.

**Find the shared path prefix by binary lifting**

The same traversal records each node's parent and depth. Build the binary-lifting table where level $k$ stores the $2^k$-th ancestor. To find an LCA, first lift the deeper endpoint to equal depth, then lift both endpoints from the largest power downward until their parents converge.

For an `update`, apply the subtree difference and replace the node's current one-bit mask. For a `query`, combine the two current root masks with the current mask at the LCA, then perform the one-odd-letter test. The root-mask identity accounts for every inclusive path node exactly once modulo two, and the parity criterion is both necessary and sufficient for a palindromic rearrangement, so each reported boolean is exact after all preceding updates.

## Complexity detail

Let $N$ be the number of nodes and $Q$ the number of operations. Building the tree, Euler data, initial masks, and binary-lifting table takes $O(N\log N)$ time. Each update performs at most two Fenwick modifications in $O(\log N)$ time. Each path query uses binary lifting plus two Fenwick prefix queries, also in $O(\log N)$ time. Total time is $O((N+Q)\log N)$.

The adjacency list and Euler/Fenwick arrays use $O(N)$ space, while the ancestor table uses $O(N\log N)$ space, which dominates the auxiliary bound.

The benchmark defines size as $N+Q$. Each tier is a one-color path with $Q=N$ full-path queries. Root masks plus binary lifting scale near $O((N+Q)\log N)$, while a correct implementation that searches and reconstructs the tree path separately for every query performs $O(NQ)$ work on these inputs.

## Alternatives and edge cases

- **Heavy-light decomposition plus segment tree:** Split each path into $O(\log N)$ heavy-chain intervals and XOR a segment tree over them. This follows the direct path-query model but takes $O(\log^2 N)$ time per query.
- **Lazy segment tree over the Euler tour:** Subtree XOR changes can be range updates and root masks can be point queries in $O(\log N)$, matching the Fenwick asymptotic bound with more machinery.
- **Direct path search:** BFS or DFS can reconstruct the exact path for each query and count its letters, but worst-case paths make the total $O(NQ)$.
- **Static root-prefix masks:** Precomputed masks alone answer a tree with no updates; failing to propagate a changed node to descendant root paths makes later answers stale.
- **Twenty-six frequency counters:** Storing full counts instead of parity masks is correct, but XOR is sufficient because rearrangeability depends only on odd versus even frequencies.
- **Single-node path:** One character always forms a palindrome, including after any update to that node.
- **No-op update:** Assigning a node its current letter has zero difference mask and must leave every later query unchanged.
- **Inclusive LCA:** The lowest common ancestor belongs to the requested path and must be restored once after the two root masks cancel it.
- **Operation order:** Updates produce no output, and every query must observe all earlier updates but none that appear later.
