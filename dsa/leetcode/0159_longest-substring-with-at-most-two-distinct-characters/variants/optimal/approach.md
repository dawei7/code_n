## General
**Right expansion considers every possible ending position**

Move `right` through the string and increment the included character's count. The interval `[left,right]` is the current candidate ending at `right`; before normalization it may temporarily contain a third character type.

**Left contraction stops at the earliest valid boundary**

While the count map has more than two keys, decrement `s[left]`, delete its key exactly when the count reaches zero, and advance `left`. Stop immediately once only two types remain, then update the best length.

Deleting zero-count keys is essential: retaining them would make map size overstate the number of distinct characters still inside the window.

**After contraction, the window is maximal for its right endpoint**

After shrinking, the window contains at most two distinct characters and is the longest valid window ending at the current right boundary: moving its left edge backward would restore the third character that forced shrinking.

**Trace the third character forcing an eviction**

For `eceba`, the window grows to `ece`. Adding `b` creates three character types, so the left edge moves through `e` then `c` until the window is valid again. The recorded maximum remains three.

**The leftmost valid window is best for each right endpoint**

After adding a character at `right`, the left boundary advances only while the window contains more than two distinct characters. When shrinking stops, the window is valid and its boundary is the farthest left one that remains compatible with this right endpoint; any earlier boundary would still include the third character that forced the shrink.

Every candidate substring has some right endpoint. The maintained window is the longest valid candidate for that endpoint, so taking the maximum over all endpoints yields the global optimum.

## Complexity detail
Each character enters and leaves the window at most once, giving $O(n)$ time. The map contains at most three keys transiently and at most two after shrinking, so space is $O(1)$ relative to input length.

## Alternatives and edge cases
- **Start a scan at every index:** is simple but costs $O(n^2)$.
- **Store last positions of only two characters:** can also work but needs careful handling when choosing which character to evict.
- **Enumerate character pairs:** multiplies work by the alphabet and still requires repeated scans.
- Empty input returns zero. A string with one or two distinct characters is entirely valid.
- Frequent transitions among three characters may trigger many shrink iterations, but each left position is removed only once overall.
