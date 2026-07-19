## General
**Index intervals from both endpoints**

An inserted value can interact only with intervals ending at `value - 1` or starting at `value + 1`. Keep a set of all present values for duplicate and neighbor checks, a map from every interval start to its end, and a reverse map from every interval end to its start.

**Classify the four possible local updates**

For a new value, four cases cover every possible update:

- Neither neighbor exists: create `[value, value]`.
- Only `value - 1` exists: extend its interval's right endpoint to `value`.
- Only `value + 1` exists: extend its interval's left endpoint to `value`.
- Both exist: join the left and right intervals through `value`.

**Why immediate neighbors reveal the endpoints**

The neighbor facts are enough to locate endpoints. If `value` is absent but `value - 1` is present, then `value - 1` must be the right endpoint of its interval; otherwise that interval would already contain `value`. The symmetric statement holds for `value + 1`. Endpoint maps therefore retrieve both affected intervals in expected constant time.

**Why maximal disjoint intervals are preserved**

After each update, the maps contain disjoint maximal intervals: the only new adjacency involving an old interval can pass through the inserted value, and the four cases merge every such adjacency immediately. No other intervals change. The present set prevents duplicates from applying an update twice. Sorting the start-map keys during `getIntervals()` yields the required order without affecting the maintained partition.

## Complexity detail
`addNum` performs expected $O(1)$ hash operations. If `k` intervals currently exist, `getIntervals` sorts their starts in $O(k \log k)$ time and emits $O(k)$ pairs. With `v` distinct stream values, the presence set uses $O(v)$ space and the endpoint maps use $O(k)$, so total space is $O(v)$.

## Alternatives and edge cases
- **Sorted interval array:** keeps queries ordered but may shift $O(k)$ interval entries during insertion or deletion.
- **Rebuild from all seen values:** costs $O(v \log v)$ for every snapshot after sorting `v` values again.
- **Balanced ordered map:** provides $O(\log k)$ insertion and ordered queries, but Python's standard library has no built-in implementation.
- Adding a duplicate is a no-op.
- Adding the one missing value between two intervals must merge both intervals, not merely extend one.
- Zero and isolated values become ordinary singleton intervals.
