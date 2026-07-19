## General
**View all pair sums as sorted rows**

For each index `i` in `nums1`, pairing `nums1[i]` with successive values of sorted `nums2` forms a nondecreasing row of sums. The full Cartesian product is therefore a collection of sorted rows, and the task asks for the first `k` values in their merged order.

Only the first `min(k, len(nums1))` rows can matter: before any later row's first pair is needed, there are already at least $k$ row-start pairs with no larger first-array values.

**Merge row fronts with a min-heap**

Seed the heap with pair `(i,0)` from each relevant row, keyed by its sum. Repeatedly remove the smallest heap entry and output its two values. If that row has another column, push `(i,j+1)`. Stop after `k` removals or when the heap is empty.

**Why every popped pair is globally next**

The heap contains the smallest not-yet-output pair from every active row. Any later pair in a row is no smaller than that row's front, so none can precede the minimum heap entry. After popping one front, advancing only its row restores this condition. Induction proves that the heap emits pair sums in global nondecreasing order, including duplicate index pairs with equal values.

**Handle ties as semantic choices**

Several index pairs can share the cutoff sum. Any selection of the required multiplicity at or below that threshold is valid. Validation therefore checks available value-pair multiplicities and the k-th sum threshold rather than enforcing one heap tie order.

## Complexity detail
Let `m = len(nums1)` and $h = \min(k,m)$. Heap initialization uses $O(h)$ entries. At most `k` pop/push steps each cost $O(\log h)$, for $O(k \log \min(k,m))$ time after constant-time array access. The heap uses $O(\min(k,m))$ auxiliary space, while the returned pairs are output space.

## Alternatives and edge cases
- **Generate and sort every pair:** costs $O(mn \log(mn))$ time and $O(mn)$ space even when `k` is small.
- **Binary-search a sum threshold:** can count qualifying pairs efficiently, but reconstructing exactly `k` pairs around ties adds complexity.
- **Seed one heap row per second-array value:** is symmetric and may be preferable when `nums2` is shorter.
- Empty input arrays produce no pairs.
- If `k` exceeds the Cartesian-product size, every index pair is returned.
- Duplicate values represent distinct index combinations and must retain their available multiplicity.
- Negative values and tied sums require no special heap logic.
