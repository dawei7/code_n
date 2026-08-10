## General

The object must summarize every distinct value seen so far, but it does not need to retain every value separately. Consecutive values can be compressed into one closed interval. For example, after seeing `1`, `2`, `3`, `6`, and `7`, the complete set is represented by `[[1, 3], [6, 7]]`.

The exact solution maintains those disjoint intervals continuously inside a `SortedDict`. Each dictionary entry has a numeric key used for ordered searching and a mutable two-element value `[start, end]` containing the interval's actual boundaries. Because entries stay ordered, a newly added number can interact only with the interval immediately to its left and the interval immediately to its right.

**Why only neighboring intervals matter.**

Assume the current intervals are sorted and disjoint, with at least one missing integer between consecutive intervals. When adding `val`, an interval farther left than the immediate predecessor ends no later than that predecessor, so it cannot touch `val` if the predecessor does not. The same argument applies to intervals farther right. Therefore the update has only five meaningful outcomes:

- `val` already lies in an interval, so nothing changes.
- `val` is exactly one greater than the left interval's end, so that interval extends right.
- `val` is exactly one less than the right interval's start, so that interval extends left.
- Both adjacency conditions hold, so `val` bridges two intervals into one.
- Neither side contains or touches `val`, so `[val, val]` becomes a new interval.

This local-neighbor fact is what makes an ordered map useful. Rebuilding all intervals after every insertion would discard work that earlier calls already completed.

**Locating the two relevant entries.**

Let `n` be the current number of interval entries. `bisect_right(val)` returns `ridx`, the position after every dictionary key less than or equal to `val`. The entry at `ridx`, when it exists, is the immediate key to the right. If `ridx` is not zero, the entry at `ridx - 1` is the immediate key on the left. The code stores that latter index as `lidx`; when no left entry exists, it uses `n` as a sentinel meaning “absent.”

`keys = self.mp.keys()` and `values = self.mp.values()` are aligned ordered views. At a given index, `keys[index]` is the map key and `values[index]` is that entry's `[start, end]` list.

There is a subtle implementation detail: when an interval is extended to the left, the source changes the first number inside its stored list but does not replace its `SortedDict` key. Thus a map entry might have key `7` and stored interval `[5, 9]`. The key is an ordered search anchor inherited from when the interval was created, not always the current `start`. This is unusual, but the branch logic continues to consult the actual endpoints in `values`, and extensions cannot pass across a previous interval without triggering a merge. Consequently, the anchor ordering remains sufficient for locating the neighboring interval groups.

**Case 1: bridge the left and right intervals.**

The first condition requires both neighbors to exist. It then checks whether the left interval ends at `val - 1` and the right interval starts at `val + 1`. If so, the new number fills the only gap between them.

The solution changes the left interval's end to the right interval's end, then removes the right entry. For example, adding `2` to `[1, 1]` and `[3, 4]` produces `[1, 4]`. Keeping both old entries would violate disjoint maximal representation, so removing the right one is essential.

This branch is checked first because extending only one side would miss the simultaneous merge. It also reduces the interval count by one.

**Case 2: belong to or touch the left interval.**

If bridging did not occur, the next branch checks `val <= left_end + 1`. When `val` is inside the left interval, `max(val, left_end)` leaves its endpoint unchanged; this handles duplicate additions without a separate early return. When `val == left_end + 1`, the maximum becomes `val`, extending the interval by one.

Values cannot create a valid jump over a missing integer. If `val` is more than one beyond the left endpoint, this branch correctly fails.

**Case 3: touch or already belong to the right interval.**

If the left case fails and a right entry exists, the source tests `val >= right_start - 1`. Because `ridx` was found by ordered bisection, this covers the adjacent-right case and can also harmlessly handle a duplicate that lies in an interval whose actual start has previously moved left of its stored key. The new start becomes `min(val, right_start)`, so an existing interior value leaves the interval unchanged while an adjacent value extends it left.

The map key is not changed in this branch. As noted above, the stored value is the authoritative interval returned to the caller, while the old key continues to serve as its ordered anchor.

**Case 4: create a singleton.**

If neither neighbor contains or touches `val`, the value is isolated from every existing interval. The assignment `self.mp[val] = [val, val]` creates a new ordered-map entry. Since `val` lies in a genuine gap, this preserves both disjointness and sorted order.

