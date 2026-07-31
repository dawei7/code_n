## General

Moving an element at index $i$ to the front costs exactly $i$ adjacent swaps. Among duplicate minimum values, the leftmost occurrence therefore has the least possible frontward cost. Symmetrically, among duplicate maximum values, the rightmost occurrence has the least possible cost to reach the final index.

Scan once to record those two occurrences. Update the minimum index only for a strictly smaller value, preserving the first minimum. Update the maximum index for a greater or equal value, preserving the last maximum.

Without interaction, their costs sum to `minimum_index + n - 1 - maximum_index`. If the selected minimum begins to the right of the selected maximum, the two elements must cross. The swap in which they cross moves both one step toward their destinations, but the separate distances count that same swap twice. Subtract one exactly in this case. If the minimum already lies to the left, their routes do not cross and no correction is needed.

## Complexity detail

Let $n$ be the array length. One scan finds both chosen indices in $O(n)$ time, after which the answer is constant-time arithmetic. The method stores two indices and a loop variable, using $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Simulate every swap:** This reaches the same arrangement but can take $O(n^2)$ time when an extreme crosses most of the array.
- **Choose arbitrary duplicate extremes:** A later minimum or earlier maximum adds avoidable travel, so the occurrences nearest their required endpoints are necessary for optimality.
- **Crossing correction:** When the minimum starts after the maximum, failing to subtract one double-counts their shared adjacent swap.
- **Single element:** Its endpoint distances are both zero and no crossing occurs.
- **All values equal:** The first occurrence serves as the minimum and the last as the maximum, so the array is already valid.
