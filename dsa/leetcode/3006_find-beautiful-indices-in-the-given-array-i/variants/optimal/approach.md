## General

**Collect every occurrence, including overlaps.** Find the sorted start indices
of `a` and `b`, advancing the next search by one position rather than by the
pattern length. This preserves overlapping matches such as both starts of
`"aa"` inside `"aaa"`.

**Merge the two sorted lists.** Maintain a pointer into the `b` occurrences.
For each `a` index `i`, discard `b` indices smaller than `i - k`.
The first remaining index is the closest possible candidate on or to the right
of that lower boundary. If it is at most `i + k`, then `i` is beautiful.

Both occurrence lists and the answer are already ordered. The pointer never
moves backward, so each occurrence participates in only constant pointer work.

## Complexity detail

The patterns have contract-bounded length at most 10. Finding their occurrences
and merging the two lists therefore takes $O(N)$ time. The occurrence lists and
output use $O(N)$ auxiliary space.

## Alternatives and edge cases

- **Binary search per `a` occurrence:** Searching the sorted `b` positions works in $O(N\log N)$ time but is unnecessary.
- **Nested proximity checks:** Comparing every `a` start with every `b` start can require $O(N^2)$ time.
- **Rolling hash or KMP:** General linear string matchers are valid, though the pattern-length bound makes direct substring search sufficient.
- **Overlapping matches:** Advance occurrence discovery by one index so no valid start is skipped.
- **Inclusive distance:** A start exactly `k` positions away qualifies.
- **Same patterns:** The same occurrence may witness both `a` and `b`.
- **No nearby occurrence:** Such an `a` index is omitted without affecting later indices.
