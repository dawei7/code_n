## General
**Turn flips into a window condition:** A subarray can be changed entirely to ones precisely when it contains at most `k` zeroes. Its existing ones cost nothing, and each zero consumes one permitted flip. This converts the requested run into the longest contiguous window satisfying a simple zero-count constraint.

**Grow the right boundary and repair violations:** Maintain a left boundary, a zero counter, and the best valid length. Move the right boundary across `nums`, incrementing the counter whenever `nums[right] == 0`. If the count exceeds `k`, advance `left` until enough departing zeroes have been removed and the window is valid again. Once repaired, update the best length with `right - left + 1`.

**Why discarding the prefix is safe:** For a fixed right boundary, after shrinking stops, `left` is the earliest boundary that leaves at most `k` zeroes in the window. Any earlier boundary is invalid, so no longer valid window ending at this position was skipped. Boundaries only move to the right; therefore every possible right endpoint is considered and the longest feasible subarray is recorded.

## Complexity detail
The right boundary visits each of the $N$ entries once. The left boundary also advances at most $N$ times over the entire run, so the total work is $O(N)$ rather than one complete scan per window. The two boundaries, the zero counter, and the best length use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Prefix sums plus binary search:** Prefix zero counts can test a window quickly, and binary searching each left boundary gives $O(N\log N)$ time and $O(N)$ space, but it is less direct than the linear window.
- **Try every starting position:** Extending a fresh window from every index is correct, but an array with no zeroes forces $\Theta(N^2)$ inspections.
- **Zero flip allowance:** When `k == 0`, the window reduces to the longest run already containing only ones.
- **Allowance covers every zero:** If the array has at most `k` zeroes, the entire array is feasible and the answer is $N$.
- **All zeroes:** The result is $\min(N,k)$, including `0` when `k == 0`.
