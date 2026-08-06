## General
**Feasibility becomes monotone in sorted order**

At sorted index `i`, exactly $n - i$ papers lie at or above `citations[i]`. The index is feasible when `citations[i] >= n - i`; feasibility remains true for every index to its right.

Binary search keeps every possible first feasible index in `[left, right]`. A feasible midpoint moves the right boundary left to seek an earlier one; an infeasible midpoint discards itself and every earlier index.

**The boundary converts directly into the h-index**

Binary search locates the first index `left` satisfying `citations[left] >= n - left`. The suffix then contains `n - left` papers, each with at least that many citations. If a preceding index exists, its failure proves the larger candidate associated with that longer suffix is impossible. Therefore `n - left` is exactly maximal.

## Complexity detail

Each iteration halves the half-open search interval `[left, right)`, so the boundary is found in $O(\log n)$ time.
The two boundaries, midpoint, and paper count use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Linear scan:** ignores the sorted-input advantage and takes $O(n)$.
- **Empty input:** the app-local half-open search returns zero defensively, although the native contract requires at least one paper.
- **Every paper qualifies:** the first feasible position is zero, so the result can equal the complete paper count.
- **No positive threshold qualifies:** the boundary reaches `n`, yielding an h-index of zero.
