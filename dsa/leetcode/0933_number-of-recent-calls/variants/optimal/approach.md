## General

**The data that a call needs**

Each call `ping(t)` must return how many recorded requests have timestamps in the inclusive interval `[t - 3000, t]`. The timestamps arrive in strictly increasing order. That ordering guarantee is the key to the optimal solution.

At the moment a new timestamp arrives, it is later than every stored timestamp. Any old timestamp smaller than `t - 3000` is now outside the requested window. More importantly, it can never become relevant again: every future timestamp will be still larger, so every future lower boundary will be at least as large as the current lower boundary.

The algorithm can therefore permanently discard expired requests. It needs to retain only the timestamps in the current sliding time window.

**Why a deque matches the operations**

Because calls arrive in increasing order, the retained timestamps are sorted from oldest at the front to newest at the back. Every new timestamp belongs at the back. Every expired timestamp, if one exists, must be among the oldest values at the front.

A deque supports both needed operations efficiently:

- `append(t)` adds the new, largest timestamp to the back;
- `popleft()` removes an expired, smallest timestamp from the front.

A regular Python list can append efficiently, but removing index zero shifts every remaining element and costs linear time. The deque avoids those repeated shifts.

**The exact order inside `ping`**

The method first executes `self.q.append(t)`. This is important for two reasons. The current request belongs to its own interval because `t` is at the inclusive upper boundary, so it must be counted. Appending first also guarantees that the deque is nonempty before the code reads `self.q[0]` in the loop condition.

Next, the loop checks `self.q[0] < t - 3000`. If the oldest timestamp is strictly below the lower boundary, it is outside the inclusive interval and is removed. The loop repeats because several old calls may expire at once.

The comparison must be strict. A request at exactly `t - 3000` is inside `[t - 3000, t]` and must remain. Replacing `<` with `<=` would incorrectly discard a boundary request.

Once the oldest timestamp is not below the lower boundary, every later timestamp is also at least that large because the deque is sorted. No additional element can be expired. The method returns `len(self.q)`, which is exactly the number of requests still in the window.

**A trace that exposes the inclusive boundary**

Consider calls at times `1`, `100`, `3001`, and `3002`.

- After `ping(1)`, the window is `[-2999, 1]` and the deque is `[1]`, so the answer is `1`.
- After `ping(100)`, the window is `[-2900, 100]` and both `1` and `100` remain, so the answer is `2`.
- After `ping(3001)`, the lower boundary is `1`. Timestamp `1` is exactly on the boundary and remains. The deque is `[1, 100, 3001]`, so the answer is `3`.
- After `ping(3002)`, the lower boundary is `2`. Timestamp `1` is now too old and is removed. Timestamp `100` is valid, so removal stops and the deque becomes `[100, 3001, 3002]`. The answer is `3`.

Only the front needs examination. Looking at every stored timestamp would reproduce the correct answer but throw away the benefit of sorted arrival.

**The maintained invariant**

After every completed call, the deque contains exactly the timestamps of all calls in that call's interval `[t - 3000, t]`, in increasing order.

Initially the deque is empty, which is correct before any calls. For a new call, appending `t` preserves increasing order because timestamps are strictly increasing, and the new timestamp is valid. The loop removes every timestamp below the new lower boundary. It cannot remove a valid timestamp because it uses a strict comparison, and when it stops, the front is valid. Sorted order then guarantees that everything behind the front is also valid. Previously removed timestamps remain invalid because the lower boundary never moves backward. The invariant therefore holds after every call, and the returned deque length is the requested count.

**Why expired timestamps never need to be remembered**

Suppose a timestamp `s` is removed while processing `t`, so `s < t - 3000`. Any future timestamp `u` satisfies `u > t`. Therefore `u - 3000 > t - 3000`, which means `s` is also below the future lower boundary. Discarding `s` loses no information needed by a later answer.

This monotonicity is what turns the deque into more than a convenient container. It proves that a one-way stream of additions and removals is sufficient.

## Complexity detail

Let `m` be the total number of calls made to `ping`.

A single call may remove many timestamps, so its individual worst-case running time is `O(m)`. For example, one large jump in `t` can expire almost the entire deque. Across the complete sequence, however, each timestamp is appended exactly once and removed at most once. There are at most `m` appends and `m` removals, plus constant work per call. The total time for `m` calls is `O(m)`, which gives amortized `O(1)` time per call.

The deque contains only requests in the active 3000-unit window. In the worst case, all `m` calls can fit in that interval because the contract makes timestamps strictly increasing but does not require a large gap between them. Thus worst-case auxiliary space is `O(m)`. More precisely, at any instant the space is proportional to the number of calls in the current window.

## Alternatives and edge cases

- **Scanning an array of all timestamps:** Append every call and count values in the range each time. This is simple but can cost `O(m)` per call and `O(m^2)` across the full sequence.
- **Array plus a moving start index:** Keep every timestamp in a list and advance an index past expired values. This also gives amortized `O(1)` query time, but old entries remain allocated unless the list is occasionally compacted. The deque naturally releases them.
- **Binary search over all timestamps:** Since arrival order is sorted, binary search can find the first valid timestamp in `O(log m)` time. It retains every historical call and is slower than the deque's amortized constant time.
- **Balanced tree or ordered multiset:** Such a structure supports general insertions and range counts, but it is unnecessary because timestamps arrive in a much stronger order. It adds logarithmic overhead and implementation complexity.
- **Timestamp exactly at `t - 3000`:** It is valid and must stay. This is the central reason for using `<` rather than `<=` in the expiration test.
- **A very large jump in time:** Many values may be popped in one call. The current timestamp remains because it was appended first and can never be smaller than its own lower boundary.
- **Safety of reading the front:** `self.q[0]` cannot fail inside `ping` because the method appends `t` before entering the loop, and that newly appended value is never expired.
- **Strictly increasing timestamps:** The correctness and efficiency rely on this contract. If timestamps could arrive out of order, expired values would not necessarily form a prefix and a deque alone would not be sufficient.
- **Duplicate timestamps:** The stated contract excludes them. If nondecreasing timestamps were allowed, the same deque mechanics would still count duplicates correctly, but that is not the interface guarantee being used.
- **Inclusive upper boundary:** The new request at `t` is always counted. Appending before returning the length handles this automatically.
