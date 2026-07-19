## General
**Store histories by index rather than arrays by snapshot.** Give every index a chronological list of `[snap_id, value]` records, initialized with value `0` at snapshot ID `0`. Unchanged indices then consume no additional storage when a snapshot is taken.

**Coalesce changes made before the same snapshot.** `set(index, val)` associates the new value with the current snapshot counter. If the last record for that index already has this counter, replace its value; otherwise append a new record. Calling `snap()` merely returns the current counter and increments it, so both operations take constant time.

**Find the last change visible to a historical read.** Records for an index have increasing snapshot IDs. Binary search for the rightmost record whose ID is at most the requested `snap_id`; that record is exactly the most recent assignment included in the snapshot. The initial zero record guarantees that this predecessor always exists. Later assignments carry larger IDs and therefore cannot affect the result.

## Complexity detail
Each `set` and `snap` takes $O(1)$ time, while `get` takes $O(\log u)$ time for the queried index's $u$ records. Across $q$ operations this is $O(q\log u)$ in the worst case. The initial history for every array position uses $O(\texttt{length})$ space, and the effective change records add $O(s)$ space.

## Alternatives and edge cases
- **Copy the full current array on every snapshot:** Historical reads become $O(1)$, but each `snap` costs $O(\texttt{length})$ time and total storage can grow to the product of the length and number of snapshots.
- **Store a full map for every snapshot:** Sparse maps still duplicate unchanged state unless they are linked through a persistent structure, making the simple per-index histories more direct.
- **Repeated sets before `snap`:** Only the last value belongs to that snapshot, so overwriting one record prevents redundant history entries.
- **Never-set index:** Its initial record returns `0` for every valid snapshot.
- **Empty snapshots:** Consecutive `snap` calls without updates receive distinct IDs but share all previously stored values.
- **Read after later updates:** Binary search ignores records whose IDs exceed the requested `snap_id`.
