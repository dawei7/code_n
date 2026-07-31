## General

**Separate the fixed side from the changing side.** Only `nums2` receives updates. Count each distinct value in `nums1` once and retain its multiplicity. Because `nums1` has at most five elements, a pair-count query needs at most five complement values from the changing array.

**Represent `nums2` by blocks.** Partition its $n$ positions into blocks of size $B=\Theta(\!\sqrt n\!)$. For every block, maintain:

- a lazy increment that logically applies to every position in that block; and
- a frequency map of the stored values before that lazy increment is applied.

Thus, if a block stores base value $v$ and has lazy increment $z$, its current logical value is $v+z$. This representation preserves every duplicate and therefore every index-pair multiplicity.

**Apply a range addition without touching every covered position.** At most two blocks intersect an update only partially. For either boundary block, first add its lazy value into every stored element, reset the lazy value to zero, update the covered positions explicitly, and rebuild that block's frequency map. Every block strictly between the boundaries is fully covered, so increasing only its lazy value is sufficient. The invariant remains true because partial blocks are rebuilt from their current values and full blocks keep the same bases with a uniformly larger offset.

**Count complements through the invariant.** Consider a type-2 target `tot`, a fixed value $a$ occurring $f_a$ times in `nums1`, and a block with lazy value $z$. A base value in that block forms the requested sum exactly when

$$
v = \texttt{tot}-a-z.
$$

The block frequency map returns how many positions contain that base value. Multiplying by $f_a$ counts all index pairs contributed by the repeated value $a$. Summing this quantity over every fixed value and every block counts each valid pair once and no invalid pair. Processing queries in order maintains the block invariant after every update, so every emitted count reflects precisely the current `nums2`.

## Complexity detail

Let $n=\lvert\texttt{nums2}\rvert$, let $q=\lvert\texttt{queries}\rvert$, let $D$ be the number of distinct values in `nums1`, and let $B$ be the block size. Here $D\le5$.

Building the fixed-value map and all block maps takes $O(n)$ time. A range addition rebuilds at most two boundary blocks in $O(B)$ time and changes at most $O(n/B)$ lazy values, for $O(B+n/B)$ time. A pair-count query performs $D$ lookups in each of $O(n/B)$ blocks, for $O(Dn/B)$ time. Choosing $B=\Theta(\sqrt n)$ makes either query type $O(\sqrt n)$ because $D$ is bounded by five, and the complete query sequence takes $O(n+q\sqrt n)$ time.

The stored array, block frequency maps, lazy values, and fixed frequencies occupy $O(n)$ auxiliary space in total. The returned answer array is output space.

For scaling evidence, each benchmark uses $n$ distinct elements in `nums2` and $n$ alternating full-range updates and pair-count queries. The three tiers use $n=32$, $128$, and $512$. Square-root decomposition takes $\Theta(n\sqrt n)$ time on this workload, whereas scanning every current value for each count request takes $\Theta(n^2)$.

## Alternatives and edge cases

- **Direct simulation:** Updating every covered element and scanning all of `nums2` for every count request is straightforward and exact, but it costs $O(nq)$ in the worst case.
- **Rebuild one global frequency map after updates:** A range addition can change many different values, so rebuilding or adjusting the complete map still requires linear work per update.
- **Ignore duplicate values in `nums1`:** This undercounts pairs. The fixed frequency must multiply every matching `nums2` position by the number of indices carrying that value in `nums1`.
- **Update wholly covered blocks element by element:** This discards the main benefit of decomposition; a single lazy increment represents the same logical change.
- **Partial update after an earlier lazy update:** Push the block's existing lazy value before changing individual positions, or its rebuilt frequency map will mix incompatible base values.
- **No type-2 queries:** The correct returned array is empty even though all type-1 updates must still be processed safely.
- **Targets with no complement:** Missing frequency-map entries contribute zero without requiring a special case.
