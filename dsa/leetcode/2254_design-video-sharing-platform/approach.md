## General

**Store each active video and its counters together**

`self.videos` maps each active `videoId` to a four-entry mutable record:

`[videoText, views, likes, dislikes]`.

Keeping all state for one ID together makes successful operations expected constant-time dictionary lookups, aside from copying watched substring content.

Deleted IDs are absent from this dictionary. Membership is therefore the authoritative existence check for every method.

**Maintain the smallest reusable ID**

Two fields coordinate allocation:

- `self.next_id` is the smallest ID that has never been assigned;
- `self.available_ids` is a min-heap of IDs that were assigned and later removed.

On upload, if the heap is nonempty, `heapq.heappop` returns its smallest deleted ID. Otherwise, the method uses `next_id` and increments it for the future.

This always gives the globally smallest available ID. Every heap entry is below `next_id` because it was previously assigned. If any deleted ID exists, the heap minimum is smaller than every never-used ID. If none exists, all IDs below `next_id` are active, making `next_id` the smallest available.

The new dictionary record initializes views, likes, and dislikes to zero. Reusing an ID does not inherit the deleted video's statistics.

**Removal releases an ID exactly once**

`remove` first checks whether `videoId` is active. If so, it deletes the dictionary entry and pushes the ID into the reusable heap.

Calling `remove` again on the same absent ID does nothing, so duplicate heap entries cannot be created. This matters because duplicate reuse entries could assign one ID to multiple uploads.

Removing an unknown ID has no effect on any state.

**Watch only active videos**

If `videoId` is absent, `watch` returns the string `"-1"` and does not increment a counter.

For an active record, it increments `record[1]` before returning:

`record[0][startMinute : endMinute + 1]`.

Python slices exclude their right endpoint, so adding one makes `endMinute` inclusive. If `endMinute` exceeds the video's last index, Python automatically truncates the slice at string length, exactly matching the required `min(endMinute, video.length - 1)` behavior.

Every successful call counts one view regardless of returned substring length. The start position is guaranteed valid by the contract.

**Likes and dislikes are guarded mutations**

`like` increments record index two only when the ID exists. `dislike` similarly increments index three. Calls on absent IDs do nothing.

The counters are independent: liking does not change views or dislikes, and watching changes only views.

**Queries return the required shapes**

`getLikesAndDislikes` returns `[-1]` for an absent ID. For an active record, `record[2:4]` returns a new two-element list `[likes, dislikes]`. Returning a slice prevents the caller from receiving the full mutable internal record.

`getViews` returns `-1` when absent and record index one when active.

The string sentinel from `watch` and integer/list sentinels from the other methods match their distinct contracts.

**Persistent-state invariants**

At all times:

- an ID is either an active key, a reusable heap entry, or a never-used value at least `next_id`;
- no ID belongs to two of those categories;
- every active record has exactly one text and three nonnegative counters;
- the heap contains no duplicate released ID.

Constructor state satisfies these properties. Upload moves an ID from reusable or never-used into active. Removal moves one active ID to reusable. Other methods change only counters. Therefore, the invariants persist across any valid call sequence.

**Trace ID reuse**

Uploads initially receive zero and one. Removing zero deletes its record and pushes zero. The next upload sees a nonempty heap, pops zero, creates a fresh record, and returns zero. ID one remains associated with its original video and statistics.

If IDs two and zero are later removed, heap order ensures zero is reused before two.

**No stale state survives deletion**

Deleting the dictionary record removes its video text and counters. When the ID is reused, assignment overwrites with a new `[video,0,0,0]` record. Queries between deletion and reuse see the ID as absent.

## Complexity detail

Let `A` be the number of reusable IDs currently in the heap and `L` the length of a returned watch substring. Upload with reuse and successful removal take `O(\log A)` heap time; upload without reuse is `O(1)` apart from storing the video reference.

Dictionary membership, likes, dislikes, and scalar queries are expected `O(1)`. `watch` takes `O(L)` to create its returned substring.

Across `Q` calls and total returned/stored content volume `C`, the manifest summarizes time as `O(Q \log Q + C)`.

Active video strings occupy `O(U)` total content space. The dictionary and reusable heap contain `O(Q)` records or IDs over the call history, giving `O(U + Q)` space.

## Alternatives and edge cases

- **Scan upward from ID zero on every upload:** It finds the smallest free ID but can take linear time per upload; the heap retrieves released minima efficiently.
- **Use only a monotonically increasing ID:** Deleted IDs would never be reused, violating the contract.
- **Reuse IDs with a stack or queue:** Neither guarantees the smallest available ID; a min-heap does.
- **Push on every remove call:** Repeated removal would duplicate heap entries. Membership guarding is essential.
- **Mutate counters before existence check:** Invalid operations must have no effect.
- **Watch beyond video end:** Python slicing truncates automatically at the correct final character.
- **Inclusive end minute:** `endMinute + 1` converts the inclusive contract to Python's exclusive slice endpoint.
- **Removed then queried:** All query methods return their specified missing-ID sentinel.
- **Reused ID:** New counters start at zero and old content is gone.
- **Duplicate videos:** Text equality does not matter; each upload receives its own ID and record.
- **Repeated arrival of same call:** Every successful watch increments views once; every valid like or dislike increments its own counter once.
- **Returned likes list:** Slicing produces only the two requested values, not the internal video record.
