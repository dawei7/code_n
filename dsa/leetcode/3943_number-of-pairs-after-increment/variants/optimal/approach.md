## General

The difficulty comes from combining two different query types:

- a range addition changes many values in `nums2`;
- a pair-count query needs frequencies of the current values in `nums2`.

Updating every affected element is slow for a long range, while rebuilding a complete frequency map after every update is also slow. The source uses square-root decomposition: it divides `nums2` into blocks, stores a frequency counter for the materialized values in each block, and attaches one lazy addition to each whole block.

The unusually small `nums1` is equally important. It contains at most five positions, so a pair query can iterate its distinct values for every block.

**Compress the fixed array by frequency**

`nums1` never changes. The source builds `fixed_frequencies = Counter(nums1)` and converts its entries to `fixed_items`.

If value $a$ occurs $c_a$ times in `nums1` and a current value $b$ occurs $c_b$ times in `nums2`, then they form $c_ac_b$ index pairs. Storing multiplicities preserves index counting while avoiding repeated work for equal fixed values.

Let $D$ be the number of distinct values in `nums1`. The constraints give $D\le5$.

**Choose and initialize the blocks**

For `length = len(nums2)`, the source selects a block size close to

$$
\sqrt{\frac{\texttt{length}\cdot D}{2}}.
$$

The exact integer expression uses `isqrt` and adds one so the size is positive and rounded safely. This choice balances the cost of rebuilding up to two boundary blocks against the cost of visiting all blocks and all $D$ fixed values during a count query.

`block_frequencies[b]` is a `Counter` of the values physically stored in block $b$. `lazy[b]` is an addition that logically applies to every value in that block but has not necessarily been written into `nums2`.

Thus, if the counter stores a base value $v$, its current logical value is

$$
v+\texttt{lazy[b]}.
$$

Initially every lazy value is zero, so counters can be built directly from slices of `nums2`.

**Materialize a boundary block before changing part of it**

A range update may cover only part of its first or last block. A single lazy offset cannot describe a change to only some positions, so `update_boundary` first pushes the block's old lazy value into every physical element.

It finds the full block bounds, reads `offset = lazy[block]`, adds that offset to all physical entries when nonzero, and resets the lazy value to zero. Now `nums2` again contains the true current values throughout that block.

The helper then adds `delta` only to the requested inclusive indices `left` through `right` and rebuilds the block's frequency counter from its complete physical slice.

Rebuilding the whole boundary counter is necessary: changing individual positions can remove occurrences of old values and add occurrences of new values. With only about one block's worth of entries, reconstruction is inexpensive.

**Apply a range update**

If both endpoints lie in the same block, the source calls `update_boundary` once for exactly that interval.

Otherwise, the range is separated into:

1. the suffix of the left endpoint's block;
2. every whole block strictly between the endpoint blocks;
3. the prefix of the right endpoint's block.

The two partial pieces are materialized and rebuilt. Every middle block is covered completely, so the source merely performs `lazy[block] += delta`. Its physical values and counter remain unchanged; the offset records the logical update in constant time for that block.

This representation may leave `nums2` only partially materialized after the method returns. Boundary blocks have physical updates, while untouched whole blocks may retain pending lazy offsets. That hybrid state is internally consistent for queries, although callers should not expect the original list object to visibly contain every logical update.

**Count pairs without pushing lazy values**

For a type-2 target $T$, consider one block with lazy offset $\ell$. A stored physical value $b$ currently represents $b+\ell$. Paired with fixed value $a$, it satisfies

$$
a+(b+\ell)=T
$$

exactly when

$$
b=T-\ell-a.
$$

The source first sets `adjusted_target = target - lazy[block]`. For every fixed pair `(value, multiplicity)`, it asks the block counter for

`adjusted_target - value`.

That counter lookup returns how many `nums2` indices in the block have the required physical value. Multiplying by the frequency in `nums1` gives all index pairs for this value and block. Summing over all fixed values and blocks counts every valid pair exactly once.

There is no need to materialize a lazy block just to answer a query. Subtracting its common offset from the target is algebraically equivalent and leaves the data structure ready for later operations.

**Why updates and counts stay synchronized**

For each block, maintain this invariant:

- its counter describes the values physically stored in its slice of `nums2`;
- adding its lazy offset to those physical values gives the true array state after all processed queries.

A full-block update changes only the second component. A partial update first merges the components, changes physical values, and rebuilds the counter. Both preserve the invariant.

The pair formula reads exactly that logical state. Since queries are processed from left to right, each answer includes every preceding update and no later one.

## Complexity detail

Let $N=\lvert\texttt{nums2}\rvert$, let $D$ be the number of distinct `nums1` values, and let $B$ be the chosen block size.

Initialization takes $O(N)$ time and $O(N)$ counter storage in the worst case.

A range update rebuilds at most two blocks for $O(B)$ work and increments lazy values across at most $O(N/B)$ complete blocks. Its time is $O(B+N/B)$.

A pair query visits $O(N/B)$ blocks and $D$ fixed values per block, costing $O(DN/B)$ expected time with hash-counter lookups.

The chosen $B$ is on the order of $\sqrt{ND}$ and balances the dominant terms. Since $D\le5$ is a fixed constraint, every query costs $O(\sqrt N)$ up to constants, and total time is $O(N+Q\sqrt N)$ for $Q$ queries, matching the manifest.

Counters collectively hold at most $N$ distinct-entry occurrences across blocks, and lazy storage is $O(N/B)$. Auxiliary data-structure space is $O(N)$. The returned answer can contain $O(Q)$ integers; if output storage is included, total additional space is $O(N+Q)$.

## Alternatives and edge cases

- **Update every element in the range:** This makes type-1 queries $O(N)$ in the worst case. Lazy whole blocks avoid touching their entries.
- **Use one global frequency counter:** A range addition affects an arbitrary subset, so updating the global frequencies still requires knowing every changed old value. Per-block counters localize reconstruction.
- **Push all lazy blocks before every count query:** This restores a literal array but wastes $O(N)$ work. Adjusting the target gives the same counts without materialization.
- **Iterate every `nums1` position instead of distinct values:** It remains bounded by five but repeats identical counter lookups. Multiplicity compression is cleaner and counts index pairs correctly.
- **Same-block range:** Only one boundary rebuild is performed, avoiding double application where left and right endpoint blocks coincide.
- **Range aligned to block boundaries:** Endpoint helpers still work; interior whole blocks receive only lazy increments.
- **Repeated values in either array:** Frequency multiplication counts every index pair, not merely distinct-value combinations.
- **Target smaller than current values:** Counter lookups for negative or absent required physical values return zero naturally.
- **Many accumulated full-block updates:** Lazy values add together. A later boundary update pushes their total exactly once before rebuilding.
- **Partially materialized output list:** The internal answers are correct, but `nums2` itself may not display pending lazy additions in whole blocks after return.
- **One-element `nums2`:** There is one block. Every update is a boundary update and every count query uses its one counter.
- **Large update totals:** Python integers safely hold values after many positive range additions.
- **No type-2 queries:** The returned answer is empty even though type-1 updates are still processed.
