## General
**Locate only values on the wrong side**

The final array has one boundary: every value to its left is even, and every value to its right is odd. A left pointer can skip values that are already even, while a right pointer can skip values that are already odd. If both pointers stop before crossing, the left pointer identifies an odd value that belongs on the right and the right pointer identifies an even value that belongs on the left.

Swap those two misplaced values, then move both pointers inward. The swap permanently places an even value in the settled prefix and an odd value in the settled suffix. Repeating this process requires no knowledge of the exact boundary in advance.

Before each swap, all positions strictly before the left pointer are even and all positions strictly after the right pointer are odd. The swap and pointer updates preserve those facts while expanding both settled regions. When the pointers meet or cross, no unresolved position can contain an odd value before an even value, so the entire array satisfies the required partition. Swapping never adds or removes an element, so the result is also a permutation of the input.

## Complexity detail
Each pointer moves only toward the center and visits at most $n$ positions. The total running time is therefore $O(n)$. The rearrangement is performed inside `nums` with two index variables, so the auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Two filtered lists:** Collecting the even values and odd values separately and concatenating them is simple and stable within each group, but it uses $O(n)$ auxiliary space.
- **Sort by parity:** Sorting with parity as the key produces a valid partition but generally costs $O(n\log n)$ time.
- **Stable insertion partition:** Moving each encountered even value ahead of earlier odd values preserves group order, but repeated shifts can take $O(n^2)$ time.
- **All values have one parity:** Both an all-even array and an all-odd array already satisfy the condition.
- **Zero:** `0` is even and belongs in the leading group.
- **Duplicates:** Every occurrence must be preserved; the partition rule does not permit dropping repeated values.
- **Relative order:** The two-pointer swaps are not stable, which is acceptable because the contract allows any satisfying arrangement.
