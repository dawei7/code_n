## General

**A 26-bit mask contains all palindrome information**

The order of path characters does not matter because the path string may be rearranged. Only the parity—odd or even—of each letter frequency matters.

Represent letter `c` by one bit:

`1 << (ord(c) - ord("a"))`.

XOR combines these masks. A bit is 1 in the result exactly when that letter appeared an odd number of times, because two equal bits cancel:

$$
1\mathbin{\mathrm{xor}}1=0.
$$

A multiset can form a palindrome when at most one frequency is odd. A mask has at most one set bit exactly when:

`mask & (mask - 1) == 0`.

For mask zero, the condition is also true, representing all-even counts. For a one-bit mask, subtracting one clears that bit and fills only lower positions, so the AND is zero. A mask with two or more set bits retains at least one bit after the operation.

The source stores each node's current one-letter mask in `node_mask`.

**Root the tree and record static structural information**

The tree is rooted at node 0. The source performs iterative DFS rather than recursion, which is important for a possible 50,000-node chain.

Each stack entry contains `(node, previous, leaving)`. On the first visit:

- `parent[node]` records the parent;
- `depth[node]` is one more than the parent's depth;
- `entry[node]` receives the current Euler timer;
- `initial_root_mask[node]` becomes the XOR of initial letters from root through this node.

The timer increments only when entering a node. The source then pushes a leaving marker and pushes all children.

When the leaving marker is popped, `exit_time[node]` receives the current timer. By then, every node in this subtree has been entered and no outside node was entered between them.

Therefore the subtree of `node` corresponds exactly to the half-open Euler interval:

$$
[\texttt{entry[node]},\texttt{exit_time[node]}).
$$

This interval is the bridge between a node update and every root path affected by that update.

**Initial root masks make a static path query easy**

Let `R(v)` be the XOR mask on the inclusive root-to-`v` path. Initially, this is `initial_root_mask[v]`.

For two nodes `u` and `v` with lowest common ancestor `w`:

$$
R(u)\mathbin{\mathrm{xor}}R(v)
$$

cancels every node on the shared root-to-`w` prefix, including `w` itself. The remaining bits represent both branches below `w`. XORing `node_mask[w]` once adds the LCA character back.

Thus the inclusive path mask is:

$$
R(u)\mathbin{\mathrm{xor}}R(v)\mathbin{\mathrm{xor}}\operatorname{mask}(w).
$$

Updates make `R` dynamic, but the same formula remains valid.

**Build binary-lifting ancestors for each LCA**

`ancestors[0][v]` is `parent[v]`. Each later row doubles the jump:

$$
\texttt{ancestors}[p][v]
=
\text{the }2^p\text{-th ancestor of }v.
$$

The recurrence looks up the $2^{p-1}$ ancestor twice. The table has `n.bit_length()` levels, enough to jump through any possible depth.

To compute an LCA, the helper first lifts the deeper node until both depths match. It reads the bits of the depth difference and applies the corresponding power-of-two jumps.

If the nodes then coincide, that node is the LCA.

Otherwise, it examines ancestor levels from largest to smallest. Whenever the two lifted ancestors differ, both nodes jump upward by that amount. At the end, the nodes are distinct children of their LCA, so `parent[first]` is returned.

Each LCA takes $O(\log N)$ time.

**Understand how changing one node affects root paths**

Suppose node `u` changes from old letter mask `old` to new mask `new`. The parity change is:

`difference = old ^ new`.

Every root-to-node path ending inside `u`'s subtree contains `u` and must XOR this difference. Every root path ending outside that subtree does not contain `u` and remains unchanged.

The update is therefore a range XOR over `u`'s Euler subtree interval.

If old and new letters are identical, `difference` is zero and no structure needs modification.

The source also replaces `node_mask[u]` with the new one because a future query may use `u` itself as the LCA.

**Use a Fenwick difference structure for range XOR and point query**

`difference_tree` is a Fenwick tree whose combine operation is XOR rather than addition.

To apply XOR mask `d` to every Euler position in half-open interval `[l,r)`, a difference-array view toggles:

- `d` at `l`;
- `d` again at `r`.

The prefix XOR at a position inside the interval sees the first toggle but not the second. At or after `r`, both toggles cancel.

`apply_from(index, mask)` performs a Fenwick point update. The source calls it at `entry[node]` and, when the interval does not end at `n`, at `exit_time[node]`.

