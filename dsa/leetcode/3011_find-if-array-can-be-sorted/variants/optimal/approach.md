## General

**The popcount sequence is fixed.** Swapping equal-popcount neighbors exchanges
their values but leaves the popcount at both positions unchanged. Therefore no
value can cross a boundary between two maximal contiguous blocks with different
set-bit counts.

Inside one block, adjacent swaps can realize any permutation, so that block's
values may be sorted freely. The entire array is sortable exactly when every
value in one block can precede every value in the next. It is enough to compare
the current block's minimum with the maximum value over all preceding blocks.

Scan each block, compute its minimum and maximum, reject if its minimum is below
the previous maximum, and otherwise carry its maximum forward. Passing every
boundary proves that sorting each block yields a globally non-decreasing array.

## Complexity detail

Every element is inspected once. The method uses $O(N)$ time and $O(1)$
auxiliary space.

## Alternatives and edge cases

- **Sort each popcount block:** This directly constructs the best reachable array but costs $O(N\log N)$ time.
- **Simulate allowed bubble swaps:** Repeatedly swapping legal inversions is correct but can cost $O(N^2)$ time.
- **Group values globally by popcount:** Values with the same count but separated by another count cannot cross that intervening block.
- **Already sorted:** The block boundary inequalities hold even if no swap is needed.
- **Single element:** One value is trivially sorted.
- **Duplicate values:** Equality across or within block boundaries is allowed.
