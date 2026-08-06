## Function Contract

**Inputs**

- `nums1`: the source integer array.
- `nums2`: an anagram of `nums1`, so it has the same length and the same multiset of values.

**Return value**

- A list `mapping` of the same length as the inputs such that `nums1[i] = nums2[mapping[i]]` for every valid position `i`.

When a value occurs more than once, the contract requires only value equality at the selected position. It does not require different occurrences in `nums1` to use distinct positions in `nums2`, so any matching index is acceptable for each output entry.
