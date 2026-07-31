## General

Each invocation needs two competing promises: the promise returned by `fn(...args)` and a timeout promise that rejects with the exact required string after `t` milliseconds. `Promise.race` adopts whichever of these settles first, automatically preserving either the source's resolved value or its rejection reason.

Create the timeout and retain its timer handle. Await the race inside `try`, then call `clearTimeout` in `finally`. The cleanup executes after success, source rejection, or timeout rejection. If the source settles early, clearing prevents an unnecessary later timer callback; if the timeout already fired, clearing its handle is harmless.

**The race matches every observable outcome**

Before either competitor settles, the returned promise remains pending. If the source settles first, `Promise.race` adopts exactly that state and value. If the timer fires first, its rejection becomes the returned rejection and later source settlement cannot change the already settled promise. These are the only possibilities, so the wrapper implements the required time boundary while forwarding every positional argument once.

An already settled source promise schedules its race reaction as a microtask, which precedes a zero-delay timer callback. For two delayed timers registered at the same delay by this implementation, the wrapper's timeout is registered first and therefore wins their tie.

## Complexity detail

Let $a$ be the number of forwarded arguments. Excluding `fn`'s own work and pending duration, forwarding those arguments takes $O(a)$ time. Timer creation, racing two promises, settlement, and cleanup are constant additional operations. The wrapper retains the argument array until settlement plus a constant number of promise and timer references, for $O(a)$ space.

Because $a \le 10$ and $t \le 1000$, runtime tiers cannot honestly measure the argument-forwarding class; wall-clock scaling would mainly measure user-selected delays. The bounded-domain certificate instead verifies the constant race structure and all material settlement boundaries.

## Alternatives and edge cases

- **Manual outer `Promise`:** Attach `then` and `catch` handlers to `fn(...args)` and reject from a timer. This is correct when carefully cleaned up, but `Promise.race` states the competition more directly.
- **Race without clearing the timer:** Observable results remain correct, yet every early source settlement leaves a needless timer scheduled until `t` expires.
- **Await the source before creating the timer:** This never enforces the limit because timer setup occurs only after the source has already finished.
- **Source rejection:** Preserve the original reason when it happens before the timeout; do not replace every rejection with the timeout message.
- **Timeout rejection text:** Use exactly `"Time Limit Exceeded"`, including capitalization and spaces.
- **Zero arguments:** Forward an empty argument list and race normally.
- **Zero time limit:** An already settled promise reaction runs before the timer task, while genuinely delayed work loses to the zero-delay timeout.
- **Losing source promise:** A timeout does not cancel the underlying asynchronous operation; its eventual settlement simply cannot change the race result.
