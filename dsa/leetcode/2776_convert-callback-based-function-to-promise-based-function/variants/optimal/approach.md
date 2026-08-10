## General

**Build an adapter instead of changing the original function**

The input `fn` follows a result-first callback convention: its first argument is a callback, later arguments are the ordinary inputs, and that callback receives `result` first and an optional `error` second. The requested `promisify` function must return a new function with a Promise-based interface.

The exact solution creates two nested closures. Calling `promisify(fn)` stores the original function and returns a wrapper. Calling that wrapper with `...args` creates and returns one new Promise for that invocation. This separation is important: promisifying a function does not execute it, and every later wrapper call gets an independent Promise with independent settlement functions.

**Capture every forwarded argument**

The returned regular function declares a rest parameter `...args`. JavaScript gathers the caller's separate arguments into an array while preserving their order. Inside the Promise executor, the original function is invoked as

`fn(customCallback, ...args)`.

The adapter inserts its own callback at position zero, exactly where `fn` expects it, and spreads all user arguments after it. If the wrapper is called with `(a, b, c)`, the original function observes `(customCallback, a, b, c)`.

The wrapper does not interpret, reorder, or copy the semantic contents of the arguments. Its job is only to bridge the completion mechanism.

**Translate the callback into Promise settlement**

The inserted callback receives `(result, error)`. Its branches are:

- If `error !== undefined`, reject the Promise with that exact value.
- Otherwise, resolve the Promise with `result`.

The explicit comparison with `undefined` matters. It does not test whether the error is truthy. An error value such as an empty string, zero, false, or null is still considered present and causes rejection. Only the absence marker `undefined` selects success.

On success, the first callback argument becomes the Promise fulfillment value. On failure, the result is ignored and the second callback argument becomes the rejection reason. This matches the examples, including one where both a numeric result and an error string are supplied.

**Synchronous and asynchronous callbacks both work**

The Promise executor calls `fn` immediately. If `fn` calls its callback synchronously before returning, `resolve` or `reject` settles the Promise immediately, although attached `then` or `catch` handlers still run asynchronously through the microtask queue as normal Promise semantics require.

If `fn` saves the callback and calls it later after a timer, event, or other asynchronous operation, the executor finishes while the Promise stays pending. The captured `resolve` and `reject` remain reachable through the callback closure. The later callback invocation settles the same Promise.

The adapter therefore does not need to know when `fn` completes. It only needs control of the callback through which completion is reported.

**A thrown exception receives useful native handling**

The call to `fn` occurs inside the function passed to the Promise constructor. JavaScript automatically catches a synchronous exception thrown by a Promise executor and rejects that Promise with the exception. Although the code has no explicit `try/catch`, an immediate throw from `fn` becomes a rejection.

This is separate from callback-reported failure. Callback failure goes through the explicit `reject(error)` branch; a synchronous throw is handled by the Promise constructor itself. An exception thrown asynchronously outside the callback cannot be captured automatically by this executor, which is standard JavaScript behavior and outside the stated callback contract.

**Promise settlement happens at most once**

A badly behaved callback API could invoke its callback more than once. The custom callback would call `resolve` or `reject` repeatedly, but a Promise ignores every settlement attempt after the first. The result exposed to the wrapper's caller is therefore determined by the first callback invocation or earlier synchronous exception.

The solution does not try to unregister the callback or prevent later work. It relies on the native one-settlement rule.

**What happens to `this`**

The original function is invoked as plain `fn(...)`. The wrapper is a regular function, but it does not use `fn.call(this, ...)` or `fn.apply(this, ...)`. Consequently, a method that depends on its receiving object does not automatically preserve that receiver after being passed unbound to `promisify`.

This is actual source behavior, not a hidden Promise detail. The given contract describes a standalone function, so direct invocation is sufficient. A general-purpose library adapter would need to decide whether and how to forward the wrapper's `this` value.

**Why the adapter is correct**

For one wrapper invocation, exactly one Promise is created and exactly one custom callback is passed to `fn` with all original arguments. If `fn` reports an error value other than undefined, the corresponding Promise is rejected with that same value. If it reports no error, the Promise is fulfilled with the reported result. These are precisely the two callback outcomes required by the contract. Closure isolation ensures concurrent wrapper calls cannot settle one another's Promises.

**Why the exact complexity differs from a simplistic constant-time claim**

Creating the closures is constant work, but invoking the wrapper with `a` arguments materializes the rest-parameter array and spreads those `a` entries into `fn`. The manifest correctly accounts for that forwarding work as linear in the number of arguments. The runtime and storage used internally by `fn` itself are not properties of the adapter and must be analyzed separately.

## Complexity detail

Let `a` be the number of ordinary arguments supplied to one call of the returned function. Gathering the rest arguments and forwarding them through spread requires `O(a)` time. Creating the Promise, creating the callback, and selecting a settlement branch are `O(1)`. Excluding the unknown work performed by `fn`, one wrapper invocation therefore adds `O(a)` time overhead.

The rest array retains `a` references until invocation setup no longer needs it, and the closures may retain it while the asynchronous operation is pending. Adapter space per pending call is `O(a)`. The Promise, callback, and scalar settlement functions add constant overhead. Calling `promisify` itself, before any wrapper invocation, costs `O(1)` time and space.

Elapsed time is governed by `fn`. The adapter neither delays nor accelerates its work; it only exposes the eventual callback outcome as a Promise.

## Alternatives and edge cases

- **Node.js error-first adapter:** Many Node APIs call `callback(error, result)`. This problem uses result first and error second, so an error-first implementation would reverse the outcomes.
- **Truthy error test:** `if (error)` would treat zero, false, an empty string, or null as success. The exact `error !== undefined` test recognizes every supplied error value.
- **Preserve method receiver:** Invoking `fn.call(this, callback, ...args)` can forward the wrapper's receiver. The exact implementation calls `fn` plainly and therefore does not preserve method context.
- **Synchronous callback:** The Promise settles during executor execution, while consumer handlers still follow normal microtask scheduling.
- **Asynchronous callback:** Closure capture keeps the correct settlement functions alive until the callback runs.
- **Synchronous throw from `fn`:** The Promise constructor converts it into a rejection automatically.
- **Multiple callback calls:** Only the first settlement affects the Promise; later resolve or reject calls are ignored.
- **Callback supplies both result and error:** Any second argument other than undefined wins, so the Promise rejects and the result is ignored.
- **Callback supplies no arguments:** Error is undefined, so the Promise fulfills with undefined.
- **Concurrent wrapper invocations:** Each call creates new resolver functions and a new callback closure, preventing cross-settlement.
- **Argument order:** Rest gathering and spread preserve the exact left-to-right order expected by `fn`.
- **Work inside `fn`:** Its own time, memory, side effects, and cancellation behavior are outside the adapter's `O(a)` overhead.
