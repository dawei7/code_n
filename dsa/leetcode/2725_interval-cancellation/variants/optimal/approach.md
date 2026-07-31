## General

Call `fn(...args)` once before creating any timer. This guarantees the required time-zero invocation rather than making the first call wait one interval.

Create one interval whose callback invokes the same function with the same spread arguments every `t` milliseconds. Save the returned interval identifier and return a closure that passes it to `clearInterval`. The identifier connects the cancellation function to exactly this repeating schedule without exposing other state.

Before cancellation, the interval mechanism produces one callback at every interval boundary, and each callback performs the required invocation. The explicit first call adds time zero. Once the closure clears the interval, the runtime schedules no later callbacks for that identifier, so the combined sequence is precisely the immediate call followed by the interval times preceding cancellation.

## Complexity detail

Let $k$ be the number of invocations that occur before cancellation. Excluding the work performed inside the caller-supplied `fn`, total bookkeeping is $O(k)$ time, one constant action per call, and $O(1)$ auxiliary space for the interval identifier and closure. Legal timing bounds cap $k$ at $17$, so deterministic scheduler evidence replaces scaling.

## Alternatives and edge cases

- **Recursive `setTimeout`:** Scheduling the next timeout after every call can reproduce the cadence, but drift and cancellation state require more explicit handling.
- **Interval without an immediate call:** This misses the required invocation at time zero.
- **Create a new interval for every call:** Multiple active handles complicate cancellation and can produce duplicate invocations.
- Cancellation before the first interval still leaves the immediate call.
- Every invocation receives the same arguments in the same order.
- Return values do not affect scheduling, including zero or negative results.
- The cancellation closure must clear the exact interval created by this call.
- The maximum legal window produces seventeen calls at $t=30$ before cancellation at $500$ ms.
