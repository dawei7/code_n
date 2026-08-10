## General

**The challenge is updating every existing element without visiting every element**

A literal implementation would store the sequence in a list and loop over the whole list for every `addAll` or `multAll` call. With as many as $10^5$ total operations, repeated full-list updates could require quadratic work. The checked-in solution instead stores the values in a dynamic lazy-propagation segment tree. A segment tree groups consecutive positions into intervals, and lazy propagation lets one update an entire covered interval by changing a single node.

The tree's coordinate domain is 1 through 100001. The public API uses zero-based indices, but the implementation stores the first appended value at tree position 1, the second at position 2, and so on. Since there can be at most $10^5$ calls total, there can never be more than $10^5$ appended elements, so this domain is large enough.

`Fancy.n` is the current sequence length. The tree begins conceptually filled with zeros. Nodes are created only when an operation descends into their interval, which avoids eagerly allocating the complete tree.

**What every tree node means**

A `Node` represents the inclusive interval from `node.l` through `node.r`. Its midpoint divides that interval into the left half `[l, mid]` and the right half `[mid + 1, r]`.

The fields have these meanings:

- `v` is the sum of all current sequence values in the node's interval, modulo $M=10^9+7$.
- `mul` and `add` describe a pending affine transformation for the node's children.
- `left` and `right` point to child nodes, which initially do not exist.

An affine transformation has the form

$$
x \longmapsto x\cdot \textit{mul}+\textit{add}.
$$

Initially, `mul = 1` and `add = 0`, the identity transformation. Storing both tags is necessary because multiplication changes a previously pending addition. If an element should first become $x\cdot m_1+a_1$ and a later multiplication by $m_2$ arrives, the combined result is

$$
x\cdot(m_1m_2)+(a_1m_2).
$$

That is why a multiplication update multiplies both the node's `mul` and its `add`.

**Range addition**

`modifyAdd(l, r, inc, node)` adds `inc` to every position in the requested inclusive range. An empty range returns immediately; this makes `addAll` on an empty Fancy sequence safe because it asks to update `[1, 0]`.

When the node is completely inside the requested range, there is no reason to visit its children. If the interval length is `node.r - node.l + 1`, adding `inc` to every element increases the interval sum by that length times `inc`. The source updates `node.v` accordingly modulo $M$ and adds `inc` to the lazy `add` tag.

For partial overlap, `pushdown` first makes the children current, and recursion visits only the halves that can intersect the requested range. `pushup` then restores the parent's sum as the modular sum of its two child sums.

**Range multiplication**

`modifyMul` has the same interval structure. A fully covered node has every value multiplied by `m`, so its stored sum is also multiplied by `m`. The pending transformation changes from

$$
x\cdot\textit{mul}+\textit{add}
$$

to

$$
x\cdot(\textit{mul}\cdot m)+(\textit{add}\cdot m).
$$

Accordingly, the source multiplies `v`, `add`, and `mul` by `m` modulo $M$. This ordering is crucial. Leaving `add` unchanged would make a child eventually receive an addition that had escaped the later multiplication.

**Why pushing lazy operations to children preserves their order**

`pushdown` creates missing children as zero-filled interval nodes. If the parent has a non-identity pending transformation, it applies that transformation to each child's aggregate:

`child.v = child.v * node.mul + child_length * node.add`.

The multiplication scales every existing value. The addition is applied once to every position, hence the factor `child_length`.

The child's own pending transformation must be composed with the parent's newer one. Its tags become:

`child.mul = child.mul * node.mul`

and

`child.add = child.add * node.mul + node.add`.

This is the same affine-composition formula. After both children contain the parent's update, the parent resets its tags to identity. Its `v` remains correct; only responsibility for later propagation has moved downward.

**Mapping each public operation to the tree**

`append(val)` first increments `n` and then adds `val` to the single position `[n, n]`. That location was conceptually zero, so a point addition stores exactly `val`. Importantly, older global operations affected only `[1, old_n]`. The newly appended position did not exist in that range and therefore starts with the supplied value, exactly as the API requires.

`addAll(inc)` updates `[1, n]`. Those are precisely the currently existing elements; unused future positions are excluded.

`multAll(m)` similarly multiplies `[1, n]`, so it changes every existing value and no future value.

