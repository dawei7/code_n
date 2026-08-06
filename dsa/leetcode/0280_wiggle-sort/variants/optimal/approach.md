## General

**Repair the next alternating inequality locally**

Scan left to right. At odd position `i`, require `nums[i - 1] <= nums[i]`; at an even position, require
`nums[i - 1] >= nums[i]`. Swap the adjacent values exactly when the required relation is violated.

Before processing position `i`, every relation ending before `i` already wiggles. The optional swap fixes the relation
at `i` without breaking the preceding one because the value moved left is an even better local low or high for that
preceding requirement.

**The swap cannot break the inequality behind it**

At a position that must be a local high, a violating pair is swapped so the larger value moves right; the smaller value
moving left can only strengthen the preceding local-low relation. At a position that must be a local low, the symmetric
swap moves the larger value left and likewise strengthens the preceding local-high relation. Each step fixes the new
relation without disturbing the established prefix, so induction yields a valid wiggle ordering.

## Complexity detail

The candidate visits each of the $n - 1$ adjacent pairs once and performs at most one constant-time swap per pair. The
total time is $O(n)$ and the in-place scan uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Sort then interleave:** works but costs $O(n \log n)$.
- **Quadratic sorting before interleaving:** is correct but unnecessarily takes $O(n^2)$ time.
- **Equal neighbors:** satisfy both non-strict inequalities and require no special handling.
- **Empty or singleton input:** the app-local loop performs no work, although the source contract requires at least one
  element.
- **In-place contract:** every change is an adjacent swap, so the array's multiset is preserved without auxiliary
  storage.
