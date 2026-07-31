## General

An `async` function must return a promise, but returning from it immediately would not create the required delay. Instead, construct a new promise and retain its `resolve` callback. Register that callback with `setTimeout`, passing the requested number of milliseconds. The function returns the pending promise at once; the host timer later invokes `resolve`, which settles it.

No polling is necessary. JavaScript's event loop and timer facility track the deadline while other work may continue. The promise can resolve with `undefined` because the contract places no requirement on its fulfilled value.

The delay is approximate rather than exact. A timer callback becomes eligible after the requested interval, but a busy event loop can execute it later. That scheduling behavior is why small deviations in the measured duration are permitted.

## Complexity detail

Let $m$ be the requested delay in milliseconds. The promise completes after $O(m)$ elapsed time, while setting up the promise and timer requires $O(1)$ JavaScript work. The promise, resolver, and timer registration occupy $O(1)$ auxiliary space.

The elapsed-time bound is optimal for this contract: a valid implementation cannot resolve materially before $m$ milliseconds, giving an $\Omega(m)$ lower bound. A single timer matches it without a CPU-consuming loop.

## Alternatives and edge cases

- **Busy waiting:** Repeatedly checking the clock could delay for the right duration, but it blocks the event loop and wastes CPU for the entire interval.
- **Immediately resolved promise:** This preserves the asynchronous return type but violates the required pending duration.
- **Timer callback wrapper:** Passing `() => resolve()` also works, but passing `resolve` directly is simpler because the fulfilled value is unrestricted.
- **Minimum delay:** A one-millisecond request must still use asynchronous scheduling rather than resolve synchronously.
- **Timer imprecision:** Event-loop load may make the observed duration slightly longer than requested; such minor deviation is allowed.
- **Resolved value:** No particular fulfillment value is required, so resolving without an argument is valid.
