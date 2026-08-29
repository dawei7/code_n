## General

**Track only the first missing video**

The longest uploaded prefix has length $r$ when every video from 1 through $r$ has been uploaded but video $r+1$ has not. This suggests maintaining the boundary directly rather than recomputing the prefix from video 1 after every call.

The class stores two pieces of state:

- `self.s` is the set of all uploaded video numbers.
- `self.r` is the current length of the longest uploaded prefix.

The constructor initializes `r` to zero because no videos have been uploaded yet. The input `n` is not stored by the exact implementation. It does not need the upper bound during normal operations because every uploaded number is guaranteed to lie from 1 through $n$, and the set itself records the relevant events.

**What happens during an upload**

Calling `upload(video)` first adds the number to `self.s`. A set supports expected constant-time membership checks and does not depend on upload order.

The loop then asks whether `self.r + 1` is present. That number is the only video that can extend the current prefix. If it has been uploaded, the prefix grows by one and `r` increments. The loop immediately checks the new next number, because it may have been uploaded earlier while the prefix was blocked.

For example, after uploading video 3 first, the set is `{3}` but `r` remains 0 because video 1 is absent. Uploading video 1 advances `r` to 1 and stops because video 2 is absent. Uploading video 2 then advances from 1 to 2; the loop checks video 3, finds the previously uploaded value, and advances again to 3. A single upload can therefore release an entire waiting consecutive run.

Videos greater than `r + 1` are remembered but cannot change the answer immediately. This is correct because any missing smaller number breaks the definition of a prefix regardless of how many later videos are available.

**The maintained invariant**

After construction and after every completed `upload` call, the following facts hold:

1. Every integer from 1 through `self.r` belongs to `self.s`.
2. `self.r + 1` does not belong to `self.s`, unless `r` has already reached $n$ and there is no legal next video.

Initially the first statement is vacuously true for an empty range, and video 1 is not in the empty set. During an upload, adding a value cannot make any already uploaded prefix position disappear. Every loop increment is performed only after confirming the new boundary video is in the set, so the first fact remains true. The loop stops precisely when the next required number is missing; if it continues, it repeats the same argument for the following position.

These facts prove maximality. The first says that `r` is a valid uploaded prefix length. The second says that no longer prefix can exist, because every longer prefix would have to include the missing video `r+1`. Therefore `r` is exactly the longest uploaded prefix.

**Why `longest` is constant-time**

The `longest` method simply returns `self.r`. All work required to keep the answer current was already performed by `upload`. It does not scan the set, sort uploads, or revisit the prefix from the beginning.

This division of responsibility is valuable because the operation sequence may contain many `longest` calls. A query remains $O(1)$ even after $10^5$ uploads.

**Why the loop is efficient over the full sequence**

One particular call to `upload` can execute the loop many times. It might appear that this makes uploads expensive, but `self.r` only increases and never decreases. Each successful loop iteration permanently advances past one video number. Across the lifetime of an object, there can be at most $n$ such increments.

Thus the cost is best understood amortized over all calls. Some uploads merely insert into the set and do no loop work; an upload that closes a gap may pay for many increments, but those increments will never be repeated by later calls.

The constraints say upload values are distinct. The set would also harmlessly absorb a duplicate because adding an existing member changes nothing, although duplicate calls are outside the promised input. The monotonic boundary would still remain correct.

## Complexity detail

Let $q$ be the total number of method calls and $u$ the number of uploads, with $u \le n$. Set insertion and membership are expected $O(1)$ each. Across all uploads, the boundary loop succeeds at most $n$ times, while each upload can cause at most one final failed membership check. Therefore all updates together take expected $O(u+n)$ time. Every `longest` call takes $O(1)$, giving $O(n+q)$ total time over the entire operation sequence, as stated by the manifest.

Equivalently, `upload` has expected amortized $O(1)$ time because the total $O(n)$ advancement work is spread across at most $n$ distinct uploads. Its worst-case time for one isolated call is $O(n)$ when that call fills the one missing gap before a long uploaded suffix.

The set stores at most $n$ video numbers, so space is $O(n)$. The boundary integer takes $O(1)$ additional space. The constructor does not allocate an $n$-element boolean array and does not retain `n`, but the set reaches the same linear worst-case bound after all videos are uploaded.

## Alternatives and edge cases

- **Boolean array:** Store one flag per video and advance the same persistent boundary while the next flag is true. It has deterministic $O(1)$ access and $O(n)$ space, but requires allocating the full array immediately.
- **Disjoint-set union:** Uploaded adjacent positions can be joined into intervals, and the interval containing 1 gives the answer. This is more machinery than needed because a single monotone boundary already captures the prefix.
- **Min-heap of uploads beyond the boundary:** A heap can expose the smallest waiting video, but membership and stale handling complicate the logic. A set directly answers whether the exact next number is available.
- **Recompute from video 1 on every query:** This makes `longest` potentially $O(n)$ per call and repeats work. Persisting `r` makes queries constant-time.
- **Out-of-order uploads:** Later videos remain in the set until earlier gaps close. The loop can then advance through them without new uploads.
- **First upload is not video 1:** The boundary stays zero, correctly representing that no non-empty prefix exists.
- **Uploading video 1:** The prefix becomes at least 1 and may jump farther if videos 2 onward were already uploaded.
- **All videos uploaded:** The loop advances `r` to $n$. The next membership test checks $n+1$, which is absent under the contract, and stops safely.
- **Single video stream:** Construction reports 0; uploading video 1 advances to 1; every later query returns 1.
- **Repeated queries:** They do not mutate state and always return the current boundary immediately.
- **Distinct-upload guarantee:** It ensures at most $n$ upload calls with new values. The set representation nevertheless makes accidental duplicate uploads idempotent.
