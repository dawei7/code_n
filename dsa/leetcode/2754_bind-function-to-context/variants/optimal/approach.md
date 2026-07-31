## General

JavaScript determines `this` from the call expression. If a function is stored as a property of `obj` and invoked through that property, the language supplies `obj` as the receiver. The polyfill can use that rule without calling `bind`, `call`, or `apply`.

**Capture the binding once**

When `bindPolyfill` runs, `this` is the target function. Save that function in the returned closure together with `obj`. The wrapper accepts a rest parameter so every later argument is retained in order.

**Create a collision-free temporary method**

On each wrapper invocation, create a fresh `Symbol`, store the target at `obj[symbol]`, and call `obj[symbol](...args)`. A symbol cannot collide with ordinary string-keyed data, and a fresh symbol also keeps nested or overlapping invocations independent. The method-call syntax makes `obj` the target's `this` value.

Return the target's result directly. Remove the temporary property in a `finally` block so the context is restored even if the target throws. Thus every successful invocation observes the required receiver and arguments, while cleanup does not depend on the returned value or control flow.

## Complexity detail

Let $a$ be the number of arguments passed to the returned function. Creating the bound wrapper takes $O(1)$ time and space. Invoking it captures and spreads $a$ arguments once, requiring $O(a)$ time and $O(a)$ auxiliary space; the target function's own work is excluded.

The contract limits $a$ to 100. That bounded domain is too narrow for reliable asymptotic timing, so a bounded-domain certificate verifies the one-pass forwarding work and explicit boundary cases instead of claiming a measured scaling verdict.

## Alternatives and edge cases

- **Built-in `bind`:** It directly performs the operation, but the problem explicitly forbids it.
- **Built-in `apply`:** It is the simplest permitted base solution, but it does not satisfy the stronger follow-up that avoids context-binding helpers.
- **Fixed string property:** A key such as `fn` can overwrite existing user data; a fresh `Symbol` avoids that collision.
- **Arrow-function targets:** Like native binding, changing the call receiver cannot replace an arrow function's lexical `this`.
- The wrapper must support zero arguments and preserve the order of up to 100 arguments.
- Reads, writes, and nested lookups through `this` must affect the supplied object.
- Cleanup belongs in `finally` so an exception cannot leave the temporary property behind.
