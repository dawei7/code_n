## General
**Repair the next alternating inequality locally**

Scan left to right. At odd index `i`, require `nums[i - 1] <= nums[i]`; at even index, require `nums[i - 1] >= nums[i]`. Swap the adjacent values exactly when the required relation is violated.

Before processing index `i`, every relation ending before `i` already wiggles. The optional swap fixes the relation at `i` without breaking the preceding one because the value moved left is an even better local low or high for that preceding requirement.

**The swap cannot break the inequality behind it**

At a position that must be a local high, a violating pair is swapped so the larger value moves right; the smaller value moving left can only strengthen the preceding local-low relation. At a position that must be a local low, the symmetric swap moves the larger value left and likewise strengthens the preceding local-high relation. Each step fixes the new relation without disturbing the established prefix, so induction yields a valid wiggle ordering.

## Complexity detail
One comparison and at most one swap per adjacent pair gives $O(n)$ time and $O(1)$ space.

## Alternatives and edge cases
- **Sort then interleave:** works but costs $O(n \log n)$.
- **Quadratic sorting before interleaving:** is unnecessarily slow.
- Equal values satisfy both non-strict inequalities; empty and singleton arrays already qualify.
