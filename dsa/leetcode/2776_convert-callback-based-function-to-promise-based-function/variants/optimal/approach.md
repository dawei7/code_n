## General

Return a closure that collects the arguments supplied to the converted function. On every invocation, construct one `Promise`. Its executor creates the callback expected by `fn`, then invokes `fn(callback, ...args)` so the callback occupies the first parameter and all ordinary arguments retain their original order.

Inside the inserted callback, inspect its two parameters. If the callback supplies an error as its second argument, call `reject(error)`. Otherwise, call `resolve(result)` with the first argument. These are the only two routes through which the wrapper settles its promise.

**Why the promise matches the callback outcome**

The wrapper invokes `fn` exactly once and gives it a callback closed over the matching promise's `resolve` and `reject` functions. Therefore, a callback call without an error resolves that invocation's promise with precisely the callback result, while a callback call with an error rejects it with precisely that error. JavaScript promises ignore settlement attempts after the first, so even an ill-behaved source that calls its callback more than once cannot change an already established outcome.

Calling `fn` inside the `Promise` executor also handles a synchronous exception correctly: the promise constructor catches a throw from its executor and turns it into a rejection. The returned wrapper need not be declared `async`; constructing and returning the promise directly supplies the required interface without an extra adoption layer.

## Complexity detail

Let $a$ be the number of ordinary arguments passed to the converted function, excluding the inserted callback. Capturing the rest arguments and forwarding them once takes $O(a)$ time. Creating the promise, callback, and settlement branch uses constant additional work; any computation performed internally by `fn` is outside the wrapper's complexity. The rest array stores $a$ references, so the wrapper uses $O(a)$ auxiliary space.

The source contract caps $a$ at 100. That bounded legal domain is too small for a reliable runtime-scaling verdict, so the package records a bounded-domain complexity certificate with boundary cases instead.

## Alternatives and edge cases

- **`async` wrapper:** An `async function` can return an inner promise and obtain the same externally visible settlement, but it adds no benefit over returning the newly constructed promise directly.
- **Prepending with repeated copies:** Rebuilding an argument array with spread during a loop can perform $O(a^2)$ copying; one rest collection and one spread forward every argument once.
- **Calling `fn(...args, callback)`:** Appending the callback violates the required calling convention because `fn` expects it in the first position.
- **Callback error:** Reject with the callback's error and ignore its result argument.
- **Synchronous throw:** Keep the `fn` call inside the promise executor so the thrown value becomes a rejection.
- **Asynchronous callback:** The promise remains pending until the callback runs; no special timer or polling is necessary.
- **Repeated callback calls:** Native promise settlement is one-shot, so only the first resolve or reject attempt has an effect.
- **Argument order:** Spread `args` only after the callback so every ordinary argument reaches the same positional parameter as before conversion.
