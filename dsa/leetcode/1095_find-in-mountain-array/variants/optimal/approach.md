## General
**Find the peak without reading the whole array.** At a midpoint `mid`, comparing `get(mid)` with `get(mid + 1)` reveals the slope. If the values rise, the peak lies strictly to the right; otherwise the peak is at `mid` or to its left. Repeating this binary decision isolates the unique peak in $O(\log n)$ calls.

**Search the increasing side first.** The prefix ending at the peak is strictly increasing, so ordinary binary search applies. Returning immediately when it finds `target` guarantees the minimum index: every index on this slope precedes every index on the decreasing slope.

**Reverse the comparison on the decreasing side.** If the first search fails, binary-search the suffix after the peak. Here a midpoint value smaller than `target` means moving left, while a larger value means moving right. The strict ordering on each side makes both searches valid, and searching their union covers the entire mountain.

The peak search never discards the peak because its slope comparison retains the half containing the transition. Each subsequent search discards only values that cannot equal the target under that side's strict order. Thus a found index is valid, the increasing-side priority makes it minimal, and failure of both searches proves absence.

## Complexity detail
Peak discovery and the two side searches each use $O(\log n)$ time and `MountainArray.get` calls, for $O(\log n)$ overall. At $n \leq 10^4$, the three searches stay below the 100-call limit. They maintain only interval endpoints and current values, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Linear scan:** It would find the first occurrence in $O(n)$ time but can exceed the 100-call interactive limit.
- **Cache queried values:** Memoization can avoid duplicate `get` calls, though the uncached three-search method already fits the limit and uses constant space.
- **Target on both slopes:** Search the strictly increasing prefix first so the returned index is the minimum one.
- **Target equals the peak:** The first binary search includes the peak and returns it without searching the descending suffix.
- **Target absent:** Both ordered searches terminate with `-1`; no full traversal is needed.
- **Three-element mountain:** The peak search and side intervals remain valid at the minimum permitted length.
