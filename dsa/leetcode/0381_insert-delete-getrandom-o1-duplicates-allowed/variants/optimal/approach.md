## General
**Represent every occurrence in a dense array**

Store one array entry per occurrence. Uniformly selecting an array index then automatically weights a value by its multiplicity. A hash map associates each value with a set of all array indices where its occurrences currently reside.

Insertion appends a new occurrence and adds its index to the value's set. It returns true only when that set did not previously exist or was empty.

**Remove one indexed occurrence by swapping the tail**

Choose and remove any index from the target value's index set. Move the array's final occurrence into that position, then update the moved value's index set: add the replacement index and discard the former final index. Pop the array tail. If the removed value has no indices left, remove its map entry.

When the removed occurrence is already last, no relocation is needed. When the moved value equals the removed value, updating the shared index set in this order still replaces the correct occurrence index.

**Why multiplicities and probabilities stay correct**

Each insertion creates exactly one array cell and one matching index-set entry. Swap deletion removes exactly one occurrence and preserves a matching index for every other cell. Therefore the array length equals total multiset cardinality and contains each value exactly as many times as its index set. Uniform index selection gives each occurrence equal probability and each value probability equal to its count divided by total count.

**Validate random traces by multiset state**

The app validator replays counts, verifies insert/remove Booleans, and accepts any random result with positive current multiplicity. Statistical uniformity comes from the implementation's uniform array-index choice rather than one deterministic case trace.

## Complexity detail
Hash-map and index-set operations, append, tail swap, pop, and random indexing are all average $O(1)$. The array and all index sets together store one entry per occurrence, using $O(n)$ space for total multiset size `n`.

## Alternatives and edge cases
- **Plain list:** naturally represents multiplicity and random weighting, but membership and arbitrary removal require $O(n)$ work.
- **Value-to-count map only:** supports insert/remove but cannot select an occurrence proportionally without scanning counts.
- **Balanced tree of cumulative counts:** supports weighted selection but adds logarithmic complexity.
- Inserting a duplicate returns false but still adds an occurrence.
- Removing a value deletes only one occurrence.
- Removing a missing value returns false.
- Swap deletion must update indices correctly when the moved and removed values are equal.
