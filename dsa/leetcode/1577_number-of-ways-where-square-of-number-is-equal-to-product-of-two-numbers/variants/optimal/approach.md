## General
**Aggregate every unordered pair product**

For one array, enumerate every index pair `left < right` and store the frequency of `values[left] * values[right]` in a hash table. Repeated products must increase the frequency because they correspond to distinct index pairs.

Build this product-frequency table for both arrays. The table for `nums2` describes every possible paired side of a type-1 triplet, while the table for `nums1` serves type 2.

**Match each squared position against the opposite table**

For every value in `nums1`, look up `value * value` in the pair-product table for `nums2`. Its frequency is exactly the number of choices for `j < k` that combine with that particular `nums1` index. Sum those frequencies, then repeat with the arrays reversed.

Every valid triplet has one singled-out squared index and one unique unordered pair of indices in the other array, so it appears in exactly one lookup contribution. Conversely, a product-frequency match satisfies the required equality and represents that many distinct index pairs. Adding both directions therefore counts every valid triplet once.

## Complexity detail
Enumerating all pairs costs $O(N^2)$ for `nums1` and $O(M^2)$ for `nums2`. The subsequent square lookups take $O(N+M)$ expected time, so the total is $O(N^2+M^2)$.

In the worst case, every pair can produce a distinct hash-table key. The two product maps therefore use $O(N^2+M^2)$ space.

## Alternatives and edge cases
- **Count square frequencies first:** store squared-value counts, then enumerate opposite-array pairs and add matching square frequencies. This has the same time bound and can use only $O(N+M)$ frequency space.
- **Sort with two pointers:** for each squared value, a sorted opposite array can count factor pairs in linear time, but repeating that search for every value can reach cubic time without further aggregation.
- **Enumerate every triplet:** directly test each singled-out index against every opposite pair. It is correct but takes $O(NM^2+MN^2)$ time.
- **Array of length one:** that array supplies no pair, although its sole value may still be the squared side of a triplet.
- **Duplicate values:** equal values at different indices create distinct singles and pairs; frequency multiplication must preserve that multiplicity.
- **Matches in both directions:** type-1 and type-2 counts are independent and must be added.
- **Large values:** products and squares can reach $10^{10}$, so fixed-width implementations need a sufficiently wide integer type.
- **No matching products:** all hash lookups return zero, producing answer zero.
