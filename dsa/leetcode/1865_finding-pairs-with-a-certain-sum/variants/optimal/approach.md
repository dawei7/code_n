## General

**Exploit the large difference in array sizes.** `nums1` has at most 1,000 elements, while `nums2` may have 100,000. A count query can afford to scan `nums1`, but repeatedly scanning `nums2` would be much more expensive. The class therefore maintains a frequency counter for current `nums2` values.

`self.cnt = Counter(nums2)` maps each value to the number of indices holding it. The class also retains references to both input lists because additions must modify an exact `nums2` index and counts must read every current `nums1` occurrence.

**Update the frequency map around an addition.** Before changing `nums2[index]`, the old value contributes one occurrence to its counter bucket. The method decrements that bucket, mutates the list element with `+= val`, then increments the new value’s bucket.

This order preserves the invariant that `cnt[v]` equals the number of current `nums2` indices containing `v` after every completed operation.

The exact code does not remove a key when its frequency becomes zero. Zero-count historical values may remain in the `Counter`. They do not affect pair counts because reading them contributes zero, but repeated additions can gradually increase the number of stored keys.

**Count complements rather than pairs explicitly.** For one `nums1` value `x`, a pair sum equals `tot` exactly when the second value is `tot - x`. `self.cnt[tot - x]` is the number of valid `j` indices for that particular `i`.

The generator repeats this lookup for every occurrence in `nums1` and sums the results. If `x` appears several times, each index is intentionally processed separately, multiplying the complement frequency by the number of first-array occurrences. This counts ordered index pairs rather than only distinct value combinations.

`Counter` returns zero for a missing key, so the count method needs no membership test. Missing lookups through `Counter.__missing__` do not create stored keys.

**Trace a frequency update.** If `nums2[index]` changes from two to four, the count of two drops by one and the count of four rises by one. A later query for total seven will stop counting that index as a complement to five and start counting it as a complement to three.

**State invariant and correctness.** Immediately after construction, `cnt` is the exact frequency distribution of `nums2`. An addition removes one occurrence from the old value and adds one at the new value, preserving the invariant.

During `count(tot)`, for each first index `i`, the counter lookup returns exactly the number of second indices `j` satisfying the equation. These sets of pairs are disjoint across different `i` values as indices, even when values repeat. Summing them therefore gives all and only valid pairs.

**Mutation and aliasing behavior.** The constructor stores the original list objects rather than copies. `add` visibly mutates the caller’s `nums2`. The class never mutates `nums1` itself, but external changes to either retained list could violate the counter invariant; the intended object API assumes the arrays are managed through the class.

**Why not counter both arrays.** A second counter could let `count` iterate distinct values instead of all `nums1` entries. That is valid, but the exact source uses the small array directly. It naturally accounts for duplicates and stays within the 1,000-element limit.

## Complexity detail

Let `n1` and `n2` be the array lengths, `a` the number of add calls, and `c` the number of count calls. Initialization builds the second counter in `O(n2)` time. Each add uses expected `O(1)` hash operations. Each count scans `n1` values with expected constant-time lookups. Total operation time is `O(n2 + a + c * n1)`.

The retained arrays occupy their input storage, and the counter initially has at most `n2` keys. Because zero-count keys are not deleted and each add may introduce a new value, exact counter key storage can grow to `O(n2 + a)`, rather than remaining strictly bounded by current distinct values. No per-query collection is allocated.

## Alternatives and edge cases

- **Frequency maps for both arrays:** Iterate the smaller distinct-key set and multiply both frequencies, which can help when `nums1` has many duplicates.
- **Scan both arrays for every count:** This costs `O(n1 * n2)` per query and is unnecessary.
- **Remove zero-count keys:** It preserves the same results while keeping counter size tied to current distinct `nums2` values.
- **Old and new value equal outside constraints:** Positive `val` means values always increase, so an add always changes the value.
- **Missing complement:** `Counter` returns zero and contributes no pair.
- **Duplicate values in `nums1`:** Each index must form its own pairs, and repeated generator lookups count them.
- **Duplicate values in `nums2`:** One counter frequency represents all valid second indices.
- **Repeated updates at one index:** Each operation first removes its current value, so the invariant remains correct.
- **Zero-frequency historical keys:** They are harmless for answers but consume space.
- **Caller-visible mutation:** `nums2` is changed in place because the original reference is retained.
- **Large totals:** Complement values may be negative or absent; counter lookup still safely returns zero.
- **Ordered indices:** Pair multiplicity is based on positions, not unique numeric pairs.
