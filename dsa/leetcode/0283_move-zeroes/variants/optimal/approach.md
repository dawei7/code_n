## General
**Compact stable nonzero values into the prefix**

Maintain the index where the next nonzero value belongs. Scan the array; whenever a nonzero value appears, swap it into that write position and advance the write index.

Before each scan position, the prefix ending at the write index contains exactly the nonzero values already seen, in their original order. Positions between the write and scan indices are zeros.

**Every swap extends the stable prefix**

Each encountered nonzero is placed at the first position after all earlier nonzeros, so their relative order is preserved. When the scan index differs from the write index, the displaced value is zero and moves into the not-yet-finalized suffix. At completion the prefix contains every nonzero exactly once and all remaining positions contain the original number of zeros.

## Complexity detail
One pass performs at most one swap per element for $O(n)$ time and uses only two indices.

## Alternatives and edge cases
- **Shift the suffix for every zero:** preserves order but can take $O(n^2)$.
- Creating a filtered copy violates the in-place space requirement; all-zero and zero-free arrays remain valid.
