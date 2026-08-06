## General

**Compact stable nonzero values into the prefix**

Maintain `write` as the position where the next nonzero value belongs. Scan with `read`; whenever a nonzero value
appears, swap it into `write` and advance that pointer.

Before processing `read`, `nums[:write]` contains exactly the nonzero values already seen, in their original order, and
every position in `nums[write:read]` is zero.

**Every swap extends the stable prefix**

Each encountered nonzero is placed at the first position after all earlier nonzeros, so their relative order is
preserved. When `read` differs from `write`, the displaced value is zero and moves into the not-yet-finalized suffix.
When they are equal, the swap leaves the value in place. At completion the prefix contains every nonzero exactly once,
and all remaining positions contain the original number of zeros.

## Complexity detail

The scan visits each of the $n$ elements once and performs at most one constant-time swap per element, giving $O(n)$
time. The read position, write position, and current value use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Shift the suffix for every zero:** preserves order but can take $O(n^2)$.
- **Filtered copy:** is stable and linear but violates the $O(1)$ in-place space requirement.
- **Guard self-swaps:** checking `read != write` before swapping can reduce writes on a zero-free prefix, but it changes
  only constant factors and not the required complexity.
- **All zeroes:** `write` never advances, and every value remains zero.
- **No zeroes:** each value is swapped with itself and the input remains unchanged.
