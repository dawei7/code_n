## General

**Merge the two sorted streams.** Keep one pointer at the next unprocessed record in each input. If their IDs match, append one record containing that ID and the sum of both values, then advance both pointers. If the IDs differ, append the record with the smaller ID and advance only its pointer.

The smaller current ID cannot appear later in the other array because that array is strictly sorted and its current ID is already larger. It is therefore safe to emit immediately. For equal IDs, uniqueness within each input proves that the two current records are the only contributions to that output ID. These observations preserve both completeness and strict output ordering after every step.

When one input is exhausted, all records remaining in the other input have IDs larger than the last emitted ID and cannot have a counterpart. Append them unchanged. Each input pointer advances exactly once per record.

## Complexity detail

Let $n$ and $m$ be the lengths of `nums1` and `nums2`. The two pointers process each record once, taking $O(n + m)$ time. Apart from the required output array, the pointers and current record values use $O(1)$ auxiliary space. The output itself contains at most $n+m$ records.

## Alternatives and edge cases

- **Hash-map aggregation:** Accumulating values by ID is simple, but sorting the keys afterward costs $O((n+m) \log(n+m))$ time and uses extra map space despite the inputs already being sorted.
- **Nested matching:** Searching the second array separately for every first-array ID is correct but takes $O(nm)$ time before output sorting.
- **Completely disjoint IDs:** Every input record appears unchanged, and the pointers interleave them in ascending order.
- **Complete overlap:** Each step advances both pointers and emits the sum for one shared ID.
- **Unequal lengths:** After one pointer reaches its end, the remaining suffix of the other input is already in its final order.
- **Value bounds:** Two shared values can sum to $2000$, even though each individual input value is at most $1000$.
