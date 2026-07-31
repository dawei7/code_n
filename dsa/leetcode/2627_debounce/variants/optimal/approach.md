## General

At any moment, a debounced function needs at most one pending execution: the newest call that has not yet enjoyed a quiet interval of `t` milliseconds. Store that pending timeout's handle in the closure returned by `debounce`.

**Replace the pending execution on every call**

When the wrapper is invoked, first pass the stored handle to `clearTimeout`. This is harmless before the first call and cancels the previous callback on later calls. Then schedule a new callback for `t` milliseconds later and save its handle.

The timer callback closes over the newest arguments and receiver. Calling `fn.apply(context, args)` forwards both, so debouncing does not change how the underlying function observes its invocation.

After any wrapper call, the single stored timer represents exactly that call and is due after the full delay. A later call before it fires cancels it and establishes the same property for the newer call. If no later call arrives, the timer fires and invokes `fn` once with the retained arguments. Thus every interrupted burst suppresses all but its last call, while calls separated by quiet intervals execute independently.

## Complexity detail

Treating host timer registration and cancellation as constant-time operations, creating the wrapper takes $O(1)$ time and each invocation takes $O(1)$ time. Across $C$ wrapper calls, total scheduling work is $O(C)$. The closure keeps one timer handle; one pending callback additionally retains only the newest receiver and argument list, so state beyond those required arguments is $O(1)$.

## Alternatives and edge cases

- **Generation counter:** Schedule every callback and let each compare a captured generation with the newest generation before running. This preserves observable output but leaves superseded timers active and may retain arguments for every call until their delays expire.
- **Timestamp polling:** Record the latest call time and run a periodic poller. It adds unnecessary repeated work and makes exact scheduling and cleanup more complicated.
- **Lodash `_.debounce`:** A library utility provides richer options, but its use is explicitly forbidden by this problem.
- **First invocation:** `clearTimeout(undefined)` is safe, so no separate initialized flag is needed.
- **Zero delay:** Execution is still scheduled through the timer queue; another synchronous call can cancel it before the callback runs.
- **Same-time calls:** Process invocation order normally; every later wrapper call cancels the handle created by the earlier one, leaving the final call pending.
- **Receiver and arguments:** Preserve `this` as well as all positional arguments when the delayed function runs.
