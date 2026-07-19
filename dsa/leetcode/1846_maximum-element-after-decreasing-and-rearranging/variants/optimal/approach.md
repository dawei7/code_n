## General
**Sort values by their ability to support steps**

Because elements may be rearranged freely, process them in non-decreasing order. Assigning a smaller original value before a larger one cannot reduce future possibilities: the smaller value has the tighter upper bound and should satisfy the earlier, lower step.

Maintain `maximum`, the greatest final value achievable at the end of the processed sorted prefix. Start at zero conceptually. For sorted value `value`, the next valid final number cannot exceed `maximum + 1`, because adjacent values may rise by at most one. It also cannot exceed `value`, because only decreases are permitted. Choose `min(value, maximum + 1)`.

**Why taking the largest legal step is optimal**

The chosen number is feasible: it is positive, no greater than the current original value, and at most one above the preceding constructed value. For the first element, positivity ensures the formula produces 1.

No valid arrangement of the same processed prefix can end higher. The current original element bounds its contribution by `value`; independently, the best previous prefix bound permits at most one additional unit. Therefore their minimum is an upper bound, and the greedy assignment reaches it. Induction over the sorted values proves that the final `maximum` is globally optimal.

## Complexity detail
Sorting $n$ values takes $O(n\log n)$ time, and the greedy scan takes $O(n)$. The app-local implementation creates a sorted copy using $O(n)$ space. An in-place sort can reduce additional storage according to the language's sorting implementation.

## Alternatives and edge cases
- **Frequency counting:** Clamp values above $n$ and count occurrences to obtain an $O(n)$-time alternative with $O(n)$ extra space, since the answer cannot exceed $n$.
- **Repeated minimum selection:** Choosing the next smallest unused element without sorting is correct but can require $O(n^2)$ scans.
- **Single element:** It can always be decreased to 1, so the answer is 1.
- **No original one:** The smallest element may be decreased to create the required first value.
- **Many ones:** Duplicate ones cannot support separate increasing steps until a larger value appears.
- **Huge values:** A value far above the current step is decreased to exactly one more than the current maximum.
- **Already consecutive:** Values `[1, 2, ..., n]` retain maximum $n$.
- **Input order:** It has no semantic effect because rearrangement is allowed.
