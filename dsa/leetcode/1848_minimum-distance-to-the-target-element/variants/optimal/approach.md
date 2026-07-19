## General
Scan `nums` with both each value and its index. Whenever the value equals `target`, compute the absolute index difference from `start`. The answer is the minimum of those candidate distances.

Every possible destination is examined exactly once, so no target occurrence can be missed. Non-target indices are never considered as destinations. Taking the minimum over precisely the target positions therefore returns exactly the fewest required adjacent moves. The guarantee that `target` occurs makes the minimum well-defined.

## Complexity detail
The scan visits $n$ elements, giving $O(n)$ time. A running minimum requires $O(1)$ auxiliary space. The generator expression in the reference streams candidate distances rather than storing all matching indices.

## Alternatives and edge cases
- **Expand in both directions:** Check equal distances to the left and right of `start`; the first target found is nearest, but boundary handling is more elaborate.
- **Repeated growing slices:** Searching a larger copied interval for every possible distance is correct but can copy and rescan $O(n^2)$ elements.
- **Target at `start`:** The minimum distance is zero.
- **Multiple occurrences:** A farther occurrence must not overwrite a nearer one.
- **Equal left and right distance:** Either position gives the same numeric answer.
- **Endpoint target:** Absolute difference handles index 0 and index $n-1$ without special cases.
- **Single element:** The target guarantee forces distance zero.