`accumulated_at(index)` computes the Fenwick prefix XOR. At `entry[v]`, it returns the combined differences from every earlier update whose subtree contains `v`.

The current root-path mask is therefore:

`initial_root_mask[v] ^ accumulated_at(entry[v])`.

The initial mask never needs to be rewritten for every descendant. Updates are layered over it through Euler intervals.

**Assemble a dynamic path mask**

For a query between `first` and `second`:

1. find their current structural LCA, `ancestor`;
2. obtain each current root mask by XORing its initial mask with its Fenwick accumulated difference;
3. XOR the two root masks;
4. XOR `node_mask[ancestor]` to include the LCA exactly once.

The source expression is:

`initial_root_mask[first] ^ accumulated_at(entry[first]) ^ initial_root_mask[second] ^ accumulated_at(entry[second]) ^ node_mask[ancestor]`.

Tree structure never changes, so parent, depth, Euler, and ancestor tables remain valid across all character updates.

The resulting mask is tested for at most one set bit, and one Boolean is appended only for a `query` operation. Updates produce no output.

**Trace an update on a chain**

For chain `0 - 1 - 2` with letters `"aac"`, the initial root mask at node 2 represents two `a` characters canceling and one `c` remaining. The query from 0 to 2 has one odd letter and returns true.

Updating node 1 from `a` to `b` creates difference mask `a XOR b`. The subtree of node 1 contains nodes 1 and 2, so their dynamic root masks receive that difference; node 0's does not.

The next path mask contains one each of `a`, `b`, and `c`, giving three set bits and false.

**Why interval updates and the query formula stay synchronized**

Initially, every `initial_root_mask[v]` is exact. For an update at `u`, precisely the root paths of descendants contain `u`. Euler range XOR applies exactly the old-to-new difference to those descendants and no others. Thus the reconstructed current root mask remains exact after every update.

For a query, XORing the two exact root masks cancels their common prefix. Adding the current LCA letter restores the one path node canceled twice. The final 26-bit mask therefore equals the parity multiset of the unique inclusive path.

The final bit test is exactly the palindrome-rearrangement criterion, so every returned Boolean matches the current tree state.

## Complexity detail

Building the adjacency list and iterative Euler traversal takes $O(N)$ time and space. The binary-lifting table has $O(N\log N)$ entries and takes $O(N\log N)$ preprocessing time.

An update performs at most two Fenwick point updates, each $O(\log N)$. A path query performs one $O(\log N)$ LCA plus two $O(\log N)$ Fenwick prefix queries and constant mask arithmetic. For $Q$ commands, total time is $O((N+Q)\log N)$.

The ancestor table dominates space at $O(N\log N)$. Adjacency, Euler arrays, masks, Fenwick storage, and DFS stack are each $O(N)$. The answer list contains one Boolean per path query.

## Alternatives and edge cases

- **Heavy-light decomposition:** Split each path into logarithmically many chains and use a segment tree of XOR masks. It supports the same operations in roughly $O(\log^2 N)$ per query and is more general, but the root-mask subtree-update transformation is simpler here.
- **Recompute each path explicitly:** Finding and scanning all path nodes per query can cost $O(NQ)$ on a chain.
- **Segment tree over Euler differences:** It can replace the Fenwick tree for range XOR and point query, but Fenwick operations are smaller and sufficient.
- **Update to the same letter:** The difference mask is zero, so the source correctly skips both range updates.
- **Query a node with itself:** The path contains one character, the LCA is that node, and the result is always true.
- **Root update:** Its subtree interval is `[0,n)`. Only the entry toggle is needed because there is no in-range endpoint at `n`.
- **Zero parity mask:** All letter counts are even, so it is palindrome-compatible; the bit test accepts zero.
- **One-node tree:** Euler, ancestor, Fenwick, update, and LCA logic all remain valid.
- **Deep chain:** Iterative DFS avoids Python recursion overflow; LCA and Fenwick operations stay logarithmic.
- **Repeated updates to one node:** Each difference is based on the current `node_mask`, so changes compose correctly by XOR.
- **LCA character after updates:** The source uses current `node_mask[ancestor]`, not its initial character, which is necessary after an LCA-node update.
- **Operation parsing:** Results preserve chronological query order, while update commands append nothing.