`getIndex(idx)` first checks `idx >= n` and returns `-1` for an out-of-range request. Otherwise, it converts the public index to tree position `idx + 1` and performs a one-position range-sum query. The sum of a singleton interval is its value, so the returned result is the requested sequence element modulo $M$.

**Why the complete data structure is correct**

At all times, each materialized node's `v` is the correct modular sum for its interval, including updates retained lazily at that node. Its tags represent, in chronological order, the operations that its descendants have not yet absorbed. Full-cover updates maintain this invariant through the affine formulas. Partial operations call `pushdown` before examining children, so they never use stale descendant values, and `pushup` rebuilds the correct parent sum afterward.

Each public operation targets exactly the occupied position range. Therefore, by induction over API calls, every occupied leaf represents the value obtained by applying exactly those global operations that happened after its append. A singleton query returns that value, while an invalid query returns `-1`. This is the full Fancy contract.

## Complexity detail

Let $U=100001$ be the fixed tree coordinate range, $Q$ the total number of API calls, and $A$ the number of appended elements.

A point update or point query follows one root-to-leaf path and costs $O(\log U)$. A prefix update on `[1,n]` is represented by $O(\log U)$ canonical tree intervals, so `addAll` and `multAll` also take $O(\log U)$ in the worst case. Initialization is $O(1)$. Across all calls, the checked-in implementation therefore takes $O(Q\log U)$ time. Because $U$ is fixed by the problem limit, $\log U$ is a small constant in practice, but it is useful to show it explicitly.

Nodes are allocated lazily along paths and prefix boundaries. A safe bound is $O(A\log U)$ allocated nodes for the positions introduced by appends and the boundaries needed by their updates. Since $U$ itself is fixed, the complete binary interval universe is also bounded by $O(U)$ nodes, and the practical storage grows with the occupied portion of that universe. The recursion stack is $O(\log U)$.

The manifest's aggregate `O(Q\log M)` notation uses $M$ ambiguously. For this exact source, the logarithm comes from the coordinate-domain size $U$, not from modular exponentiation: this implementation never computes a modular inverse. Its storage summary `O(A)` is reasonable when the fixed universe and constant-height paths are suppressed, while $O(A\log U)$ is the conservative explicit bound for dynamic allocation.

## Alternatives and edge cases

- **Single global affine transform with modular inverses:** Store each appended value normalized against a global multiplier and addition, then answer with one affine evaluation. This gives constant-time global updates and queries, while append needs a modular inverse. It is elegant under the given multipliers, but the checked-in source deliberately uses a segment tree and does not rely on invertibility.
- **Store an operation snapshot per append:** One can record the global transform when each value is inserted and reconcile that snapshot at query time. This also uses modular inverses and requires careful algebra about operation order.
- **Update a plain list eagerly:** This is easy to understand, but every `addAll` and `multAll` costs $O(A)$. Alternating appends with global updates can make total work $O(Q^2)$.
- **Use a static full segment-tree array:** Preallocating about four times the maximum coordinate count simplifies child handling but reserves $O(U)$ memory immediately. Dynamic nodes allocate only paths reached by actual operations.
- **Empty sequence global update:** `addAll` and `multAll` call the tree with `l > r` and return without changing future positions. A later append therefore receives no operation that happened before it existed.
- **Index conversion:** The API is zero-based, while the tree is one-based. Querying `idx` instead of `idx + 1` would shift every result and make index 0 miss the first element.
- **Out-of-range index:** The code tests `idx >= n` before entering the tree and returns `-1` exactly as required.
- **Append after earlier global updates:** Only `[1, old_n]` was updated, so the new position is still zero before its point addition. This prevents historical operations from affecting a new value.
- **Multiplication after pending addition:** The lazy `add` tag must also be multiplied. For example, “add 3, then multiply by 2” means $2x+6$, not $2x+3$.
- **Addition after pending multiplication:** Adding `inc` changes only the additive tag, giving $mx+(a+\textit{inc})$. It must not change the multiplier.
- **Modulo arithmetic:** Node sums and composed multiplication tags are reduced modulo $10^9+7$. The public API asks only for modular values, and addition and multiplication are compatible with reducing intermediate results.
- **The extra coordinate 100001:** At most 100000 appends can occur, so that final spare leaf is never required for an element. It does not affect correctness because all public operations stop at `n`.
