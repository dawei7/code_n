## General
**Encode whose turn it is with two permits:** Initialize a `foo` semaphore with one permit and a `bar` semaphore with zero. The first `foo` iteration may proceed immediately, while an early `bar` thread blocks.

**Hand ownership to the other thread after every print:** On each of its $n$ iterations, `foo` acquires the `foo` permit, invokes `printFoo()`, and releases the `bar` permit. Symmetrically, `bar` acquires `bar`, invokes `printBar()`, and releases `foo` for the next round.

Initially only `foo` can print. Each print disables further progress by that same method until the other method prints and returns the permit, so neither `"foofoo"` nor `"barbar"` can occur. Every `foo` releases exactly one opportunity for `bar`, and every nonfinal `bar` releases the next opportunity for `foo`; with $n$ loop iterations in each method, the output is exactly $n$ ordered `"foobar"` pairs.

## Complexity detail
Each thread performs $n$ callback calls and a constant number of semaphore operations per iteration, for $O(n)$ total work. The two semaphores and loop counters occupy $O(1)$ space. Blocking time depends on scheduling but does not add polling work.

## Alternatives and edge cases
- **Condition variable with a turn flag:** It is correct when waits use guarded predicate loops, but requires more explicit lock and notification logic.
- **Two events:** Events can alternate if each phase carefully clears its own signal before setting the other; semaphores state the single-permit handoff more directly.
- **Busy waiting:** Polling a Boolean wastes CPU and lacks portable memory-order guarantees without synchronization.
- **One mutex only:** Mutual exclusion prevents simultaneous callbacks but does not by itself force alternation or make `foo` go first.
- **`n = 1`:** One permit handoff produces exactly one `"foobar"` pair.
- **Bar thread starts first:** It blocks on its zero-permit semaphore until `foo` emits the first token.
- **Spurious scheduling delays:** A delayed thread retains the only available permit, so the other thread cannot print out of turn.
