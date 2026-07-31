## General

JavaScript supplies a method's receiver as `this`. The polyfill can therefore turn the target function into a temporary method of `context`, invoke that method, and then remove it.

**Use a collision-free property**

Create a fresh `Symbol` and store the function—the value on which `callPolyfill` was invoked—at `context[symbol]`. Unlike a string key, this symbol cannot overwrite an ordinary property or collide with another polyfill invocation. Calling `context[symbol](...args)` uses normal method-call semantics, so JavaScript binds `this` to `context` and forwards every additional argument in order. Return that invocation's value unchanged.

Place deletion in a `finally` block. This restores the context even when the target throws, so the temporary implementation detail does not remain visible after the call. The required context is a non-null object, so it can serve as the temporary receiver.

## Complexity detail

Let $a$ be the number of additional arguments. Capturing and spreading those arguments takes $O(a)$ time and $O(a)$ space for the rest-parameter array. Creating, installing, and deleting one symbol property takes $O(1)$ expected time and space. The target function's own runtime and storage are outside the polyfill's complexity.

The contract bounds $a$ by $99$. That complete legal range is too small for a reliable scaling benchmark, so the bounded-domain certificate verifies the one-pass forwarding work and the argument-count boundary instead.

## Alternatives and edge cases

- **Built-in `Function.call`:** It directly provides the desired binding, but the problem explicitly forbids it.
- **Built-in `apply` or `bind`:** Either can bind the receiver, but using a temporary symbol demonstrates the required mechanism without substituting another context-binding helper.
- **Fixed string property:** A name such as `fn` can overwrite data already stored on the context; a fresh `Symbol` avoids that collision.
- The polyfill must work when there are no additional arguments.
- Preserve argument order and return objects, strings, numbers, booleans, or `null` without conversion.
- The target may mutate `this`; the call must operate on the supplied object rather than a clone.
- Delete the temporary property in `finally` so cleanup also occurs when invocation throws.
