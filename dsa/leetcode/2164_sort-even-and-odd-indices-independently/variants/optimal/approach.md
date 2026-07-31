## General

**Separate the two independent orderings**

An even-indexed value can never move to an odd index, or vice versa. Therefore
the required arrangement is completely determined by two subsequences:
`nums[::2]` must be sorted in non-decreasing order, and `nums[1::2]` must be
sorted in non-increasing order.

Extract and sort those subsequences separately. Copy the original array, then
assign the ascending values back to its even-indexed slice and the descending
values back to its odd-indexed slice. Each destination receives exactly the
multiset that originally occupied its parity group, and the two required order
relations hold, so the constructed array is the unique valid result.

## Complexity detail

For an array of length $n$, each parity group contains at most
$\lceil n/2\rceil$ values. Sorting both groups takes $O(n\log n)$ time, and the
extracted groups plus returned array use $O(n)$ auxiliary space.

The benchmark uses the full array length as `size`. Its mixed-value tiers make
both parity groups require substantial reordering, distinguishing comparison
sorting from quadratic repeated minimum/maximum selection.

## Alternatives and edge cases

- **Two heaps:** A min-heap for even-indexed values and a max-heap for
  odd-indexed values also gives $O(n\log n)$ time, but ordinary sorting is
  shorter and has lower constants.
- **Repeated selection:** Repeatedly scanning for the next minimum even value
  and maximum odd value is correct, but takes $O(n^2)$ time.
- A length-one array has no odd-indexed values and is returned unchanged.
- For odd $n$, the even-indexed group has one more value than the odd-indexed
  group.
- Duplicate values preserve their multiplicities; their individual identities
  do not matter.
- The rule concerns index parity, not whether the stored values are even or
  odd.
