## General
**Reduce each position to a shift residue**

For a source character and target character, the only relevant quantity is their forward cyclic difference from `0` through `25`. A zero difference needs no move. A nonzero difference `d` can use exactly the positive move numbers

`d, d + 26, d + 52, ...`

because adding 26 alphabet steps leaves the resulting letter unchanged.

**Schedule repeated residues in their earliest moves**

Maintain how many positions have already required each nonzero residue. If residue `d` has appeared `count` times before, its earliest unused compatible move is `d + 26 * count`. Reject immediately if that move exceeds `k`; otherwise reserve it by incrementing the count.

This greedy choice cannot harm another residue because different residues use disjoint move-number sequences modulo 26. Within one residue, assigning occurrences to compatible moves in increasing order is optimal: any other one-to-one assignment has a greatest move at least as large. Therefore every required position can be scheduled within `k` exactly when none of these earliest available moves exceeds the limit.

**Handle unchanged characters separately**

Positions where the characters already match do not consume a move. Treating their difference as residue zero would be wrong because move zero does not exist and moves `26`, `52`, and so on would unnecessarily alter scheduling. Skip them entirely.

Before scanning, compare the string lengths. A move changes a character but never inserts or deletes one, so unequal lengths make conversion impossible regardless of `k`.

## Complexity detail
Let $n$ be the common string length. The algorithm examines each paired character once for $O(n)$ time. Its 26 residue counters occupy fixed $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Search previous positions for the same shift:** correctly finds which compatible move occurrence is needed, but repeated prefix scans take $O(n^2)$ time.
- **Store every assigned move in a set:** can test collisions, but uses $O(n)$ space and obscures the simpler residue-count structure.
- Equal strings are always convertible, including when `k = 0`, because every move may be skipped.
- Strings of unequal length are impossible to convert because moves cannot change length.
- Wraparound differences such as `z` to `a` require shift `1`, while `a` to `z` requires shift `25`.
- Several positions may require the same residue, but their scheduled moves must differ by 26; using the same numbered move twice is forbidden.
- A very large `k` does not require iterating through moves; only the largest assigned move for each residue matters.
