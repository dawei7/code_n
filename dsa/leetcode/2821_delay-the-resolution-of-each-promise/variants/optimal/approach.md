## General

Map every source function to a new zero-argument wrapper. Do not invoke the source while building the array: the wrapper calls `fn()` only when the caller invokes that wrapper.

Attach both callbacks of `then` to the source promise. The fulfillment callback creates a new promise and schedules `resolve(value)` with `setTimeout(..., ms)`. The rejection callback likewise creates a new promise and schedules `reject(reason)` after the same delay. Returning those timer-backed promises makes the promise chain wait for the extra interval before it exposes either outcome.

**Why both settlement paths need separate handlers**

An `async` wrapper that simply awaits the source and then sleeps delays successful results, but an awaited rejection throws before the sleep is reached. Handling fulfillment and rejection explicitly guarantees that both paths receive the additional delay. Each handler forwards the exact value or reason it received, so delaying settlement cannot change the source outcome.

Array `map` writes each wrapper at the same index as its source function. Every invocation creates its own source promise and timer, so wrappers neither reorder nor share pending work.

## Complexity detail

Let $n$ be the number of source functions. Constructing the returned array visits each function once, requiring $O(n)$ time and $O(n)$ space for the wrappers. Invoking one wrapper adds $O(1)$ bookkeeping and one pending timer beyond the work and storage of the source promise itself.

The legal input contains at most ten functions, and `ms` is a required wall-clock delay rather than computational work that an implementation may optimize away. Runtime scaling would therefore measure timer scheduling noise over a domain of only ten wrappers. A bounded-concurrency certificate instead verifies the $O(n)$ construction, lazy invocation, independent timers, order preservation, and both settlement paths with a deterministic scheduler.

## Alternatives and edge cases

- **Await and then sleep only on success:** A rejected source throws before the delay step, so this common form violates the rejection-delay contract.
- **Delay before calling the source:** This shifts the start of the underlying work instead of adding `ms` after its settlement.
- **Invoke every source during `map`:** That eagerly starts promises before the returned functions are called and breaks the required lazy function interface.
- **Use one shared timer:** Source promises can settle at different times, so every invocation needs its own timer beginning at its own settlement.
- **Fulfillment values:** Forward the original value unchanged, including `undefined`, objects, and other reference values.
- **Rejection reasons:** Reject with the original reason rather than resolving with it or replacing it.
- **Repeated invocation:** Calling one returned wrapper multiple times must call the corresponding source function multiple times and create independent delayed promises.
- **Array order:** Completion order does not affect the position of wrappers in the returned array.

