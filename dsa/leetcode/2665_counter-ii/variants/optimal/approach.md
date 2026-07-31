## General

The returned methods must outlive the `createCounter` call while continuing to share one mutable value. Declare `current` inside `createCounter`, then return an object whose three function values close over that lexical binding. The binding remains private but accessible to every method on that particular counter object.

`increment` adds one before returning, and `decrement` subtracts one before returning. This ordering matters: both methods report the updated value, not the value that existed before the call. `reset` assigns the original `init` to `current` and returns it. Because `init` itself is never changed, reset has the same reference point after any history of updates.

After any sequence of calls, `current` equals `init` plus the increments since the most recent reset minus the decrements since that reset. Each method performs exactly the state transition named by the operation and returns the resulting right-hand side of this relation. The invariant proves every emitted value, while separate invocations of `createCounter` receive separate lexical environments and cannot interfere.

## Complexity detail

Creating a counter and invoking any one of its methods take $O(1)$ time. The closure retains two numeric bindings regardless of the number of calls, so it uses $O(1)$ space. An app harness that processes $q$ calls and collects their outputs necessarily uses $O(q)$ total time and output space, but the required counter operation remains constant-time per call.

The $O(1)$ per-operation bound is verified by an asymptotic-optimality certificate: returning one result already requires $\Omega(1)$ work, and each accepted method performs a fixed number of primitive updates.

## Alternatives and edge cases

- **Class instance:** A class with three prototype methods can maintain the same state, but the required factory returning an object of functions does not need class machinery.
- **Public object property:** Storing `current` as a visible property works mechanically but exposes mutable state that a closure can keep private.
- **Post-increment or post-decrement:** Returning `current++` or `current--` would report the old value and violate the contract.
- An empty call sequence returns an empty result and must not mutate the newly created counter.
- Repeated resets always return the original `init`, even without an intervening update.
- Incrementing or decrementing may move beyond the allowed range for `init`; that constraint applies only to initialization.
- Each counter object must own independent state rather than sharing a module-level variable.
