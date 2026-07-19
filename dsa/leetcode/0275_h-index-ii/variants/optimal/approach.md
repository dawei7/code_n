## General
**Feasibility becomes monotone in sorted order**

At sorted index `i`, exactly $n - i$ papers lie at or above `citations[i]`. The index is feasible when `citations[i] >= n - i`; feasibility remains true for every index to its right.

Binary search keeps every possible first feasible index in `[left, right]`. A feasible midpoint moves the right boundary left to seek an earlier one; an infeasible midpoint discards itself and every earlier index.

**The boundary converts directly into the h-index**

Binary search locates the first index `left` satisfying `citations[left] >= n - left`. The suffix then contains `n - left` papers, each with at least that many citations. If a preceding index exists, its failure proves the larger candidate associated with that longer suffix is impossible. Therefore `n - left` is exactly maximal.

## Complexity detail
The search interval halves each iteration for $O(\log n)$ time. Two boundaries and a midpoint use $O(1)$ space.

## Alternatives and edge cases
- **Linear scan:** ignores the sorted-input advantage and takes $O(n)$.
- Empty input returns zero; an h-index may equal the complete paper count.
