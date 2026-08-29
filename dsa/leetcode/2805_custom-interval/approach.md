## General

**The delay grows after every callback.** This interval is not a fixed-period timer. If the initial delay is `delay` and the increment is `period`, the first callback is scheduled after `delay` milliseconds, the second after an additional `delay + period` milliseconds, the third after another `delay + 2 * period` milliseconds, and so forth. The implementation realizes that behavior as a chain of one-shot `setTimeout` calls.

**Give each custom interval its own identity and state.** A module-level `Map` named `intervals` associates numeric custom IDs with state objects. `nextIntervalId` starts at one and is incremented for each creation, so concurrently active intervals receive different IDs even though the native environment may represent timeout handles in its own way.

The state contains `count`, `handle`, and `active`. `count` is the number of callbacks that have already completed. `handle` is the currently pending native timeout handle. `active` is a logical cancellation flag that protects against timing races and cancellation during a callback.

**Schedule exactly one pending timeout.** The nested `schedule` function calls `setTimeout` with a delay of `delay + period * state.count`. Initially `count` is zero, so the first wait is exactly `delay`.

When the timeout fires, its closure first checks `state.active`. If cancellation happened after the host queued the timeout callback but before the callback body began, this test suppresses `fn`. Otherwise, it calls `fn()`, increments `count`, and, if still active, calls `schedule()` again.

Because `count` is incremented before rescheduling, the second timeout receives `delay + period`, the third receives `delay + 2 * period`, and in general the wait before callback number $r$, using one-based callback numbering, is

$$
\texttt{delay} + (r-1)\texttt{period}.
$$

The cumulative ideal firing time of callback $r$ relative to creation is the sum of all those waits:

$$
r\texttt{delay}+\frac{r(r-1)}{2}\texttt{period}.
$$

Real event-loop scheduling can add lateness, so these values are requested delays rather than wall-clock guarantees.

**Reschedule only after the callback completes.** The next wait begins after `fn` returns and `schedule` is called again. Therefore, a slow callback adds its own execution duration to the elapsed wall-clock time between observed callback starts. This is chained-timeout behavior, not a calendar schedule that compensates for drift.

The recursion is asynchronous. `schedule` returns immediately after registering the timeout. When a timeout later invokes `schedule` again, the previous JavaScript call stack has already unwound except for the current host callback. Consequently, repeated firings do not build an ever-deeper synchronous recursion stack.

**Register before returning.** After defining `schedule`, the code stores the state in `intervals`, schedules the first timeout, and returns the custom numeric ID. Keeping the state in the map allows `customClearInterval` to find it later. Multiple custom intervals remain independent because each has a separate state object and closure.

**Cancellation is deliberately two-layered.** `customClearInterval(id)` retrieves the state. If no entry exists, it returns without effect, making repeated or unknown-ID cancellation safe. For a live interval, it sets `active = false`, calls native `clearTimeout` on the currently stored handle, and deletes the map entry.

Native cancellation prevents a still-pending timer from being delivered in the ordinary case. The flag covers harder timing situations. If a host has already queued the callback, its first active check prevents `fn`. If `fn` itself calls `customClearInterval` for its ID, cancellation sets the flag while the callback is executing; the active check after `count++` then prevents another timeout from being scheduled.

**Why callbacks occur in the required sequence.** At creation, exactly the zero-count timeout is scheduled. Assume callback $r$ is the next active callback and `count = r - 1` when its wait is chosen. Its delay has the required formula. After it runs, count becomes $r$, and exactly one timeout for callback $r+1$ is scheduled using the next formula. Cancellation can stop the sequence but cannot create an extra scheduled branch. By induction, every callback that occurs has the correct increasing delay and order.

**A thrown callback is a limitation of the exact source.** There is no `try...finally` around `fn()`. If `fn` throws, execution skips `count++` and the rescheduling call. The interval effectively stops firing, but its state remains in `intervals` until explicitly cleared, which can retain memory. The normal problem contract assumes callbacks complete normally.

## Complexity detail

Creating an interval performs a constant amount of JavaScript work plus one map insertion and one host timer registration, so it is expected $O(1)$ time. Clearing by ID performs an expected $O(1)$ map lookup and deletion plus one host cancellation.

For $k$ callbacks that actually fire, the scheduler performs $O(k)$ total bookkeeping work, excluding the time inside `fn` and the real waiting time. Each firing does constant arithmetic, flag checks, and one possible timer registration. It is often clearer to state $O(1)$ overhead per firing.

At any moment, each active custom interval has one map entry, one state object, one closure environment, and at most one pending native timeout. If $a$ intervals are active, scheduler-managed space is $O(a)$. For a single interval, space stays $O(1)$ regardless of how many times it has already fired; callbacks are not accumulated.

The numeric `count` grows over time. Under JavaScript Number semantics, extremely long-running intervals can eventually lose integer precision, but challenge durations are nowhere near that boundary. The manifest's constant-space description is correct per active interval, while total global storage naturally scales with the number of simultaneous intervals.

## Alternatives and edge cases

- **Native `setInterval`:** It repeats a fixed delay and therefore cannot directly express a delay that grows by `period` after every callback.
- **Recursive `setTimeout` without a map:** This handles one interval but provides no stable custom ID lookup for cancelling among multiple active intervals.
- **Absolute-deadline scheduling:** Compute each desired cumulative deadline from the original start time and subtract the current time before scheduling. That can reduce drift from timer lateness, but it differs from the exact after-callback chaining behavior.
- **Cancellation before the first firing:** Native `clearTimeout` removes the pending handle, the active flag is false, and no callback should execute.
- **Cancellation during `fn`:** The post-callback active check prevents rescheduling, even though `count` is still incremented after `fn` returns.
- **Cancellation after host queueing:** The leading active check suppresses a queued callback that native clearing can no longer retract.
- **Unknown or repeated ID:** The map lookup fails and clearing becomes a harmless no-op.
- **Multiple intervals:** Unique IDs and separate state objects prevent one interval's count or handle from affecting another.
- **Zero period:** Every requested wait is `delay`, so the custom timer behaves like a chained fixed-delay interval.
- **Zero delay:** The first callback is eligible immediately through the event loop, and later waits grow by multiples of `period`; callbacks still do not run synchronously during creation.
- **Slow callback:** The next timeout is registered only after completion, so observed start-to-start spacing includes callback execution time.
- **Thrown callback:** Rescheduling is skipped and the map entry is retained. A production implementation could use `try...finally` and define an explicit error policy.
- **Timer clamping:** Browsers and Node.js may delay or clamp timers. The algorithm controls requested delays but cannot promise exact wall-clock execution.
- **ID growth:** IDs increase monotonically and are not reused. Ordinary challenge workloads cannot approach Number precision limits, but a permanent service might need wraparound handling.
