## General

Each operation depends only on the current maximum pile, so the data structure must repeatedly expose that maximum and accept its replacement. A max-heap provides both operations without sorting all piles again. Python's standard heap is a min-heap, so store every pile as its negative; the smallest stored number then represents the largest pile.

Heapify all $n$ negated values once. For each of the `k` seconds, remove the heap root, negate it to recover the richest pile, compute its exact integer square root, and push the negated replacement. Tied maxima need no special handling because the contract permits choosing any tied pile, and equal values produce equal replacements.

After exactly `k` updates, negating the sum of the heap entries gives the total number of gifts left. The heap always contains one entry for each original pile, and every loop iteration applies precisely the required transformation to a current maximum, so it represents the multiset of pile sizes after that second.

## Complexity detail

Let $n$ be the number of piles. Heap construction takes $O(n)$ time. Each of the $k$ operations performs one pop and one push, each in $O(\log n)$ time, for $O(n+k\log n)$ overall. The heap holds $n$ integers and therefore uses $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Scan for the maximum:** Finding the richest pile with `max` on every second is simple but takes $O(kn)$ time in the worst case.
- **Sort after every update:** Reordering all piles for each operation costs $O(kn\log n)$ and repeats work that a heap avoids.
- **Tied richest piles:** Any tied pile may be selected; because their values are equal, the resulting multiset is identical whichever one is used.
- **Piles of one:** Since $\lfloor\sqrt{1}\rfloor=1$, operations may eventually stop changing the values even though all `k` seconds must still be simulated.
- **Non-perfect squares:** Integer square root is required; ordinary floating-point rounding is unnecessary and can be unsafe in other numeric ranges.
- **Large totals:** The final sum can be as large as $10^{12}$, so fixed-width implementations must use a 64-bit total.
