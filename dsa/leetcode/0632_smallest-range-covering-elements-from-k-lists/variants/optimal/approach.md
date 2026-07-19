## General
**Represent one candidate from every list**

Place the first value of each list in a min-heap and track the maximum value currently represented. Those `K` values define a valid covering range from the heap minimum to the tracked maximum.

**Advance only the current minimum**

For the current maximum, no range beginning below the heap minimum can be better. To seek a smaller range, remove that minimum and replace it with the next value from the same sorted list. Advancing any other list would leave the minimum unchanged and could only preserve or increase the right endpoint.

**Record width and tie order explicitly**

Compare each valid range by `(right - left, left)`. This selects the shortest width first and the smaller left endpoint on a tie, exactly matching the required ordering.

**Why exhaustion ends the search**

The heap always contains exactly one representative from every list. When the list supplying the minimum has no next value, every future range would need an element from that exhausted list but all of its candidates at or beyond the current sweep position are gone. No later complete range exists. Every earlier complete configuration was examined before its minimum advanced, so the best recorded range is globally optimal.

## Complexity detail
Let `T` be the total number of values and `K` the number of lists. Each value is inserted into and removed from a heap of size `K` at most once, for $O(T \log K)$ time. The heap stores one entry per list, using $O(K)$ auxiliary space.

## Alternatives and edge cases
- **Flatten, sort, and slide a window:** tag every value with its source list, sort all `T` entries, and maintain a covering window; it is correct but costs $O(T \log T)$ time and $O(T)$ space.
- **Scan all current representatives:** maintain one pointer per list and linearly search for the minimum each round; it uses $O(K)$ space but can cost $O(TK)$ time.
- **Enumerate one choice per list:** directly tries the Cartesian product and becomes exponential in `K`.
- A single input list always yields a zero-width range at its smallest value.
- Duplicate values shared by all lists produce a zero-width answer.
- Negative values need no special treatment because only ordering and differences matter.
- Equal-width candidates must prefer the smaller left endpoint.
- Every list is nonempty, so the initial heap always covers all `K` lists.
