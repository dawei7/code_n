## General
**Inspect even and odd positions independently**

Use one pointer that visits only even indices and another that visits only odd indices. An even-positioned value is correct when it is even. If the even pointer finds an odd value, there must be a misplaced even value at some odd index: the input contains equal counts of both parities, so parity deficits on one side are balanced by surpluses on the other.

Advance the odd pointer by two until it finds that misplaced even value, then swap the two values. After the swap, both positions satisfy their required parity. Continue advancing the even pointer through its index class; the odd pointer never needs to move backward because all earlier odd positions have already been fixed.

Every swap repairs one mismatch of each type and never disturbs a completed position. The equal-count guarantee ensures a matching odd-index mismatch always exists whenever an even-index mismatch is found. Once all even positions are correct, all remaining odd positions must also be correct, and swapping preserves the original multiset.

## Complexity detail
Let $n$ be the length of `nums`. Each pointer advances monotonically through at most half the indices, so the total work is $O(n)$. Rearrangement uses only the two indices and temporary swap storage, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Separate even and odd lists:** Collecting both groups and interleaving them is simple and linear, but requires $O(n)$ additional space.
- **Repeatedly search remaining values:** Selecting one value of the required parity for each output position is correct but can take $O(n^2)$ time.
- **Sort first:** Sorting and then interleaving parity groups costs $O(n\log n)$ and does more ordering work than the contract requires.
- **Already valid input:** Both pointers pass through without swapping.
- **Every position misplaced:** Each swap fixes one even and one odd index, so exactly $n/2$ swaps suffice.
- **Duplicate values and zero:** Only parity matters; duplicates are preserved and zero is even.
- **Multiple valid answers:** Correctness depends on the multiset and index parities, not on one expected ordering.
