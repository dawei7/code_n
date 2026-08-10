## General

**Only two aggregate facts are needed**

Type 1 queries change a range of bits in `nums1`. Type 2 queries appear to update every element of `nums2`, but the requested type 3 result is only the total sum.

For a type 2 query with multiplier $p$,

$$
\sum_i\bigl(\texttt{nums2[i]}+p\cdot\texttt{nums1[i]}\bigr)
=
\sum_i\texttt{nums2[i]}
+p\sum_i\texttt{nums1[i]}.
$$

Because `nums1` is binary, its sum is exactly its number of ones. Therefore, the algorithm never needs to update `nums2` element by element. It maintains:

- `s`, the current total sum of `nums2`;
- the current number of ones in `nums1`.

The hard operation is flipping a whole range while keeping the one count current. A lazy segment tree supports that in logarithmic time.

**What each tree node stores**

A node represents an inclusive one-based interval `[l, r]`. Its field `s` is the number of ones in that interval. For a leaf, `s` is the corresponding input bit. For an internal node,

`node.s = left_child.s + right_child.s`.

The tree converts the zero-based input array to one-based tree coordinates during building: leaf position $l$ reads `nums[l - 1]`.

The tree list has about four nodes per input element, a conventional safe capacity for recursive segment-tree layouts.

**Flipping an entire represented interval**

Suppose a node covers a segment of length

$$
L=r-l+1
$$

and currently contains $c$ ones. It contains $L-c$ zeros. Flipping every bit turns those zeros into ones and the old ones into zeros, so the new one count is

$$
L-c.
$$

When a type 1 range fully covers a node, `modify` can update its count with this formula without visiting its descendants.

The field `lazy` records whether the descendants still need to receive a pending flip. Flipping twice restores the original bits, so only the parity of pending flips matters. The operation `lazy ^= 1` toggles between “no pending flip” and “one pending flip.”

**Push pending work down only when necessary**

If a later operation must inspect only part of a lazily flipped node, `pushdown` transfers the flip to both children. It replaces each child's one count by child length minus old count and toggles each child's lazy bit.

The parent lazy bit is then toggled back to zero. The code writes `self.tr[u].lazy ^= 1` because `pushdown` runs only when that value is currently one.

Child lengths are calculated from the parent's midpoint. The left interval has length `mid - parent.l + 1`, while the right interval has length `parent.r - mid`.

After recursively modifying relevant children, `pushup` recomputes the parent's total from them. These rules keep every stored count consistent even though most individual leaves are not immediately changed.

**Process the three query types**

For type 1 `[1,l,r]`, the solution calls

`tree.modify(1, l + 1, r + 1)`.

Adding one converts the query's zero-based inclusive range to the tree's one-based inclusive coordinates. Recursive modification descends only into nodes intersecting a partially covered boundary; fully covered middle nodes receive lazy flips.

For type 2 `[2,p,0]`, the solution obtains the number of current ones with a full-range tree query and adds

`p * ones`

to `s`. The physical `nums2` array remains unchanged, but `s` represents exactly what its total would be after all conceptual element updates.

For type 3, the current `s` is appended to `ans`. Answers naturally appear in query order.

**Why the maintained state is correct**

After building, every node count equals the number of ones in its segment, and `s = sum(nums2)`. A type 1 query applies the mathematical complement count to a disjoint cover of its range; lazy propagation preserves the same result as flipping every affected leaf. It changes no `nums2` total.

A type 2 query adds $p$ once for each current one and zero for each current zero. Multiplying $p$ by the root's one count is therefore exactly the aggregate sum increase. A type 3 query merely reports that already-correct total.

By induction over the query sequence, both maintained facts remain equal to the conceptual arrays after every operation.

The implemented full-range `query(1,1,n)` returns immediately at the root because the root is fully covered. It could read the root's `s` field directly, but using the general query method is still constant time for this range.

## Complexity detail

Let $n$ be the array length and $q$ the number of queries. Building the tree visits $O(n)$ nodes. A range flip touches $O(\log n)$ boundary paths and a logarithmic-size canonical cover in the usual lazy segment-tree analysis, so it costs $O(\log n)$. The exact type 2 full-range query returns at the root in $O(1)$, and type 3 is $O(1)$.

Thus a precise bound is $O(n+q_1\log n+q_2+q_3)$, which is within the manifest's worst-case $O(n+q\log n)$. The tree allocates $O(n)$ nodes and recursion uses $O(\log n)$ stack depth. The answer uses output-proportional space.

## Alternatives and edge cases

- **Flip every element directly:** Range updates can cost $O(n)$ each, leading to $O(nq)$ time.
- **Fenwick tree:** A standard Fenwick tree handles point updates and range sums well, but range bit complementation is not a simple additive update without more structure.
- **Store actual `nums2` values:** Type 2 would update many elements even though only the total is ever queried. Maintaining `s` avoids that work.
- **Read the root directly:** Since type 2 always needs the whole-array one count, `tree.tr[1].s` would replace the general full-range query.
- **Flip the same range twice:** Lazy flags XOR twice to zero, and count complementation twice restores the original state.
- **Single-element range:** Recursion reaches one leaf, whose count changes from zero to one or one to zero.
- **Multiplier zero:** Type 2 adds zero regardless of the current one count, leaving `s` unchanged.
- **No type 3 queries:** The returned answer list is empty, while updates are still processed correctly.
- **Index conversion:** Both inclusive endpoints receive plus one; forgetting either conversion would update the wrong tree positions.
- **Large totals:** Repeated multipliers can produce sums beyond 32-bit range, so fixed-width implementations need 64-bit accumulation.
