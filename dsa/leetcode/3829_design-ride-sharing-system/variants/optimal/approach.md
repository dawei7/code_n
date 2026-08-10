## General

**Represent arrival order with a unique timestamp**

The system needs FIFO order independently among riders and among drivers. The source maintains one counter `self.t`. Every addition—rider or driver—receives the current counter value, and the counter then increases.

Since `self.t` never repeats, timestamps encode global arrival order. Using one global clock is stronger than necessary, but it also preserves arrival order within each category: if rider A was added before rider B, A's timestamp is smaller, regardless of driver additions between them.

The source stores:

- `self.riders` as a `SortedList` of `(timestamp, riderId)`;
- `self.drivers` as a `SortedList` of `(timestamp, driverId)`;
- `self.d[riderId]` as the rider's timestamp, used to locate that exact ordered entry during cancellation.

Tuple ordering compares timestamps first. Because timestamps are unique, the first tuple is always the earliest still-available member of that category.

**Add a rider**

`addRider` records the current timestamp in `self.d`, inserts `(timestamp, riderId)` into the ordered rider collection, and increments the clock.

The rider-ID guarantee says each rider is added at most once, so one ID never has two waiting entries. The timestamp dictionary is authoritative only for locating the rider's original tuple; waiting status is represented by whether that tuple still exists in `self.riders`.

**Add a driver**

`addDriver` inserts `(timestamp, driverId)` into `self.drivers` and increments the same clock. Drivers cannot be canceled, so no driver-to-timestamp dictionary is needed.

Rider IDs and driver IDs live in separate namespaces for system behavior. The same numeric value may identify one rider and one driver, as in the second example, without collision because their tuples are stored in different ordered collections.

**Match the two earliest available participants**

`matchDriverWithRider` first checks whether either collection is empty. If even one side has no available participant, no match can be formed. The source returns `[-1, -1]` without removing anything from the nonempty side.

When both collections are nonempty, `pop(0)` removes the lexicographically first tuple from each `SortedList`. Those are the smallest timestamps, hence the earliest waiting rider and earliest available driver.

The return order is driver first and rider second:

`[self.drivers.pop(0)[1], self.riders.pop(0)[1]]`.

The `[1]` tuple component extracts the ID while discarding the no-longer-needed timestamp.

Removing both tuples ensures neither participant can be matched again. The rider's timestamp remains in `self.d`, but a later cancellation only attempts to discard an already-absent ordered tuple and has no effect.

**Cancel a waiting rider exactly**

`cancelRider(riderId)` forms the tuple

`(self.d[riderId], riderId)`

and calls `discard` on the rider collection.

If the rider is still waiting, the exact tuple is removed. Every later rider shifts forward logically, so FIFO matching naturally skips the canceled request.

If the rider has already been matched, the tuple is absent and `discard` does nothing. This implements the requirement that cancellation affect only a rider who exists and has not yet matched.

If an ID was never added, `self.d` is a `defaultdict(int)`, so reading it creates a default timestamp 0 and attempts to discard `(0, riderId)`. That tuple cannot represent another rider because its second component is different, and the unadded ID has no own tuple. The cancellation is ineffective as required. This read does retain an unnecessary dictionary entry, but later `addRider` for that ID overwrites it with the real timestamp.

**Follow FIFO state through the first example**

Rider 3 receives timestamp 0, driver 2 receives timestamp 1, and rider 1 receives timestamp 2. The earliest rider tuple is `(0,3)` and the earliest driver tuple is `(1,2)`, so the first match returns `[2,3]`.

Driver 5 arrives later and is the only waiting driver. Canceling rider 3 attempts to discard the tuple already removed by matching, changing nothing. Rider 1 remains the earliest waiting rider, so the next match returns `[5,1]`. Both ordered collections are then empty, and another match returns the sentinel pair.

**The exact source differs from the manifest summary**

The manifest describes “FIFO rider and driver queues” with “lazily invalidating canceled riders through an active-ID set.” That is not the executable design.

The source uses ordered `SortedList` containers and eagerly removes a canceled rider's tuple. There is no deque, no active-ID set, no stale queue entry, and no cleanup loop at match time.

The distinction affects complexity. Ordered-list insertions, indexed removals, and exact discards are logarithmic ordered-container operations rather than amortized constant-time queue operations. The manifest's total $O(Q)$ time describes a deque plus lazy-invalidation alternative, not this exact source.

## Complexity detail

Let $Q$ be the total number of method calls. `SortedList.add`, `discard`, and `pop(0)` are treated as $O(\log Q)$ operations. Dictionary access is expected $O(1)$, and emptiness checks are $O(1)$.

Each add or cancellation costs $O(\log Q)$. A successful match performs two ordered removals and also costs $O(\log Q)$; an unsuccessful match is $O(1)$. Across $Q$ calls, exact-source worst-case time is $O(Q\log Q)$, not the manifest's $O(Q)$.

The rider and driver collections together hold at most all unmatched additions. `self.d` retains an entry for every added rider and may also gain entries from cancellations of unknown IDs. All storage is bounded by $O(Q)$.

The source assumes `SortedList` and `defaultdict` are supplied by the execution environment. `SortedList` is not a Python built-in.

## Alternatives and edge cases

- **Deque plus active rider set:** Append arrivals to deques, mark active riders in a set, and lazily pop canceled rider IDs from the front before matching. Each entry is removed at most once, giving $O(Q)$ total expected time. This matches the manifest summary.
- **Linked FIFO queue with ID-to-node map:** Directly unlink canceled riders in $O(1)$ while keeping FIFO ends, but implementing a robust linked structure is more complex.
- **Ordinary list queues:** Appending is cheap, but removing index 0 and arbitrary cancellations can be linear, leading to $O(Q^2)$ total time.
- **No rider available:** A waiting driver must remain queued; the early return mutates neither collection.
- **No driver available:** Waiting riders, including their order, remain unchanged.
- **Cancel a matched rider:** Its ordered tuple is already gone, so `discard` safely has no effect.
- **Cancel an unknown rider:** `defaultdict` creates a timestamp entry and discards a nonexistent tuple. Behavior is correct, though it has a small state side effect.
- **Cancellation before a later allowed addition:** The real add overwrites the default timestamp and inserts the correct tuple.
- **Interleaved categories:** A global clock still preserves the independent relative order of riders and of drivers.
- **Equal rider and driver IDs:** They are stored in separate collections and can be matched together without ambiguity.
- **Unique additions:** The contract prevents duplicate waiting tuples for one rider or driver ID.
- **Ordered result pair:** The method returns `[driverId, riderId]`, not the reverse.
