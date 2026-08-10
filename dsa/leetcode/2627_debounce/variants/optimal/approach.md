## General

**Keep only the latest pending invocation**

Debouncing groups calls that occur close together. Every call schedules execution for $t$ milliseconds later, but a newer call arriving before that execution cancels the old schedule.

At any moment, the wrapper needs to remember only one thing: the timer handle for the currently pending invocation. Variable `timeoutId` is stored in the closure returned by `debounce`.

The closure persists across calls, so every invocation can cancel the schedule created by the previous invocation.

**Cancel before scheduling**

Each wrapper call begins with:

`clearTimeout(timeoutId)`.

On the very first call, `timeoutId` is undefined. JavaScript safely treats clearing an unknown or undefined handle as doing nothing, so no first-call branch is required.

On later calls, if the prior timer has not fired, cancellation prevents its callback from executing. The wrapper then creates a new timer for the full delay $t$.

The order matters. Scheduling first and clearing afterward could cancel the newly created timer instead of the previous one.

**Capture the latest arguments**

The wrapper uses rest syntax `(...args)`, producing an array containing exactly the arguments from that invocation in order.

The timer callback closes over this particular `args` array. When a newer invocation cancels the timer, the old callback becomes unreachable by the timer system. The new timer captures the new call's arguments.

Therefore, the eventual execution receives the arguments of the last call in the quiet period, not those of the first call.

For calls with inputs one at 50 milliseconds and two at 75 milliseconds under $t=50$:

- the first timer was due at 100;
- the second call cancels it;
- the second timer is due at about 125;
- only `fn(2)` runs.

**Preserve the receiver's `this` context**

The returned wrapper is a normal function. When it is called as an object method, its dynamic `this` may matter to `fn`.

Before scheduling, the solution records:

`const context = this`.

The timer callback is an arrow function, so it captures that local reference. It later calls:

`fn.apply(context, args)`.

`apply` invokes `fn` with the original receiver and spreads the captured array as positional arguments.

Without this preservation, a method that reads `this.someProperty` could run with undefined or the global/timer context. The exact solution is therefore more general than simply calling `fn(...args)`.

**Why the arrow timer callback helps**

Arrow functions do not create their own `this`, but this callback does not need timer-provided context at all. It explicitly uses the captured `context`.

The combination is deliberate:

- normal returned function captures the caller's dynamic receiver;
- arrow timer callback retains lexical access to that receiver and the argument array.

This separates invocation-time context from later asynchronous execution.

**The quiet-period interpretation**

After every wrapper call, imagine a deadline exactly $t$ milliseconds in the future.

- A new call before the deadline erases that deadline and starts a new one.
- If no new call arrives before the deadline, the pending callback runs.

Thus execution occurs only after the call stream has been quiet for a full interval $t$.

This differs from throttling. A throttle generally permits at most one call per interval, often executing the first. This debounce implementation executes the final call after activity stops.

**Calls after an execution form a new group**

Once a timer has fired, clearing its handle during a much later wrapper call has no effect because the old callback already ran. The later call simply schedules another timer.

That is why, with calls at 50 and 100 under $t=20$, both execute: the first fires around 70, well before the second call occurs. They belong to different quiet periods.

The code does not reset `timeoutId` to undefined after firing, but it does not need to. Clearing an already-completed timer is harmless, and the handle is overwritten by the next schedule.

**Simultaneous calls**

If two wrapper invocations occur at the same recorded time, JavaScript still executes their synchronous call bodies in some definite sequence. The later one in that sequence clears the earlier timer and becomes the surviving invocation.

This matches the example where two calls at 300 milliseconds leave only the last inputs for execution at 450.

**A simple invariant proves correctness**

After each wrapper call completes, exactly one non-cancelled timer created by this debounce wrapper remains pending, and its callback captures the most recent call's arguments and receiver.

The first call establishes the invariant. Every next call cancels the one pending timer, then creates one replacement with its own data. If the timer fires before another call, it invokes `fn` once with that captured data.

Therefore, every cancelled call is suppressed, and every call followed by a quiet interval of length $t$ executes once after that interval.

**Return behavior**

The wrapper itself does not return `fn`'s eventual result. It returns undefined immediately because the real invocation occurs asynchronously.

The contract asks only for delayed execution. If callers needed an awaitable result for each surviving call, a more elaborate Promise-based API and cancellation semantics would be required.

## Complexity detail

Each wrapper invocation cancels at most one timer, captures its arguments and receiver, and schedules one timer. With at most ten arguments by the challenge constraints, this is treated as $O(1)$ time and $O(1)$ retained space, matching the manifest.

More generally, collecting and retaining $a$ arguments costs $O(a)$ time and space for the pending invocation. Only the latest argument array remains reachable through an active timer.

The elapsed delay is $t$ milliseconds, but the wrapper's computational work does not loop for $t$.

## Alternatives and edge cases

- **`setInterval` polling:** Can implement delayed detection but repeatedly wakes and tracks timestamps; one timeout per latest call is simpler.
- **Throttle:** It enforces a different policy and may execute the first call rather than the last.
- **Call `fn(...args)` directly in the timer:** Works for context-free functions but can lose the original `this` receiver.
- **First call:** Clearing undefined is harmless, then one timer is scheduled.
- **Call inside the delay window:** It cancels the preceding pending execution and restarts the full delay.
- **Call after prior execution:** It begins a new independent debounce group.
- **`t = 0`:** Execution is still deferred to a timer task; another synchronous call can cancel it first.
- **Several arguments:** Rest and `apply` preserve their order.
- **Simultaneous calls:** The last invocation in event-loop execution order survives.
- **Return value:** The debounced wrapper returns immediately and does not expose the later function result.