**Why the representation remains complete and correct.**

Initially the map is empty, accurately representing an empty stream. Assume before an addition that every seen value belongs to exactly one stored interval, every integer inside each interval has been seen, and separate intervals have at least one unseen integer between them.

The new value can affect only its immediate neighbors. Each branch either leaves an already represented value unchanged, expands one interval by exactly the adjacent new value, joins two intervals through the new value, or creates a singleton. None introduces an unseen integer, loses an old value, or leaves two adjacent intervals separate. Thus the same properties hold after the call. By repetition, they hold after every stream update.

`getIntervals` returns `list(self.mp.values())`. Since the `SortedDict` iterates entries in key order and the anchors preserve interval order, the output is sorted by actual starts. The outer list is newly allocated, though the contained interval lists are the stored mutable objects rather than deep copies.

**The exact source differs substantially from the manifest summary.**

The manifest describes paired endpoint hash maps with constant-time addition and sorting during retrieval. The source instead uses a balanced sorted mapping, performs ordered bisection on every addition, and already maintains output order. It does not maintain separate endpoint maps. Therefore its per-operation complexity is ordered-map complexity, not the advertised $O(1)$ update and $O(k\log k)$ retrieval pattern.

## Complexity detail

Let $k$ be the current number of disjoint intervals and let $v$ be the number of distinct stream values seen so far. Always $k\le v$.

`bisect_right` on a `SortedDict` takes $O(\log k)$ time. Accessing positional keys or values and updating an interval list have logarithmic or constant costs depending on the internal sorted-container operation, while inserting or removing a map entry takes $O(\log k)$. Only a constant number of such operations occurs per call. Therefore `addNum` takes $O(\log k)$ time, including duplicates because the ordered search is still performed.

`getIntervals` walks the $k$ ordered values and constructs an outer Python list, so it takes $O(k)$ time. No sorting is performed at query time. This directly contradicts the manifest's `O(1) / O(k log k)` summary; for this source, the accurate pair is $O(\log k)$ for `addNum` and $O(k)$ for `getIntervals`.

The map stores one entry and one two-integer list per interval, using $O(k)$ persistent space. Since $k\le v$, the manifest's $O(v)$ is a valid but loose upper bound; $O(k)$ explains the compression benefit more precisely. A returned outer list uses $O(k)$ additional references. Because its inner lists are shared with the map, it does not duplicate all endpoint integers into fresh inner arrays.

## Alternatives and edge cases

- **Paired endpoint hash maps:** Track interval boundaries so a new value can find intervals ending at `val - 1` and starting at `val + 1` in expected $O(1)$ time, then sort active intervals during `getIntervals` in $O(k\log k)$. This matches the manifest but is not the checked-in implementation.

- **Store every distinct value in an ordered set:** Addition costs $O(\log v)$, and a query scans all $v$ values to rebuild intervals. It is simpler but wastes query work when many values merge into a few intervals.

- **Boolean presence array:** Since values lie from `0` through `10000`, mark a fixed array and scan the whole domain for each query. Updates are $O(1)$, but queries cost $O(10001)$ even when very few values exist.

- **Duplicate additions:** Adding a value already covered by an interval leaves the endpoints unchanged. The data stream may repeat values, but the summary represents a set of seen integers.

- **Bridge insertion:** A value such as `2` between `[1, 1]` and `[3, 3]` must merge both sides in one call. The source checks this before either one-sided extension.

- **Smallest and largest values:** Values `0` and `10000` need no sentinels outside the domain. Arithmetic comparisons with `-1` or `10001` are safe Python integer operations.

- **Empty object:** Before any addition, `getIntervals()` returns an empty list because the sorted dictionary has no values.

- **One interval after many merges:** Persistent storage is proportional to one interval rather than to every value, which directly addresses the follow-up's “many merges” scenario.

- **Returned intervals are not deep-copied:** Mutating an inner list received from `getIntervals` could corrupt internal state. The judge normally treats returned results as read-only snapshots; a defensive production implementation should return copies such as `[interval[:] for interval in self.mp.values()]`.

- **Stale search anchors:** Extending a right interval leftward changes its stored start but not its map key. The algorithm remains ordered under its own controlled updates, but using actual starts as keys and reinserting on left extension would be a clearer conventional design.
