## General
**Index one preference list**

Build a hash map from every string in `list1` to its index. Distinct entries make each lookup unambiguous.

**Scan common strings in the second list**

For each string at index `j` in `list2`, use the map to find index `i` when it is common. Compare $i + j$ with the smallest sum seen.

**Replace on improvement and append on ties**

A smaller sum invalidates all previous candidates, so reset the result to the current string. An equal sum adds another valid answer. Larger sums are ignored.

**Why the result is complete and minimal**

Every possible common string is encountered exactly once during the second-list scan, and its exact index sum is computed from the map. The maintained best value is therefore the minimum among all processed common strings. Replacement removes nonminimal candidates, while tie appends preserve every string attaining that minimum; after the full scan, exactly all optimal strings remain.

## Complexity detail
For list lengths `m` and `n`, building the map takes $O(m)$ expected time and scanning the second list takes $O(n)$, for $O(m + n)$ total time. The map stores `m` entries, so extra space is $O(m)$.

## Alternatives and edge cases
- **Index the shorter list:** can reduce auxiliary space while preserving $O(m + n)$ expected time, provided index sums use the correct original positions.
- **Nested scans or repeated `list.index`:** use little extra space but can take $O(mn)$ time.
- **Sort strings with indices:** can find intersections but costs $O((m + n) \log(m + n))$ time.
- **One common string:** it is necessarily the answer.
- **Several tied strings:** return all of them.
- **Common strings with larger sums:** exclude them even if they appear early in one list.
- **Input order:** determines index sums and must not be sorted away before scoring.
- **Output order:** is unrestricted.
