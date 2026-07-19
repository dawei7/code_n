## General
**Reduce common free time to gaps in busy-time union**

All employees are free exactly when no employee has a busy interval. Flatten the schedules and sort the `N` intervals by start time. Then scan them as one global busy timeline.

**Track the end of the merged busy prefix**

Initialize `current_end` from the first interval. For each later `[start, end]`:

- if `start > current_end`, the positive-length gap `[current_end, start]` is common free time;
- whether or not there was a gap, extend `current_end` to `max(current_end, end)`.

Touching intervals have `start = current_end` and therefore produce no positive-length gap.

After processing any prefix of the sorted intervals, `current_end` is the right boundary of its last merged busy component, and every earlier gap between components has been emitted. The next start either overlaps that component or begins the next one, making the detected gap free of every busy interval. Thus the scan emits exactly all finite gaps in the total busy union.

## Complexity detail
Flattening and scanning take $O(N)$ time, while sorting dominates at $O(N \log N)$. The flattened interval list and returned gaps use $O(N)$ space; the scan itself uses constant auxiliary state.

## Alternatives and edge cases
- **Heap merge of employee schedules:** Push each employee's next interval and merge in chronological order for $O(N \log e)$ time with `e` employees, avoiding a separate flat sort.
- **Repeatedly select the next earliest interval:** This can merge correctly without sorting but costs $O(N^2)$ time.
- **Sweep-line events:** Start and end deltas identify periods with zero active employees, though event sorting has the same $O(N \log N)$ bound.
- **Overlapping or nested busy intervals:** Extend the merged end; they create no free-time boundary.
- **Touching intervals:** A zero-length gap is not returned.
- **One merged busy component:** There is no finite common free interval, so return an empty list.
- **Outside the combined schedule:** Unbounded free time before the first and after the last busy interval is intentionally excluded.
