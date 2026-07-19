## General
**Count one decimal position at a time**

For a place value `factor` such as 1, 10, or 100, split `n` into the digits higher than that position, its current digit, and the lower remainder.

**Higher digits count complete cycles**

Across complete blocks of `10 * factor` consecutive numbers, the chosen position contains `1` exactly `factor` times. The higher part therefore contributes `higher * factor` occurrences.

**The current digit determines the partial cycle**

If the current digit is zero, there is no extra contribution. If it is one, add `lower + 1`. If it exceeds one, the full block of `factor` additional ones has already occurred.

After processing a factor, the running total equals all occurrences of digit one in every processed decimal position among numbers from zero through `n`.

**Each occurrence belongs to one position and one cycle**

For $n = 13$, the ones position contributes two (`1`, `11`) and the tens position contributes four (`10` through `13`), totaling six. The complete-cycle and partial-cycle cases exhaust all numbers for each position without overlap, so summing positions counts every digit occurrence exactly once.

For a fixed position, `higher` partitions `[0, n]` into complete blocks and the pair `(current, lower)` describes the only incomplete block. The three current-digit cases count that remainder exactly. Because every written `1` occupies one unique decimal position, adding these independent position totals neither omits nor duplicates an occurrence.

## Complexity detail
The factor is multiplied by ten per iteration, producing $O(\log n)$ iterations and $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Convert every number to a string:** costs `Theta(n log n)` total digit work.
- **Digit DP:** generalizes to richer digit constraints but stores unnecessary state here.
- Zero contributes no digit one; powers of ten exercise the partial-cycle boundary.
