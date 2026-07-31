## General

Only two kinds of adjacent inversion can ever be swapped: `2, 1` and `3, 2`. A `3` that occurs before a `1` can never cross that `1`, because their difference is two and swapping either value with intervening `2`s cannot reverse the relative order of those two occurrences. Therefore, if the first `3` lies before the last `1`, sorting is impossible regardless of which indices are unlocked.

Assume that obstruction does not exist. Every `2` before the last `1` must cross a `1`. During those crossings, the left side of the swapped pair visits every index from the first `2` through the position immediately before the last `1`. Each of those indices must be unlocked. Conversely, unlocking that entire interval permits all required `2, 1` inversions to be removed.

The same reasoning applies to `3, 2` inversions: every index from the first `3` through the position immediately before the last `2` must be unlocked, and that is sufficient for all `3`s to cross the necessary `2`s. In a feasible input the `2, 1` region ends no later than the first `3`, so the two requirements do not create a hidden `3, 1` crossing. Count the currently locked indices belonging to either half-open interval. Indices already unlocked cost no operation, while every counted locked index is both necessary and sufficient.

## Complexity detail

One scan finds the first and last relevant occurrences, and one scan counts locked indices in the required intervals. This takes $O(n)$ time. Only four boundary indices and scalar counters are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Simulate adjacent swaps:** Repeated bubble-sort passes can discover required unlocks but may perform $O(n^2)$ swaps.
- **Try subsets of locked indices:** Exhaustive unlocking is exponential and ignores the interval structure forced by crossings.
- **A `3` before a `1`:** Their relative order cannot change under the permitted swaps, so the result is `-1`.
- **Already sorted or one value only:** Both required intervals are empty and no operation is needed.
- **Missing `1`, `2`, or `3`:** Sentinel boundaries naturally leave the corresponding interval empty.
- **Already-unlocked required indices:** They remain necessary for swaps but contribute zero to the operation count.
- **Half-open endpoints:** The rightmost smaller value is never the left index of its crossing, so `last_one` and `last_two` are excluded.
