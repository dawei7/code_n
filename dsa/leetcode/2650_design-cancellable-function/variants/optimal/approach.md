## General

The controller is a two-way bridge. Start the generator with `next()`. While its iteration result is not done, await the yielded promise. Feed a resolved value back through `next(value)`; if awaiting rejects, feed that reason back through `throw(reason)`. Either call may execute generator code until the next yield, return, or uncaught throw.

**Interrupt only the current wait**

Store the reject callback of one wrapper promise around the currently yielded promise. The `cancel` callback sets a permanent cancellation flag and rejects that wrapper with the literal string `"Cancelled"`. The driver's existing rejection path therefore invokes `generator.throw("Cancelled")` exactly once.

Using one replaceable reject callback matters. Racing every yield against one never-settled cancellation promise would retain one reaction for every completed race until cancellation, allowing auxiliary memory to grow with the number of yields. The current-wait bridge retains only constant controller state.

After cancellation, the loop condition prevents another generator resumption. If `generator.throw` is uncaught, it throws out of the async driver and rejects the returned promise. If the generator catches it, `throw` returns the next iteration result. Returning that result's `value` from the async driver resolves with either the catch block's return or its next yielded promise, using normal promise assimilation, and no later generator code runs.

Without cancellation, each iteration result is handled exactly according to the generator protocol. A `done` result resolves with its return value, while an escaping synchronous throw or rethrown promise rejection rejects the async driver.

## Complexity detail

Let $y$ be the number of yielded promises processed before normal completion or cancellation. The controller performs constant scheduling and generator-protocol work per yield, for $O(y)$ overhead. It stores a flag, one reject callback, one iteration result, and one live wrapper promise, giving $O(1)$ auxiliary controller space apart from the generator and its yielded promise.

## Alternatives and edge cases

- **One shared cancellation promise with `Promise.race`:** This is concise, but every completed race can leave a reaction attached to the still-pending cancellation promise, growing retained memory with $y$.
- **Call `generator.return()`:** This runs return/finally semantics but does not inject the required `"Cancelled"` value through `throw`.
- **Reject only the outer promise:** That would not let the generator catch cancellation and return a recovery result.
- A yielded promise rejection follows the same `generator.throw` route as cancellation, but must not set the cancellation flag; a catch block may continue yielding normally.
- Calling `cancel` more than once is idempotent.
- Cancellation after the generator is done cannot change the already settled returned promise.
- If cancellation is caught and the generator yields once, await that yielded promise as the final controller result without resuming the generator.
