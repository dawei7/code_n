## General

**Express compatibility as a bitmask condition**

Two positive integers `a` and `b` share no set bit exactly when

`a & b = 0`.

Let `B` be the bit length of the largest input value, and let

`full_mask = 2^B - 1`,

whose lowest `B` bits are all one.

Within those relevant bits, `full_mask ^ a` is the complement of `a`: it has ones exactly where `a` has zeros.

The condition `a & b = 0` is equivalent to saying every set bit of `b` lies inside this complement. In bitmask language, `b` must be a submask of

`full_mask ^ a`.

Thus, for each `a`, the task is to find the largest input value that is a submask of one known mask.

**Why the largest compatible value is enough**

All input values are positive. For a fixed `a`, the product `a * b` increases as `b` increases.

Therefore, among all compatible partners for `a`, only the numerically largest one can produce the best product with `a`. We do not need the full list or number of partners.

The source precomputes, for every possible mask, the largest input number that is a submask of that mask.

**Initialize exact-mask values**

The array `best_submask` has length `2^B`. Initially it is all zero.

For every input `value`, the source assigns

`best_submask[value] = value`.

At this point, entry `mask` is nonzero only when that exact number appears. Duplicate copies do not change the stored maximum because their numeric values are identical.

Zero serves as “no present value found.” This is safe because the input values are at least one.

**Propagate information from submasks to masks**

The subset dynamic program processes one bit position at a time. For a mask whose current bit is one, removing that bit produces a smaller mask that is a submask of it.

The usual recurrence is

`best[mask] = max(best[mask], best[mask without current bit])`.

After all `B` bits are processed, every entry contains the maximum exact input value among all its submasks.

The source implements this recurrence with blocks:

- `half = 1 << bit`.
- Each block has length `2 * half`.
- `lower = start + offset` has the bit unset.
- `upper = lower + half` has the same other bits and this bit set.

If `best_submask[lower]` is larger, it is copied into `upper`. Because `lower` is a submask of `upper`, every candidate valid for `lower` is also valid for `upper`.

**Why repeated bit passes cover every submask**

Suppose value `v` is a submask of mask `m`. Every bit set in `v` is also set in `m`, while `m` may contain additional bits.

Starting from exact entry `v`, the DP can add those extra bits one at a time through lower-to-upper propagation. After the pass for every extra bit, `v`’s value has reached `m`.

No incompatible value can reach `m` because propagation only adds allowed bits to a containing mask. Thus the final entry is exactly the largest present submask.

This technique is often called SOS DP, short for “sum over subsets,” although here the aggregation operation is maximum rather than sum.

**Look up the best partner for every input value**

For each `value`, its allowed partner mask is

`full_mask ^ value`.

The precomputed entry at that mask is the largest input number whose set bits are all outside `value`. Multiplying them produces the best compatible product with this fixed value.

The source takes the maximum across all input occurrences.

If no compatible partner exists, the lookup returns zero and contributes product zero. If every value lacks a partner, the final maximum is zero as required.

**Why distinct indices are respected**

Could a value accidentally select itself from the table? For a positive `value`,

`value & value = value != 0`,

so it is not a submask of its own complement. The lookup cannot return the same positive mask as a compatible partner.

Therefore any nonzero partner comes from an occurrence with a different value and hence a distinct index. Duplicates of the same positive number cannot pair with each other either, because they share all their set bits.

If zero were allowed, distinct-index handling would need extra care because zero is compatible with itself, but the constraints exclude zero.

**Trace the first example**

For value three, binary `011`, and a bit domain containing value four, its complement has the relevant form `100`. The largest present submask is four.

Their product is twelve. Values such as five `101` cannot pair with three because they share the lowest bit, and the complement lookup excludes them automatically.

**Trace the powers-of-two example**

Values 64, 8, and 32 each have one different set bit. For 64, the complement permits both eight and 32, and the table returns the larger 32. Their product is 2048.

**Why the bit domain stops at the maximum’s length**

No input has a set bit at position `B` or above. Adding higher zero positions to every complement would not permit any new input partner, but it would double the table for each unnecessary bit.

Using `max(nums).bit_length()` creates the smallest complete mask universe. With values at most `10^6`, `B <= 20` and the table has at most `2^20` entries.

## Complexity detail

Let `n` be the input length and `B` the maximum bit length.

Initialization visits all values in `O(n)` time. The subset DP processes every one of `B` bits across all `2^B` masks, for `O(B * 2^B)` time. Final partner lookups take `O(n)`.

Total time is `O(n + B * 2^B)`.

The table stores `2^B` integers, so auxiliary space is `O(2^B)`. Other variables use constant space.

At `B = 20`, the table has 1,048,576 entries and the bit propagation performs roughly twenty million constant-time comparisons, which is practical for the constraint.

## Alternatives and edge cases

- **Check every pair:** It costs `O(n^2)` and is too slow for `n = 10^5`.
- **Store only distinct values and compare them:** Deduplication may help practical work but can still leave too many pairs.
- **Bitwise trie:** A trie can search for large values avoiding forbidden bits, but maximizing numeric value under an AND-zero constraint is more involved than the subset table.
- **Complement without masking:** Python’s unary bitwise complement produces an infinite signed representation. Use `full_mask ^ value` within the relevant `B` bits.
- **No compatible pair:** Every complement lookup is zero and the source returns zero.
- **Duplicate positive values:** They cannot pair with each other because their AND is nonzero.
- **Distinct indices:** Any nonzero compatible partner has a different mask, guaranteeing a different input occurrence.
- **Powers of two:** Different powers have disjoint bits and are mutually compatible.
- **One value’s mask is zero:** Inputs are positive, so this case does not occur.
- **Maximum input value:** Its bit length determines the complete finite domain; smaller values fit automatically.
- **Repeated table propagation:** A value may reach many supermasks, which is the intended preprocessing that makes each query constant time.
- **Input preservation:** The source reads `nums` and allocates a separate DP table without modifying the array.
