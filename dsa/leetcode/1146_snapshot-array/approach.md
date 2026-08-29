## General

**Store changes instead of copying the whole array**

A literal snapshot implementation could keep a current array and copy all `length` values whenever `snap()` is called. That makes one snapshot expensive even if only one index changed. With up to 50,000 operations and a length up to 50,000, copying full arrays can waste both time and memory.

The optimal design reverses the viewpoint. Each array index keeps only its own write history. `self.arr[index]` is a chronological list of pairs

`(snapshot_id_at_write, value)`.

If an index is never written, its history remains empty and its value is known to be the initial zero for every snapshot. If it is written only a few times, only those few changes are stored no matter how many snapshots are taken.

The constructor creates one empty history list for every valid index and sets `self.i = 0`. This counter is the identifier that the next call to `snap` will return. It is also the version attached to any `set` calls made before that snapshot.

**Record writes under the current pending snapshot**

`set(index, val)` appends `(self.i, val)` to the selected index's history. It does not increment the snapshot counter. Therefore, every write between two calls to `snap` receives the same identifier.

Multiple writes to the same index before a snapshot are all appended. The last such pair must determine the snapshotted value. The retrieval binary search is deliberately designed to choose the last record with a version no greater than the requested identifier, so earlier writes carrying the same identifier are harmless.

An optional implementation could overwrite the last record when its identifier equals `self.i`, saving some space. The exact solution does not do that; it keeps one pair per `set` call. This remains within the operation limit and preserves correct ordering.

**A snapshot is only a version boundary**

`snap()` increments `self.i` and returns `self.i - 1`. If the counter was zero, writes so far belong to version zero, the counter becomes one, and the returned snapshot identifier is zero. Future writes then receive version one and cannot alter retrieval from version zero.

No array data is copied during `snap`. All histories already contain the changes that define the version being closed. Advancing the counter is sufficient to separate later changes from the saved state, so both increment and return take constant time.

**Retrieve the latest write visible to a snapshot**

To answer `get(index, snap_id)`, the value must come from the latest write at that index whose recorded version is at most `snap_id`. The per-index list is sorted by version automatically because `self.i` never decreases and records are appended in operation order.

The code performs

`bisect_left(self.arr[index], (snap_id, inf)) - 1`.

Python compares tuples lexicographically. Every real value is finite and no greater than `10^9`, so a stored pair `(snap_id, val)` is smaller than `(snap_id, inf)`. The binary-search insertion point is therefore after every record whose first component equals `snap_id`, including multiple sets in the same version. It is also after all records with smaller versions and before every record with a larger version.

Subtracting one selects exactly the rightmost pair whose version is at most the requested version. This is the last applicable write and hence the value visible in that snapshot.

If the resulting position is negative, no write to this index occurred at or before `snap_id`. The array was initialized with zeros, so the correct result is zero. Otherwise, `self.arr[index][i][1]` extracts the stored value from the selected pair.

**Trace the sample operations**

After construction, every history is empty and `self.i` is zero. Calling `set(0, 5)` appends `(0, 5)` to index zero. The first `snap()` changes the counter to one and returns zero.

The later call `set(0, 6)` appends `(1, 6)`. A query for index zero at snapshot zero searches for the last version no greater than zero and selects `(0, 5)`. The version-one write is correctly excluded even though it is the latest current value.

If two calls such as `set(0, 5)` and `set(0, 7)` occur before the same first snapshot, the history contains `(0, 5)` followed by `(0, 7)`. Searching with `(0, inf)` lands after both, and subtracting one selects seven, matching ordinary array assignment semantics.

**Why the data structure is correct**

For each index, its history lists all writes in nondecreasing snapshot-ID order. A snapshot with identifier `s` includes exactly the writes performed while the current counter was at most `s` and excludes every write performed after the counter advanced beyond `s`.

Among the included writes for one index, the last operation determines the array's value. The binary search returns precisely that last included record. If the included set is empty, the initial value is zero. Thus every `get` returns the value that the index had when the requested snapshot was taken.

The histories are independent because a `set` changes only one index. This makes it unnecessary to materialize complete versions or replay unrelated changes during a query.

## Complexity detail

Let `u` be the number of stored `set` records for the queried index, let `s` be the total number of `set` calls across all indices, and let `length` be the initialized array length.

Constructing the outer list and its empty histories takes `O(length)` time and space. A `set` call performs an append, which is amortized `O(1)` time. A `snap` call updates one counter and is `O(1)` time.

A `get` call binary-searches one history of length `u`, taking `O(log u)` time. The final index check and value access are constant time. The manifest's `O(log u)` time describes this nonconstant query operation; the update and snapshot operations are faster.

There is one empty list per index and one stored pair per `set` call. Total storage is `O(length + s)`. The binary search itself uses `O(1)` auxiliary space.

Repeated sets within the same pending snapshot are not coalesced by the exact code, so each one contributes to `s` and to that index's `u`. This is already reflected in the bounds.

## Alternatives and edge cases

- **Copy the full array at every snapshot:** Retrieval becomes direct indexing, but every `snap` costs `O(length)` time and every saved version stores `length` values, even when almost nothing changed.
- **Global change log:** One chronological log avoids per-index lists, but retrieving one index may require scanning or more complex indexing. Per-index histories make each query search only relevant writes.
- **Hash map keyed by snapshot and index:** It can store changes sparsely, but finding the latest earlier version requires backward probing or another ordered structure. Sorted histories support binary search naturally.
- **Overwrite a same-version last record:** If the last pair for an index already has `self.i`, replacing its value would reduce storage while preserving behavior. The exact solution instead appends and relies on the rightmost binary-search result.
- **Index never set:** Its history is empty, the binary-search result is negative, and `get` correctly returns the initial zero.
- **First snapshot with no sets:** `snap` still returns zero. Every index queried at snapshot zero returns zero.
- **Several snapshots without changes:** No new history records are needed. Queries at each new identifier find the same latest earlier write.
- **Several sets before one snapshot:** All receive the same ID, and tuple search with `inf` selects the last appended value for that ID.
- **A value explicitly set to zero:** A real zero record is stored and returned like any other value. It is semantically indistinguishable from the initial value but still correct.
- **Query an older snapshot after many writes:** Binary search ignores every record with a larger ID and retrieves historical state without undoing later changes.
- **Valid snapshot IDs only:** The contract guarantees `snap_id` refers to an already taken snapshot. The implementation does not need to validate future or negative IDs.
- **Why `inf` is safe:** Legal values are finite and bounded, so `(snap_id, inf)` sorts after every record for the requested version, ensuring last-write-wins behavior.
