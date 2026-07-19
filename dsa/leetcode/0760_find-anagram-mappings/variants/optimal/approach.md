## General
**Reverse the lookup direction**

The required output asks where each `nums1` value occurs in `nums2`. Build a hash table from every value in `nums2` to one of its indices. Then scan `nums1` and replace each value with its stored index.

**Why one stored index is enough**

For a value appearing multiple times, the contract accepts any matching occurrence; it does not require a unique assignment of occurrences. Overwriting an earlier index while building the table is therefore safe. For every output position `i`, the lookup was created from an actual position in `nums2` holding `nums1[i]`, so the returned mapping satisfies `nums1[i] = nums2[mapping[i]]`. Because the arrays are anagrams, every lookup is guaranteed to exist.

## Complexity detail
Building the table and producing the mapping each take $O(n)$ expected time. The table and returned list each use $O(n)$ space in the worst case.

## Alternatives and edge cases
- **Linear search for every source value:** Calling `nums2.index(value)` is simple and correct but can take $O(n^2)$ time.
- **Value-to-stack of indices:** Keeping every occurrence and popping indices creates a one-to-one occurrence assignment in $O(n)$ time, but that stronger property is unnecessary here.
- **Sort indexed pairs:** Sorting both arrays with original indices can construct a mapping in $O(n \log n)$ time and avoids hashing.
- **Duplicate values:** Reusing any index containing the requested value is valid.
- **Negative or large integers:** Hash-table keys handle them without requiring a bounded-value array.
- **Single-element arrays:** The only valid mapping is `[0]`.
