## General

**Begin with what rotation preserves**

Before rotation, `nums` is in ascending order, although equal neighboring values
are allowed. A rotation does not scramble the order arbitrarily. It produces a
high-valued segment followed by a low-valued segment, and the first element of
the low segment is a minimum of the original sorted array.

A linear scan could find that value, but most inputs still contain enough order
to discard half of the remaining indices at once. The selected solution uses
binary search and accepts that duplicates sometimes remove the information
needed for a halving step.

The variables `l` and `r` are inclusive boundaries. The central invariant is:
at least one occurrence of the array's minimum lies in `nums[l:r + 1]`.
Initially this is true because the interval is the entire nonempty array.

**Compare the midpoint with the current right endpoint**

While `l < r`, the code computes the floor midpoint with
`mid = (l + r) >> 1`. Because the indices are nonnegative, shifting their sum
right by one has the same result as integer division by two.

The value at `r` is useful because the section from the minimum through the
right boundary is nondecreasing. Comparing `nums[mid]` with `nums[r]` creates
three cases.

If `nums[mid] > nums[r]`, the rotation break must occur strictly after `mid`.
An ordinarily sorted interval could not have a larger earlier value and a
smaller later value. Therefore `mid` cannot hold the minimum, and neither can
the part from `l` through `mid`; the source safely sets `l = mid + 1`.

If `nums[mid] < nums[r]`, `mid` lies in the low sorted portion. The minimum can
be at `mid` itself or somewhere to its left, but it cannot be strictly to the
right of `mid`: that suffix rises from `nums[mid]` toward `nums[r]`. The source
therefore sets `r = mid`. Keeping `mid` is essential. For example, in
`[3,1,3]`, the first midpoint is the minimum; using `r = mid - 1` would throw
it away.

**Why equality permits only a cautious step**

If `nums[mid] == nums[r]`, their equal values do not reveal whether `mid` is on
the high side, on the low side, or inside a plateau that crosses the rotation
point. Consider how different arrays can look identical at the two inspected
positions: in `[1,3,3]` the minimum is to the left, while in `[3,3,1,3]` it is
to the right of an early midpoint.

The source responds with `r -= 1`. This removes just the rightmost occurrence.
Why is that safe? If `nums[r]` is not a minimum, removing it is plainly safe.
If it is a minimum, then `nums[mid]` has exactly the same value and remains
inside the interval, so another occurrence of the minimum survives. The
invariant promises an occurrence, not one particular index, which is precisely
what makes this deletion valid.

Moving `l` right merely because the two values are equal is not generally safe.
For `[1,3,3]`, doing so can discard the only minimum. Equality has asymmetric
safe handling here because the equal midpoint provides a replacement for the
right endpoint, whereas it does not necessarily replace the left endpoint.

**Trace the decisions**

For `[2,2,2,0,1]`, begin with `l = 0` and `r = 4`. The first midpoint holds two
and the right endpoint holds one, so the minimum must be after the midpoint;
`l` becomes three. The remaining interval is `[0,1]`. Its midpoint holds zero,
which is less than one, so `r` moves to that midpoint. Both boundaries now
identify zero.

For `[1,1,1,1]`, every comparison is equality. The right boundary moves left
one position at a time. This is slower, but every remaining value is still a
minimum, so correctness is preserved.

For `[10,1,10,10,10]`, equality first removes indistinguishable values from the
right. Eventually a comparison exposes the smaller low segment and the search
converges on one. This is the kind of arrangement that defeats a rule designed
only for distinct values.

**Why the returned value is correct**

Every branch strictly shortens `[l, r]` while retaining at least one minimum:
the greater case removes a proven high prefix, the smaller case removes a
proven nondecreasing suffix after a possible minimum, and the equality case
removes a value duplicated at `mid`.

The loop ends only when `l == r`. The invariant still holds, but the interval
now contains one index. Consequently `nums[l]` must be a minimum. The method
reads the array without modifying it.

## Complexity detail

Let $n$ be the number of elements.

When `nums[mid]` and `nums[r]` differ, the candidate interval is reduced by
roughly half, giving binary-search behavior. On many inputs the running time is
therefore $O(\log n)$.

The worst case is different. With a long duplicate plateau, equality may allow
only `r -= 1`, removing a single index per iteration. An array of identical
values realizes this behavior, so the worst-case time is $O(n)$. This explains
the manifest's conservative $O(n)$ bound and directly answers the follow-up:
duplicates can destroy the logarithmic guarantee because a comparison may
provide no directional information.

The algorithm stores only the three indices and uses no recursion or
input-sized container. Its auxiliary space is $O(1)$. The input array itself is
not counted as auxiliary storage.

## Alternatives and edge cases

- **Linear scan:** Taking the minimum of every element is simpler and has the same $O(n)$ worst-case bound, but it gives up the much faster logarithmic behavior available when comparisons are informative.
- **Skip equal values from both ends:** This can be correct with carefully stated conditions, but it adds cases and does not improve the linear worst-case bound.
- **Distinct-only binary search:** The ID 153 rule has no equality branch. Applying it unchanged here can discard the side containing the minimum because duplicate values no longer identify a unique segment.
- **One element:** `l == r` initially, so the loop skips and returns the only value.
- **All elements equal:** Equality repeatedly decreases `r`; the result is correct and the running time is linear.
- **No visible rotation:** Smaller-than-right decisions retain the left side until index zero remains.
- **Minimum repeated across the boundary:** The invariant needs only one minimum occurrence, so removing a duplicate endpoint remains safe.
- **Negative and positive values:** Only ordering and equality matter; numeric signs do not affect the decisions.
- **Nonempty contract:** The returned index is valid because the input length is at least one.
- **Standalone typing dependency:** The selected source annotates `List[int]` without importing `List`; a standalone Python module needs `from typing import List` unless the harness supplies it.
