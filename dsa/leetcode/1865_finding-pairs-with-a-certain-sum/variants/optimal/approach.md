## General
**Index the mutable array**

Store both arrays and build a frequency map of the current values in `nums2`.
Construction counts each of its $n_2$ entries once. `nums1` remains unchanged,
so it needs no update machinery.

**Keep frequencies synchronized on updates**

For `add(index, val)`, read the old value at the index and decrement its map
frequency. Increase the stored array element, then increment the new value's
frequency. These two changes preserve the invariant that the map contains
exactly the current multiplicity of every `nums2` value.

**Count complements with multiplicity**

For a query total `tot`, visit every value $x$ in `nums1`. It can pair with
every current occurrence of `tot - x` in `nums2`, so add that complement's
frequency. Iterating array positions rather than distinct values deliberately
counts duplicate `nums1` indices separately. The frequency invariant supplies
the matching `nums2` multiplicity, hence the sum counts every valid $(i,j)$
once and no invalid pair.

## Complexity detail
Construction takes $O(n_2)$ time. Each `add` performs expected $O(1)$ hash-map
work, while each `count` scans $n_1$ values in expected $O(n_1)$ time. Across
$a$ updates and $c$ queries, total time is $O(n_2+a+cn_1)$. The stored arrays
and `nums2` frequency map use $O(n_1+n_2)$ space.

## Alternatives and edge cases
- **Scan both arrays per query:** nested loops require $O(n_1n_2)$ time for
  every `count`.
- **Rebuild frequencies after each update:** queries remain fast, but every
  `add` becomes $O(n_2)$ instead of expected $O(1)$.
- Frequency entries may fall to zero after an update; leaving a zero entry in
  the map does not affect complement counts.
- Duplicate values in either array represent distinct indices and multiply the
  number of pairs.
- Repeated updates to the same index must remove its latest value, not its
  original value.
- A query with no present complement returns zero.
