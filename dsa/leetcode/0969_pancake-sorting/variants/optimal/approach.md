## General
**Fix the sorted suffix from right to left.** For each target value from $N$ down to `2`, locate that value within the still-unsorted prefix. Positions after the target index are already fixed and are never included in later flips.

**Bring the target to the front, then to its destination.** If the target is already at index `target - 1`, do nothing. Otherwise, if it is not at index `0`, flip through its current index to move it to the front. Then flip the first `target` elements, placing that value at index `target - 1`. Record each prefix length as it is applied.

**Why earlier work remains valid.** Both flips end at or before the target's destination, so the sorted suffix beyond that position is untouched. Each iteration permanently places one more maximum value. When target `2` is handled, the remaining prefix is also sorted, proving that the recorded sequence is valid.

**Respect the flip limit.** Each of the $N-1$ target values uses at most two flips, for no more than $2N-2$. This is safely below the allowed $10N$ bound.

## Complexity detail
Locating a target and reversing one or two prefixes each take $O(N)$ time per target, for $O(N^2)$ total time. The returned flip sequence contains $O(N)$ integers; apart from that output and temporary Python slices, the greedy state is constant-sized, giving $O(N)$ space for this implementation.

## Alternatives and edge cases
- **Maximum-by-rank scans:** For every candidate in the active prefix, compare it with every other candidate to identify the maximum before flipping. It is correct but raises time to $O(N^3)$.
- **Breadth-first search over permutations:** This can find a shortest flip sequence for tiny arrays but has factorial state growth and is unnecessary because optimal flip count is not required.
- **Ordinary comparison sort:** Sorting a copy does not provide the required prefix-flip sequence.
- **Already sorted input:** Return an empty sequence; no flip is necessary.
- **Target already placed:** Skip it rather than adding redundant flips.
- **Single element:** The one-value permutation is already sorted.
