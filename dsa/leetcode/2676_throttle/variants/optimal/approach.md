## General

**Model throttling as idle versus waiting**

The returned function has two modes. When `waiting` is false, no throttle window is active, so a call is a leading call and must execute `fn` immediately. When `waiting` is true, `fn` may not execute immediately; the wrapper remembers only the most recent blocked call.

Two closure variables represent all persistent state:

- `waiting` tells whether a timer chain currently owns the next permitted execution point.
- `pending` is either `null` or one record containing the latest blocked call's `context` and `args`.

The closure matters because these values must survive after `throttle` itself returns and across many later invocations of the wrapper.

**Execute an idle call immediately**

The returned function accepts arbitrary arguments with `...args`. When `waiting` is false, it runs:

`fn.apply(this, args)`.

This is the required leading execution. It then changes `waiting` to true and schedules `release` after `t` milliseconds.

Changing the flag before any later external call can arrive establishes the closed window. Until the timer fires, calls take the other branch.

**Preserve the receiver as well as the arguments**

A JavaScript method call has both explicit arguments and an implicit `this` value. Saving only `args` would be wrong when callers use the throttled function as methods of different objects.

The immediate branch passes the wrapper's current `this` directly to `fn.apply`. The blocked branch stores:

`{ context: this, args }`.

The trailing execution later uses `fn.apply(call.context, call.args)`. Therefore it reproduces both parts of the latest suppressed invocation.

**Overwrite pending work during the closed window**

While `waiting` is true, each invocation replaces `pending` rather than adding to a queue.

Suppose calls arrive with arguments 2, 8, and 5 before the next release. The stored record first holds 2, then 8, then 5. Only 5 survives.

That is the defining difference between throttling here and queueing every call. The interval limits execution frequency, while the newest request represents the current desired work.

**What the timer callback does**

When `release` runs, it first checks `pending`.

If `pending === null`, no call arrived during the completed window. The timer chain is no longer needed, so `waiting` becomes false. The next wrapper invocation will again execute immediately.

If a pending call exists, the callback:

1. saves its record in local variable `call`;
2. clears `pending`;
3. invokes `fn` with the saved receiver and arguments;
4. schedules another `release` after `t` milliseconds.

The trailing execution begins a new throttle window just like a leading execution. This is why a sustained stream can produce executions at most once per interval.

**Why pending is cleared before calling the function**

Clearing first separates the call being processed from calls that might arrive during its execution or during the next window.

After the local variable `call` captures the old record, `pending = null` means the new interval begins with no waiting work. If another wrapper call occurs, it can install a fresh pending record without overwriting the record already being executed.

The local variable retains everything needed for the current invocation.

**Trace the 50-millisecond example**

Assume the first wrapper call arrives at 50 ms with arguments 1. Because the wrapper is idle, `fn` runs immediately and a release is scheduled for 100 ms.

A call at 75 ms cannot run. Its record becomes `pending`.

At 100 ms, `release` finds that record, clears the slot, calls `fn` with arguments 2, and schedules the next release for 150 ms.

If no call arrives between 100 and 150 ms, the callback at 150 ms finds `pending` empty and changes `waiting` to false. A later call can run immediately rather than waiting for another artificial grid point.

**Trace replacement and chained windows**

With `t = 70`, a leading call at 50 ms schedules 120 ms. Calls at 75 and 90 ms both occur while waiting, so the second record replaces the first.

At 120 ms, only the 90 ms call executes. A new release is scheduled at 190 ms. A call at 140 ms becomes pending and executes at 190 ms, extending the chain to 260 ms.

If nothing is pending at 260 ms, the wrapper becomes idle. A call at 300 ms therefore runs at 300 ms, not at a stale interval boundary.

**The invariant that proves correctness**

While `waiting` is true, one timer is scheduled for the end of the current execution window, and `pending` represents exactly the latest wrapper call since the most recent execution, if such a call exists.

The leading branch establishes this invariant with an empty pending slot. Every blocked call preserves it by replacing the slot with the newest call. At release, an empty slot correctly ends the chain; a nonempty slot executes exactly its latest call and starts the invariant again for a new window.

Thus executions are separated by at least `t` milliseconds, the first idle call is immediate, and each occupied interval produces one trailing call with the latest inputs.

**Why one timer is enough**

The wrapper does not schedule a timer for every suppressed call. Those calls merely update `pending`. A single timer defines the next legal execution time.

This prevents a burst from creating many callbacks that would later all run. It also makes cancellation unnecessary because no newer suppressed call creates a competing timer.

## Complexity detail

Each wrapper call performs a constant number of flag checks, assignments, and timer operations, excluding the work performed by `fn` itself. With the challenge's bounded argument count, this is $O(1)$ time per call. More generally, collecting and later spreading $a$ arguments costs $O(a)$.

The closure stores one Boolean, one timer chain, and at most one pending call record. Under the bounded inputs this is $O(1)$ space. In a general model, the saved latest argument array occupies $O(a)$ space.

## Alternatives and edge cases

- **Schedule every blocked call:** Incorrect because intermediate calls must be coalesced, not queued.
- **Debounce:** It waits for activity to stop before executing and therefore does not provide the required immediate leading call.
- **Fixed `setInterval`:** It can implement the same state machine, but it must be cleared when a whole interval has no pending work.
- **Timestamp plus replaceable timeout:** Also valid, but it needs careful delay calculations and timer cancellation.
- **No blocked calls:** The release callback returns the wrapper to idle without invoking `fn`.
- **Many blocked calls:** Only the latest receiver and argument array survive.
- **Different `this` values:** The pending record preserves the receiver belonging to the latest call.
- **Zero interval:** The leading call is immediate; suppressed synchronous calls are coalesced until the zero-delay timer task runs.
- **Call at a timer boundary:** JavaScript event-loop ordering determines which task runs first, but the state machine remains internally consistent.
- **Callback throws:** The exact source does not catch errors; a thrown trailing callback can prevent scheduling the next release and is outside the ordinary promised-call behavior.
- **Return values:** The wrapper does not return `fn`'s result; the problem evaluates execution timing and arguments.
- **Sustained activity:** Each trailing execution starts another complete interval, enforcing the frequency limit continuously.
