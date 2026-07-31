## General

**Reduce type 2 to a count of ones.** Let `total` be the current sum of `nums2`. A type-2 query adds `p` exactly at the positions where `nums1[i]` is one, so its entire effect on the requested aggregate is

$$
\texttt{total} \mathrel{+}= p \cdot \#\{i : \texttt{nums1[i]} = 1\}.
$$

No later operation examines an individual value of `nums2`; type 1 changes only `nums1`, and type 3 requests only the total. It is therefore unnecessary to materialize any type-2 update in `nums2`. The remaining dynamic task is to maintain the global number of ones while inclusive ranges of `nums1` are flipped.

**Store one counts in a lazy segment tree.** Each tree node represents a contiguous segment and stores its current number of one bits. Flipping a segment of length $L$ changes its count from $c$ to $L-c$. A Boolean lazy marker records that the entire represented segment has been inverted but that this inversion has not yet been passed to its children. Applying another full flip toggles the marker, so two pending flips correctly cancel.

For a type-1 query, a fully covered node is updated immediately with `length - count` and its marker is toggled. A partially covered node first pushes any pending flip into both children, recursively updates the intersecting children, and recomputes its count from their sum. At all times the root therefore stores the exact current number of ones. Type 2 multiplies that root count by `p`, while type 3 appends `total` to the output.

## Complexity detail

Let $n$ be the array length and $q$ the number of queries. Building the tree and computing the initial `nums2` sum take $O(n)$ time. A range flip visits $O(\log n)$ canonical tree nodes with lazy propagation, while type-2 and type-3 queries take $O(1)$ time. Thus the worst-case total is $O(n + q \log n)$. The tree, lazy markers, and recursion use $O(n)$ space.

## Alternatives and edge cases

- **Flip the array directly:** Updating every index in `[l, r]` and recounting ones is straightforward but can require $O(n)$ work per query and $O(nq)$ overall.
- **Fenwick tree:** A Fenwick tree supports point changes and prefix sums, but it cannot complement an arbitrary range and update its one count without touching the covered positions.
- **Materialize `nums2`:** Applying every type-2 update element by element is unnecessary because later queries observe only its total.
- **Repeated flips:** Two flips over the same segment restore its previous state; toggling the lazy marker models this parity exactly.
- **Single-element ranges:** A leaf count changes between zero and one, and no child propagation is needed.
- **Zero multiplier:** A type-2 query with `p = 0` leaves `total` unchanged regardless of the current bit count.
- **Large totals:** Repeated additions can exceed 32-bit range, so fixed-width implementations need a 64-bit aggregate.
