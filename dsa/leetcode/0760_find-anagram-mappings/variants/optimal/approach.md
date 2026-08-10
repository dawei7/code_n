## General

**Map each value to any valid index in the second array**

The output requires `nums1[i] == nums2[mapping[i]]` for every position. Since `nums2` is an anagram of `nums1`, every source value occurs at least once in the second array.

The local contract permits any matching index for each output entry and does not require different duplicate occurrences to consume different indices. This lets one dictionary entry per value solve the problem.

**Build the value-to-index dictionary**

The comprehension

`d = {x: i for i, x in enumerate(nums2)}`

visits `nums2` from left to right. For a value seen once, it stores that position. If the value appears again, the later assignment overwrites the earlier one, so the final dictionary contains the last occurrence index.

Choosing the last occurrence is not required; it is simply the deterministic result of the comprehension. Any stored occurrence has the correct value.

**Construct the mapping**

For every value `x` in `nums1`, the result appends `d[x]`. By dictionary construction, `nums2[d[x]] == x`, so each output position satisfies the required equality.

The anagram guarantee ensures `x` is always a key. No missing-value branch or default is necessary.

**Handling duplicates**

Suppose both arrays contain value seven several times. The dictionary retains one of `nums2`’s seven indices, and every seven in `nums1` may map to that same index under the stated contract.

If a stricter variant required a one-to-one correspondence between occurrences, the algorithm would instead store a stack or queue of all indices per value and remove one for each source occurrence. That is a different requirement from the package’s function contract.

For example, `nums1 = [4, 4]` and `nums2 = [4, 4]` produce dictionary entry `4 -> 1` and mapping `[1, 1]`. Both entries point to a location containing four, so both required equalities hold under this contract.

**Trace a simple example**

For `nums2 = [50, 12, 32, 46, 28]`, the dictionary maps 50 to zero, 12 to one, 32 to two, 46 to three, and 28 to four.

Reading `nums1 = [12, 28, 46, 32, 50]` then returns `[1, 4, 3, 2, 0]`. Looking up each result index in `nums2` reconstructs the corresponding `nums1` value.

**Why array order otherwise does not matter**

An anagram preserves the multiset of values but may arbitrarily reorder positions. The dictionary discards `nums2`’s sequential structure except for the stored index because equality, not neighborhood or relative order, is the only mapping condition.

**The output length is automatically correct**

The list comprehension iterates once for every element of `nums1`, including duplicates. It therefore emits exactly `n` indices in source order. Each lookup corresponds to the value at that same source position, so the mapping does not need a separate index counter or postprocessing step.

**Why the method is correct**

For every distinct value `x` in `nums2`, `d[x]` is assigned an index at which that value occurs. The anagram guarantee says every `nums1[i]` is among those keys.

Therefore each produced `mapping[i] = d[nums1[i]]` is a valid index and points to an equal value. The returned list has one entry per source element, so it is a complete valid mapping.

**Why no sorting is needed**

Sorting value-index pairs could match occurrences, but it would cost `O(n log n)` and obscure the original indices. Hash lookup directly connects equal values while preserving the needed destination positions.

The solution also avoids allocating an array indexed by value. Although values are bounded, a hash map stores only values that actually occur and remains efficient if the numeric range is sparse.

## Complexity detail

Let `n` be the common array length. Building the dictionary visits `nums2` once in expected `O(n)` time. Constructing the output visits `nums1` once with expected constant-time lookups, also `O(n)`. Total expected time is `O(n)`.

The dictionary stores at most `n` distinct keys, so auxiliary space is `O(n)` in the worst case. The returned mapping also contains `n` integers as required output.

## Alternatives and edge cases

- **Store all indices per value:** Use a dictionary of lists and pop an index for every source occurrence. This supports a stricter one-to-one occurrence mapping with the same asymptotic bounds.

- **Nested search:** Scan `nums2` for every source value. It uses little extra storage but costs `O(n^2)`.

- **Sort both arrays with original indices:** This can pair duplicates uniquely but costs `O(n log n)` time.

- **Duplicate values:** The exact code reuses the last matching index, which is valid under the local contract.

- **Identical arrays:** Every value maps to an occurrence of itself; unique values map to their original positions.

- **Single element:** The dictionary maps the sole value to zero and returns `[0]`.

- **Missing key:** Impossible under the anagram guarantee, so no defensive fallback is needed.

- **Large integer values:** Dictionary storage depends on count, not the numeric range up to `10^5`.
