## General
**Why direct parent links are insufficient for many queries**

The `parent` array answers a one-step query immediately, but following it `k` times costs $O(k)$. With both the tree and query count as large as $5 \cdot 10^4$, a deep chain queried repeatedly would require quadratic total work. Preprocessing longer jumps lets each query skip most intermediate nodes.

**Defining the binary-lifting table**

Let `up[j][v]` denote the ancestor of node `v` exactly $2^j$ edges above it, or `-1` when that ancestor does not exist. Level zero is the supplied parent array because $2^0 = 1$.

For every higher level, split a $2^j$ jump into two consecutive $2^{j-1}$ jumps:

```text
halfway = up[j - 1][v]
up[j][v] = -1 if halfway == -1 else up[j - 1][halfway]
```

By induction on `j`, every stored entry has the stated jump length. Only `n.bit_length()` levels are needed because every legal `k` is at most `n`.

**Decomposing a query into power-of-two jumps**

Every positive integer `k` has a unique binary representation. Scan its set bits from low to high. When bit `j` is set, replace the current node with `up[j][node]`, advancing exactly $2^j$ edges. The sum of those chosen powers is `k`, so if all jumps exist, the final node is exactly the requested ancestor.

If any jump produces `-1`, the path has already moved above the root. No later jump can restore a node, so the query returns `-1` immediately.

**Why combining jumps preserves the answer**

Before processing any bits, the current node is zero edges above the query node. After processing a set of bits, it is the ancestor at a distance equal to the sum of their powers, because each table lookup continues upward from the result of the preceding lookup. After all bits, that accumulated distance is exactly `k`. Together with the table induction, this proves every returned node is correct and every missing ancestor is reported as `-1`.

## Complexity detail
The table has $O(\log n)$ levels and $n$ entries per level, so construction takes $O(n \log n)$ time and space. Each query inspects at most $O(\log n)$ bits and uses constant work per set bit, for $O(\log n)$ time. Across $Q$ queries, total time is $O((n + Q) \log n)$ and stored state is $O(n \log n)$.

## Alternatives and edge cases
- **Walk through direct parents:** Follow `parent[node]` exactly `k` times. It uses only $O(n)$ stored tree data but costs $O(k)$ per query and can become $O(nQ)$ on a chain.
- **Memoize only requested jumps:** Cache ancestors encountered by queries. This may help repeated identical requests but offers no worst-case guarantee when queries cover many nodes and distances.
- **Depth-first traversal with path stacks:** An offline batch of known queries can answer ancestors while traversing the tree, but the required class must support online calls after construction.
- **Euler-tour level-ancestor structures:** More advanced preprocessing can improve constants or theoretical query bounds, but binary lifting is simpler and satisfies the constraints.
- **Querying the root:** Every legal positive `k` returns `-1` for node `0`.
- **Distance equals depth:** The answer is the root.
- **Distance exceeds depth:** Some selected jump reaches `-1`, and the answer is `-1`.
- **Power-of-two distance:** A single table lookup supplies the result.
- **Non-power-of-two distance:** Multiple set bits compose disjoint jump lengths whose sum is exactly `k`.
- **Single-node tree:** The table contains only the root's `-1` parent and every query returns `-1`.
