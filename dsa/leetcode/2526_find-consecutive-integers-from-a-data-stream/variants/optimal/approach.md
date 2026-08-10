## General

**Only the trailing run matters**

After each new stream value, the question asks whether the last `k` parsed integers all equal `value`.

There is no need to remember the full stream or even the last `k` items. It is sufficient to know the length of the current consecutive run of `value` at the stream's end.

If that trailing run has length at least `k`, then the last `k` elements are all `value`. If it is shorter, some position among the last `k` is missing or contains a different value.

**Persistent object state**

The constructor stores:

- `self.val`: the target value;
- `self.k`: required trailing length;
- `self.cnt`: current trailing run length, initially zero because the stream is empty.

These fields persist across calls to `consec`. A local variable would be lost after each call and could not describe the accumulated stream.

**Update on a matching number**

If incoming `num` equals `self.val`, it extends the existing trailing run by one:

`self.cnt+1`.

For three consecutive target values, the counter progresses 1, 2, 3. Once it reaches `k`, the method returns true.

Additional target values keep increasing the counter. Returning `self.cnt>=self.k` remains true because the last `k` positions of a longer matching run are still all targets.

Testing equality `==k` would be wrong after the run grows beyond `k`.

**Reset on a mismatch**

If `num!=self.val`, the newest stream element itself is not the target. No positive-length suffix ending at it can consist entirely of target values, so the trailing target run becomes zero.

The conditional expression implements both cases:

`self.cnt=0 if num!=self.val else self.cnt+1`.

A later target begins a fresh run from one.

**Why fewer than `k` parsed values return false**

The counter can never exceed the total number of calls so far. Before `k` calls, `self.cnt<k` automatically, so the comparison returns false without maintaining a separate stream-length field.

This also covers streams with early mismatches.

**Trace the sample**

With target 4 and `k=3`:

- first 4 sets `cnt=1` and returns false;
- second 4 sets `cnt=2` and returns false;
- third 4 sets `cnt=3` and returns true;
- incoming 3 resets `cnt=0` and returns false.

These states correspond exactly to the trailing target runs after each append.

**A precise invariant**

After every call, `self.cnt` equals the largest integer $r\ge0$ such that the last $r$ stream elements are all equal to `self.val`.

The invariant is true initially with an empty stream and $r=0$. A matching new value extends the maximal suffix by one. A mismatch forces the only matching suffix length to zero. Induction proves the invariant for all calls.

Given the invariant, the returned comparison is true exactly when the trailing suffix contains at least `k` target values, which is equivalent to the last `k` elements all matching.

**Why no queue is needed**

A queue of the last `k` values could answer the question, but it stores information that becomes irrelevant. Every mismatch makes all earlier elements unusable for a trailing all-target block, so resetting one counter summarizes the complete relevant history.

**Different large integer values**

The algorithm uses equality only. Numeric magnitude up to $10^9$ has no effect on time or storage, and there is no arithmetic overflow risk.

**Multiple objects**

Each `DataStream` instance has its own target, length requirement, and counter. Calls on one object do not affect another because state is stored on `self`.

**Why the exact previous run length is enough**

Assume the prior trailing target run has length $r$. If the new value matches, every one of those $r$ elements is still immediately before the new target, so the new maximal run is $r+1$. If it differs, the final element fails the target test, so even a suffix of length one cannot qualify and the new run is zero.

Those are the only two input cases. Nothing earlier than the prior run boundary can become relevant again, which proves that discarded stream history can never affect a future answer.

## Complexity detail

Each `consec` call performs one comparison, one assignment, and one threshold test, taking $O(1)$ time.

Across `q` calls, total time is $O(q)$.

The object stores three integers regardless of stream length, so auxiliary space is $O(1)$. The stream itself is never retained.

## Alternatives and edge cases

- **Queue of last `k` values:** It works but uses $O(k)$ memory and more updates.
- **`k=1`:** Return true exactly when the current number equals the target.
- **Run longer than `k`:** Continue returning true; use `>=` rather than equality.
- **Mismatch after success:** Reset immediately and return false.
- **New run after mismatch:** The first matching value sets the count to one.
- **Fewer than `k` calls:** Counter cannot reach the threshold.
- **Target never appears:** Every call leaves or resets the counter to zero.
- **All values match:** Results become true starting with call `k`.
- **Persistent state:** Constructor fields must survive between method calls.
- **No stream storage:** The trailing-run invariant is sufficient.
