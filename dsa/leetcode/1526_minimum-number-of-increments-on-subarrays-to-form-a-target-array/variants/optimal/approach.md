## General
**View operations as horizontal layers**

Each range increment contributes one unit-height horizontal layer across a contiguous group of columns. At index 0, `target[0]` layers must begin because no earlier column can carry a layer into the array.

Moving from `target[i - 1]` to `target[i]`, existing layers can continue across the boundary up to the smaller height. If the current height is larger, the excess `target[i] - target[i - 1]` cannot come from the left and therefore requires that many new operations starting at or before index `i`; starting them at `i` is sufficient. A drop starts no new layers because surplus layers simply end at the previous index.

**Sum every unavoidable rise**

The minimum is consequently `target[0]` plus every positive adjacent difference. This is a lower bound because each counted layer start needs a distinct operation. It is attainable by extending every layer across as many later columns as their heights permit, so the same count constructs the target.

Only adjacent heights matter. The actual intervals need not be materialized, and overlapping mountains or valleys are handled by starting layers on rises and ending them on drops.

## Complexity detail
A single left-to-right scan examines each adjacent pair once, giving $O(n)$ time. The running total and previous/current values use $O(1)$ auxiliary space.

The answer may exceed any individual target height because separated rises require independent operations, but the source guarantees the total fits a 32-bit integer.

## Alternatives and edge cases
- **Per-height run counting:** for each horizontal level, count contiguous positive runs. It proves the layer interpretation but may require $O(nH)$ time for maximum height $H$.
- **Operation-by-operation simulation:** repeatedly decrement positive runs. It is correct but can be much slower than reading boundary rises directly.
- **Monotonic stack:** layers can be opened and closed with a stack, but adjacent positive differences already encode the same information more simply.
- **Single element:** its target value is the number of required one-position increments.
- **Strictly increasing target:** every rise adds, so the answer equals the final height.
- **Strictly decreasing target:** all layers start at index 0, so the answer equals the first height.
- **Flat plateau:** equal adjacent heights reuse all active layers and add no operation.
- **Separated peaks:** each rise after a valley starts additional layers and must be counted independently.
