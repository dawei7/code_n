## General

**Return wrappers without starting the original work yet.** `delayAll` maps every input function `fn` to a new zero-argument function. The mapping step creates closures but does not call `fn`. This preserves laziness: constructing the returned array causes no asynchronous task to begin.

The array order is preserved because JavaScript `map` places each produced wrapper at the same index as its source function. Calling returned wrapper $i$ invokes source function $i$.

**Start the source promise when its wrapper is called.** The wrapper body begins with `fn()`. The exact implementation therefore does not wait `ms` before starting the original operation. It starts the operation immediately, waits for its promise to settle, and then delays propagation of that settlement by an additional `ms`.

This distinction matches the examples: a promise that normally settles after thirty milliseconds becomes externally settled after approximately thirty plus fifty milliseconds when `ms` is fifty. It also means side effects performed by `fn` begin at wrapper invocation time, not after the added delay.

The local editorial presents an alternative that delays invoking the source function. That can produce the same total timing in simple timeout examples, but it has different side-effect timing. The approach here must follow the exact source: the delay occurs after source settlement and before the wrapper settles.

**Handle fulfillment and rejection symmetrically.** `fn().then(onFulfilled, onRejected)` registers two separate settlement handlers.

When the source fulfills with `value`, the first handler returns a new promise. That promise calls `setTimeout` and fulfills with the same `value` after `ms`.

When the source rejects with `reason`, the second handler also returns a new promise. Its timer rejects with the same `reason` after `ms`.

Promise chaining adopts the promise returned by a handler. Consequently, the outer promise returned by `then` stays pending until the timer-created promise settles. Fulfillment remains fulfillment, rejection remains rejection, and the original payload is forwarded unchanged.

**Why delaying only the success path would be wrong.** If the code used a single fulfillment handler and no rejection handler, a source rejection would propagate through the chain immediately. The problem explicitly requires both resolution and rejection to receive the additional delay. The two-argument form of `then` ensures both paths introduce a timer.

**Each call receives an independent timer.** A wrapper creates its timer only after that call's source promise settles. Calling several wrappers, or calling one wrapper several times, produces separate source promises and separate native timers. There is no shared timer or global queue that serializes them.

This means “preserving order” refers to the returned function array and its source association, not to forcing promises to settle in array order. If different source functions take different durations, their delayed results can still settle in different temporal order. Each simply receives the same additional delay.

**Closure behavior.** Each arrow created by `map` closes over the corresponding `fn` and the shared numeric `ms`. JavaScript creates the callback parameter binding separately for each map invocation, so wrappers do not all accidentally reference the last function.

The returned wrappers are arrows, so they do not define a dynamic `this` and call `fn()` as a plain function. The challenge describes zero-argument promise-returning functions and does not require receiver forwarding. If source functions depended on an object receiver, this exact wrapper would not preserve one.
Consider any returned wrapper. It invokes exactly its paired source function. If the source fulfills at time $t$ with value $v$, the fulfillment handler starts an `ms` timer and the wrapper cannot fulfill before that timer; when it fires, the wrapper fulfills with $v$. If the source rejects at time $t$ with reason $e$, the rejection handler does the analogous delayed rejection with $e$. Those are the only two ways a promise settles, so every valid source outcome is preserved and delayed as required.

Real JavaScript timers guarantee a minimum scheduling delay rather than an exact wall-clock instant. Event-loop load and timer clamping may make the observed delay longer than `ms`, but never intentionally shorter under normal host semantics.

**A synchronous exception is outside the protected promise path.** The expression `fn()` is evaluated before `.then` can be called. If `fn` throws synchronously instead of returning a promise, the wrapper throws immediately; it does not return a delayed rejected promise. The contract guarantees functions that return promises, so normal rejection should occur through the returned promise. A more defensive implementation would wrap the call with `Promise.resolve().then(fn)` or a try/catch.

## Complexity detail

Let $n$ be the number of input functions. Creating the returned array calls `map` once per entry and allocates one wrapper closure per entry, taking $O(n)$ time and $O(n)$ space.

Invoking one wrapper performs constant JavaScript bookkeeping beyond the work of `fn`: one source call, one `then` registration, one settlement handler, and one timer promise. Thus its scheduler overhead is $O(1)$ per invocation. Waiting `ms` milliseconds is elapsed time, not computational complexity.

If all $n$ wrappers are invoked once and their promises are pending simultaneously, up to $O(n)$ source chains and timers can be live. The returned wrapper array itself remains $O(n)$ storage. The source functions' own runtime and memory are external to `delayAll`'s transformation.

The value or rejection reason is forwarded by reference/value according to normal JavaScript semantics; it is not copied recursively.

## Alternatives and edge cases

- **Delay before source invocation:** Start a timer first and call `fn` after it fires. Simple examples show the same summed duration, but source side effects and rejection timing begin later than in the exact implementation.
- **Reusable `sleep` helper:** Define a promise-based delay and chain `sleep(ms).then(() => value)` in both outcome handlers. This can reduce duplication while preserving post-settlement delay.
- **`finally` alone:** `finally` can wait for a promise, but forwarding both the original fulfillment value and rejection reason correctly still depends on promise adoption semantics; explicit handlers are clearer.
- **Rejected source promise:** The reason is retained and rejection is delayed, rather than converted into fulfillment.
- **Immediate source settlement:** Even `Promise.resolve(value)` remains externally pending until the timer fires.
- **Multiple wrappers:** They are independent and may execute concurrently; array order does not serialize them.
- **Repeated wrapper call:** It invokes `fn` again and creates a fresh delayed promise each time.
- **Synchronous throw:** It escapes immediately because `fn()` is outside a protective promise callback. The contract's promise-returning guarantee avoids this case.
- **Thenable instead of native promise:** If `fn()` returns an object with a compatible `then` method, the code may work through that method, but the formal contract promises actual promises.
- **Timer accuracy:** Host scheduling can add delay beyond `ms`, so tests should allow timing tolerance.
- **Receiver-dependent function:** Calling `fn()` does not forward a wrapper receiver. Use `fn.call(this)` inside an ordinary wrapper if receiver preservation is required.
- **Sparse input array outside normal constraints:** `map` preserves holes rather than creating wrappers at missing positions.
