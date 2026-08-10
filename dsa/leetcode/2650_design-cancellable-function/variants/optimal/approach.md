## General

**Drive the generator one yielded Promise at a time**

A generator does not run continuously. It advances only when the controller calls:

- `generator.next(value)` to deliver a successful yielded result;
- `generator.throw(error)` to inject a rejection or cancellation.

The returned controller Promise repeatedly waits for the current yielded Promise, feeds its outcome back into the generator, and stops when the generator returns or throws.

Cancellation is modeled as one more injected error: the exact string `"Cancelled"`.

**Track cancellation and the current waiter**

Two closure variables coordinate the cancel function and asynchronous driver:

- `cancelled` records whether cancellation has ever been requested;
- `rejectCurrent` points to the rejection function of the bridge Promise currently being awaited, or null when no bridge is pending.

The cancel function is synchronous. On its first call, it sets `cancelled = true`. If a bridge is active, it rejects that bridge with `"Cancelled"`.

Later cancel calls do nothing because the flag is already true. Cancellation is idempotent.

**Start the generator**

The async immediately invoked function begins with:

`let iteration = generator.next()`.

An iterator result has:

- `value`: either the yielded Promise or final return value;
- `done`: whether the generator has finished.

If the generator returns immediately, `done` is true. The while-loop is skipped and the async driver returns `iteration.value`, resolving its Promise with the generator's return value.

**Bridge the currently yielded Promise**

While not cancelled and not done, the driver creates a new Promise. Its executor:

1. saves its `reject` function in `rejectCurrent`;
2. wraps `iteration.value` with `Promise.resolve`;
3. forwards fulfillment or rejection to the bridge;
4. rejects immediately if cancellation was already observed.

`Promise.resolve` safely assimilates the yielded Promise or thenable and would also handle a plain value, although the contract says yields are Promises.

The driver then awaits this bridge.

**Feed fulfillment back through `next`**

If the yielded Promise fulfills with value $v$, the bridge fulfills with $v$. The driver:

- clears `rejectCurrent`;
- calls `generator.next(v)`.

Inside the generator, the suspended `yield` expression evaluates to $v$. Execution continues until the next yield, return, or throw, producing a new iterator result.

The loop repeats for another yielded Promise or finishes on `done`.

**Feed rejection back through `throw`**

If the yielded Promise rejects, awaiting the bridge enters `catch(error)`. The driver clears the current reject reference and calls:

`generator.throw(error)`.

This makes the suspended `yield` throw inside the generator.

- If the generator catches that error, it can yield another Promise or return a value, and the returned iterator result lets the driver continue.
- If it does not catch the error, `generator.throw` itself throws. That exception escapes the async driver, causing the returned Promise to reject with the same error.

This exactly mirrors normal generator exception semantics.

**Cancellation uses the same rejection path**

If `cancel()` runs while the driver awaits a bridge, `rejectCurrent("Cancelled")` rejects it. The driver's catch block calls:

`generator.throw("Cancelled")`.

The generator therefore receives cancellation at its suspended yield and may catch it with ordinary `try/catch`.

If uncaught, the driver Promise rejects with `"Cancelled"`. If caught and the generator returns a partial result, that return becomes the resolved driver result.

**Why no more normal driving occurs after cancellation**

The loop condition begins with `!cancelled`. After cancellation is injected and `generator.throw` returns an iterator result, the next loop check fails.

The driver returns `iteration.value` directly:

- if the generator returned, this is its return value;
- if its catch block yielded one final Promise, returning it from an async function adopts that Promise's settlement without resuming the generator afterward.

Thus cancellation gives the generator one chance to handle the injected error, then normal iteration stops.

**Trace uncaught cancellation**

A generator yields a 200-millisecond Promise. The bridge stores its reject function and waits.

At time 100, `cancel` rejects the bridge with `"Cancelled"`. The catch block throws that string into the generator. With no catch inside the generator, `generator.throw` throws outward, so the returned controller Promise rejects at about time 100.

The original 200-millisecond Promise may still settle later, but the bridge is already rejected and cannot change the result.

**Trace caught cancellation**

Suppose the generator has accumulated result one and is waiting inside a `try`. Cancellation throws into that yield. The generator's catch returns the partial result one.

`generator.throw` returns `{ value: 1, done: true }`. Since `cancelled` is true, the loop ends and the async driver returns one, fulfilling the controller Promise.

**Why cancellation after completion does nothing observable**

If the generator completes immediately or before the scheduled cancel call:

- the driver Promise is already settled;
- `rejectCurrent` is null;
- cancel only flips its private flag.

Settled Promises cannot change state, so the completed result remains intact.


At the top of each driver iteration, `iteration` is exactly the latest result from advancing the generator, and if it is not done, its value is the sole Promise whose outcome must be delivered next.

The bridge converts source fulfillment, source rejection, or cancellation into one await outcome. The driver delivers that outcome through `next` or `throw` exactly once. This preserves generator semantics until completion or cancellation.

The async driver's final return or uncaught exception then supplies the required outer Promise settlement.

## Complexity detail

Let $y$ be the number of yielded Promises the driver processes before completion or cancellation. Each yield creates one bridge and performs constant controller work, so scheduling overhead is $O(y)$, excluding time and work inside yielded Promises.

Only the current iterator result, flags, and one reject callback are retained by the controller, giving $O(1)$ controller space. The generator itself owns its suspended local state and call frames.

## Alternatives and edge cases

- **Poll a cancelled flag:** Cannot promptly interrupt a long pending Promise; rejecting the current bridge wakes the driver immediately.
- **Race every yield with a cancellation Promise:** Valid, but the stored reject callback is a compact one-pending-wait implementation.
- **Call `generator.return()` on cancellation:** Skips the required `throw("Cancelled")` semantics and prevents generator catch logic.
- **Immediate generator return:** The controller Promise resolves without waiting, and later cancellation is harmless.
- **Yielded Promise rejects:** Its error is thrown into the generator and may be caught.
- **Cancellation uncaught:** The outer Promise rejects with the exact string.
- **Cancellation caught with return:** The outer Promise resolves with the returned recovery value.
- **Repeated cancel calls:** Only the first has an effect.
- **Underlying Promise after cancellation:** It is not physically cancelled; its later settlement cannot change the bridge.
- **One pending bridge:** `rejectCurrent` always refers only to the yield currently being awaited.
