## General

**Model turns instead of repeatedly editing the string**

The procedure repeatedly visits senators in circular left-to-right order. Banned senators disappear from all future rounds, while surviving senators eventually act again. Physically deleting characters and restarting scans would be expensive and difficult to reason about.

The solution instead stores the future turn positions of currently eligible senators:

- `qr` contains Radiant turn positions in increasing order;
- `qd` contains Dire turn positions in increasing order.

Initially, these positions are the original string indices. A surviving senator's position in the next round is represented by adding `n` to the position just used. This creates one increasing global timeline across all rounds.

For example, original index two acts at positions two, `2 + n`, `2 + 2n`, and so on if the senator survives that long. The numeric value is not a literal compacted-array index; it is an ordering label that tells us when the turn occurs.

**Build one queue per party**

The initialization scans `senate` from left to right. Each `R` index is appended to `qr` and each `D` index to `qd`. Because the scan indices increase, both queues start sorted by future turn order.

Keeping the parties separate makes the next active member of either party available at the front. A `deque` is used because removing from the front and appending to the back both take constant time.

**Why only the two queue fronts need to be compared**

Suppose `qr[0]` is the earliest future Radiant turn and `qd[0]` is the earliest future Dire turn. Whichever number is smaller acts first. A smart senator should ban an opposing senator, and banning the earliest opposing turn is safe: that opponent is the most immediate threat and would otherwise act before all later opponents.

If the Radiant index is smaller, that Radiant senator acts first and bans the Dire senator at `qd[0]`. The Radiant senator remains eligible for a future round, while that Dire senator disappears permanently. The opposite happens when the Dire index is smaller.

Original indices and requeued timeline positions are unique, so the two fronts cannot be equal.

**Update both queues after one confrontation**

The exact loop first compares the two front values. If Radiant is earlier, it appends `qr[0] + n` to the Radiant queue. If Dire is earlier, it appends `qd[0] + n` to the Dire queue.

It then removes the front of both queues:

- the earlier senator's current turn is consumed, but that senator's next-round turn has already been appended;
- the later opposing senator is banned, so its front is removed without replacement.

The order “append survivor, then pop both fronts” is valid because the appended value is larger than all current-round positions and goes at the back. The stored front values are still available for the comparison and addition before removal.

Each confrontation reduces the total number of eligible senators by exactly one. One senator survives and remains represented once; the other disappears.

**Why adding `n` preserves circular order**

All original turns for a round lie in a block of `n` consecutive timeline positions. A senator who acts at position `p` and survives must wait until the scan wraps around, so `p + n` is its corresponding position one round later.

Adding the same positive `n` preserves relative order among survivors. If one current turn precedes another, their next-round positions have the same ordering. Because requeued positions are later than the current position and queues were already sorted, appending maintains each queue's increasing order.

The senate may contain fewer active senators in later rounds, so these numbers are not counts of actual operations. Only their ordering matters.

**A walkthrough of `"RDD"`**

The initial queues are `qr = [0]` and `qd = [1, 2]`, with `n = 3`.

First, Radiant position zero is earlier than Dire position one. Radiant bans that Dire senator and is requeued at position three. After both fronts are removed:

`qr = [3]` and `qd = [2]`.

Next, Dire position two is earlier than Radiant position three. Dire bans that Radiant senator and is requeued at position five. After removal:

`qr = []` and `qd = [5]`.

No eligible Radiant senator remains, so Dire can announce victory.

**Why the simulation matches optimal play**

At any point, the minimum front across the two queues is the next senator who still has rights. If that senator left the earliest opposing senator active, that opponent would act before any later opposing senator and could ban a member of the first party. Banning the earliest opposing turn prevents the most immediate hostile action without sacrificing any earlier opportunity, so the queue pairing models a rational optimal ban.

After the ban, the survivor's next chance is exactly one circular pass later, represented by adding `n`. The two front removals therefore transform the queue state into precisely the eligible-turn state after that action.

By induction over confrontations, the queues contain exactly all senators who retain rights, ordered by their next turns. When one queue becomes empty, every remaining eligible senator belongs to the other party. A senator from that party can then announce victory, so the final conditional returns the correct name.

## Complexity detail

Let `N` be the original number of senators.

Initialization scans the string once and appends each index once, taking `O(N)` time. Every loop iteration bans exactly one senator, so there can be at most `N - 1` iterations before one party disappears. Each iteration performs constant-time deque front access, at most one append, and two `popleft` operations. Total time is `O(N)`.

The two queues initially contain exactly `N` indices in total. A confrontation removes two entries and appends one, so their combined size decreases by one. It never exceeds `N`, giving `O(N)` auxiliary space.

Timeline labels can grow beyond `N` across rounds, but Python integers handle them. Their count, rather than their numeric magnitude, determines the standard space bound.

## Alternatives and edge cases

- **Repeated string simulation:** Mark or remove banned senators and scan round after round. Physical deletion from a list or string can cost linear time per ban and lead to quadratic behavior.

- **One queue with a party balance:** A single queue can track pending bans for each side and requeue survivors. It can also achieve `O(N)` time, but the two-queue timeline makes the next opposing turns explicit.

- **Boolean banned array:** Keep original indices and search circularly for the next unbanned opponent. Without an efficient index structure, repeated searching can scan many inactive positions.

- **Ban a later opponent:** Leaving the earliest opposing turn alive permits that senator to act sooner. The two-front strategy removes the immediate threat and is the canonical optimal-play simulation.

- **Only Radiant senators initially:** `qd` is empty, the loop never runs, and the result is `Radiant`.

- **Only Dire senators initially:** `qr` is empty, the loop never runs, and the result is `Dire`.

- **One senator:** Exactly one queue contains index zero, so that senator's party wins immediately.

- **Alternating parties:** Comparisons and requeued positions correctly carry surviving senators across round boundaries; no explicit round counter is needed.

- **Long run of one party:** Early senators from that party can ban upcoming opponents one by one. Separate queues avoid scanning across the run repeatedly.

- **Equal future positions:** They cannot occur because each original senator has a unique index and adding multiples of `n` preserves distinct residues modulo `n`.

- **Using list `pop(0)`:** Removing the first list element shifts the remainder and can make the method quadratic. `deque.popleft()` is essential for the stated bound.

- **Requeueing the banned senator:** Exactly the lower timeline position survives. Appending both fronts would fail to reduce the electorate and could make the loop never terminate.

- **Appending the survivor without adding `n`:** That would place the senator back into the current round and allow an immediate second action. The offset enforces the circular wait.
