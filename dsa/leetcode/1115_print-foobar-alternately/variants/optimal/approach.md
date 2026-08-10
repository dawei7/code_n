## General

**Represent whose turn it is with permits**

Two threads must print alternating tokens for $n$ rounds. A semaphore count represents permission to proceed.

`self.f = Semaphore(1)` gives the foo thread one initial permit, so foo may print first. `self.b = Semaphore(0)` gives the bar thread no initial permit, so bar blocks if scheduled before foo.

Only one side has a permit at a time. After printing, that side releases the other side’s semaphore, explicitly handing over the turn.

**One foo iteration**

At the start of every foo iteration, `self.f.acquire()` waits for a foo permit and consumes it. The count changes from one to zero, so foo cannot pass another iteration until bar returns a permit.

`printFoo` runs while bar still has no permit. Only after the callback returns does `self.b.release()` create one bar permit.

This ordering guarantees that the complete text `foo` is produced before the corresponding `bar` callback can begin.

**One bar iteration**

The bar thread mirrors the process. `self.b.acquire()` waits until foo finishes one callback and releases a permit. Bar consumes it, calls `printBar`, and then releases `self.f`.

That last release authorizes exactly the next foo iteration. Bar cannot immediately print twice because its own semaphore returned to zero when it acquired the permit.

**The alternating invariant**

Before the first iteration, there is one foo permit and zero bar permits. After foo prints, there are zero foo permits and one bar permit. After bar prints, the state returns to one foo permit and zero bar permits.

By induction, the only callback order is:

`foo, bar, foo, bar, ...`.

Each method loops exactly `self.n` times, so there are $n$ foo callbacks and $n$ bar callbacks. Because foo owns the initial permit and bar returns the final foo permit only after its last print, the visible output is `foobar` repeated $n$ times.

**Why scheduler order does not matter**

If bar starts first, it blocks on a zero-count semaphore. If foo runs far ahead in CPU scheduling, it still blocks at its next acquire because it gave away the only turn permit. If bar receives repeated scheduler time, it similarly cannot pass twice.

The scheduler decides when an enabled thread runs, but semaphore counts decide which thread is enabled. Scheduling can delay progress but cannot change the legal order.

**Why callbacks precede releases**

The release belongs after the print callback. If foo released `b` first, bar might print before foo completed. If bar released `f` first, the next foo could begin before the current bar callback ended.

Keeping each callback between acquire and opposite release makes each printed token the completed work protected by that turn.

**Progress and absence of deadlock**

There is no circular state in which both threads permanently wait during normal execution. Initially foo can run. Every successful foo iteration enables bar, and every successful bar iteration enables foo.

Both loops use the same $n$, so neither thread exits early while the other still needs a permit. After bar’s final iteration it releases an extra foo permit, but foo has already completed its $n$ acquisitions or will use the permit for its final pending iteration depending on scheduling. No further callback is produced beyond the fixed loop counts.

Normal callback completion is assumed. An exception before releasing the opposite semaphore could leave the other thread blocked, which is outside the problem contract.

## Complexity detail

Each thread performs $n$ loop iterations. Every iteration has one acquire, one callback, and one release, all constant synchronization work apart from the external callback’s own cost. Total algorithmic work is $O(n)$.

The repository’s reviewed scaling distinction is constant work per foo/bar handoff. This implementation never rescans prior output or accumulated state.

Two semaphore objects, the stored integer $n$, and loop variables use $O(1)$ space. The output is produced through callbacks rather than stored by the class.

Blocking time depends on scheduling and callback duration, but blocked semaphore waits do not change the algorithmic operation count or consume an input-sized buffer.

## Alternatives and edge cases

- **Two locks as gates:** Start foo’s lock open and bar’s closed, then release the opposite lock after each callback. Semaphore ownership rules often make repeated cross-thread handoffs clearer.
- **Condition variable with turn flag:** Wait for a Boolean turn, print, flip it, and notify. Correct use requires a loop around waits to handle wakeups.
- **Events:** Events can coordinate turns but must be cleared and set carefully to prevent one thread from passing multiple iterations.
- **Busy waiting:** Polling a shared turn flag wastes CPU and needs synchronization for visibility.
- **`n = 1`:** Foo consumes the initial permit, prints once, enables bar, and bar prints once.
- **Bar scheduled first:** Its zero-permit acquire blocks safely until foo prints.
- **Foo repeatedly scheduled:** It cannot begin its next iteration until bar returns the permit.
- **Equal loop counts:** Both methods must run $n$ iterations; mismatched counts could strand one thread.
- **Permit counts:** Each acquire consumes the only active permit before printing, preventing duplicate consecutive tokens.
- **Release placement:** Releasing before the callback would weaken the required ordering.
- **Final permit:** A leftover foo permit after all work is harmless because no additional loop iteration exists.
- **Callback exception:** It can interrupt the handoff and block the peer; normal callback completion is assumed.
- **No output buffer:** The class controls callback order and does not build the output string itself.
