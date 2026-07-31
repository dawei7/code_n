## General

Create a Boolean `called` in the outer `once` function and return an inner variadic function that closes over it. If the flag is already true, return `undefined` immediately. Otherwise, set the flag and forward the current receiver plus all arguments to `fn` with `apply`.

Marking the wrapper as used before invoking `fn` is important. It guarantees “at most once” even if `fn` throws an exception or invokes the wrapper reentrantly. Forwarding with `fn.apply(this, args)` also preserves method-style receiver semantics instead of silently replacing `this`.

Initially, `called` is false, so exactly the first invocation reaches `fn` and returns its result. That invocation changes the flag permanently to true before any user code runs. Every later invocation then takes the early-return branch and cannot call `fn`. Each call to `once` creates a separate lexical binding, so independently wrapped functions receive independent permissions.

## Complexity detail

Excluding the wrapped function's own runtime, creating the wrapper and invoking it each take $O(1)$ time. The closure retains one Boolean and one function reference, so it uses $O(1)$ space. Forwarded argument storage belongs to the invocation interface rather than growing retained wrapper state.

The constant overhead is certified as asymptotically optimal: every invocation must make at least one decision, and the accepted wrapper performs only a fixed state check and, on the first call, one fixed state update.

## Alternatives and edge cases

- **Call-count integer:** Incrementing a numeric counter can enforce the same rule, but a Boolean expresses the two-state contract directly.
- **Replace the function after use:** Reassigning `fn` to an empty function works, but a flag separates permission state from the original callable more clearly.
- **Arrow-function wrapper:** An arrow would capture lexical `this` and could break callers that expect method-style receiver forwarding.
- A legitimate first result may be `undefined`; the wrapper is still consumed because permission depends on invocation, not return value.
- If the first call throws, subsequent calls must still be suppressed to satisfy “at most once.”
- Reentrant calls made by `fn` are suppressed because the flag is set before forwarding.
- Separate wrappers around the same `fn` each permit their own first call.
